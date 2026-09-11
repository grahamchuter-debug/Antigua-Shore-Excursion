/**
 * Shared booking engine tests — Antigua Phase 15D (Classic Beach Day only).
 */
import assert from "node:assert/strict";
import { test } from "node:test";
import {
  ANTIGUA_BOOKABLE_PRODUCTS,
  ANTIGUA_CANCELLATION_COPY,
  findAntiguaBookingProduct,
} from "../destinations/antigua-products";
import { antiguaBookingCore } from "../destinations/antigua";
import {
  assertClientTotalMatches,
  calculateBookingQuote,
  createBookingReference,
  destinationBrandFromCore,
  requestedCustomerEmail,
  statusAfterPaymentSuccess,
  supplierRequestEmail,
  validateCruise,
  validateCustomer,
} from "./index";

const brand = destinationBrandFromCore(antiguaBookingCore);
const classic = findAntiguaBookingProduct("classic-beach-day");
assert.ok(classic);

test("single Antigua product ID present", () => {
  assert.equal(ANTIGUA_BOOKABLE_PRODUCTS.length, 1);
  assert.equal(ANTIGUA_BOOKABLE_PRODUCTS[0]!.id, "classic-beach-day");
});

test("classic beach day paying guest 77 infant free; requires paying guest", () => {
  assert.equal(classic!.pricing.adultAmount, 77);
  assert.equal(classic!.pricing.childAmount, null);
  assert.equal(classic!.pricing.childPricingStatus, "not_sold");
  assert.equal(classic!.pricing.infantAmount, 0);
  assert.equal(classic!.pricing.infantPricingStatus, "priced");
  assert.equal(calculateBookingQuote(classic!, { adults: 1, children: 0, infants: 0 }).amountCents, 7700);
  assert.equal(calculateBookingQuote(classic!, { adults: 2, children: 0, infants: 0 }).amountCents, 15400);
  assert.equal(calculateBookingQuote(classic!, { adults: 1, children: 0, infants: 1 }).amountCents, 7700);
  assert.equal(calculateBookingQuote(classic!, { adults: 1, children: 0, infants: 1 }).partySize, 2);
  assert.throws(() => calculateBookingQuote(classic!, { adults: 0, children: 0, infants: 1 }));
  assert.throws(() => calculateBookingQuote(classic!, { adults: 1, children: 1, infants: 0 }));
});

test("max 10 guests; 11 rejected; infants count toward max", () => {
  assert.equal(classic!.capacity.maxGuestsPerBooking, 10);
  assert.doesNotThrow(() => calculateBookingQuote(classic!, { adults: 10, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(classic!, { adults: 11, children: 0, infants: 0 }));
  assert.throws(() => calculateBookingQuote(classic!, { adults: 0, children: 0, infants: 0 }));
  assert.doesNotThrow(() => calculateBookingQuote(classic!, { adults: 9, children: 0, infants: 1 }));
  assert.throws(() => calculateBookingQuote(classic!, { adults: 9, children: 0, infants: 2 }));
});

test("client total must match server quote", () => {
  const quote = calculateBookingQuote(classic!, { adults: 1, children: 0, infants: 1 });
  assert.doesNotThrow(() => assertClientTotalMatches(quote, 7700));
  assert.throws(() => assertClientTotalMatches(quote, 1));
});

test("payment success status is requested not confirmed", () => {
  assert.equal(statusAfterPaymentSuccess("request"), "requested");
});

test("booking references use Antigua W2ATG prefix", () => {
  assert.match(createBookingReference(antiguaBookingCore), /^W2ATG-/);
  assert.equal(antiguaBookingCore.bookingRefPrefix, "W2ATG");
});

test("customer and cruise validation", () => {
  assert.equal(
    validateCustomer({ name: "Alex Traveller", email: "alex@example.com", phone: "+447700900123" }),
    null,
  );
  assert.ok(validateCustomer({ name: "A", email: "x", phone: "1" }));
  assert.ok(
    validateCruise({
      date: "2020-01-01",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    }),
  );
  assert.equal(
    validateCruise({
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    }),
    null,
  );
});

test("cancellation copy covers 14-day policy and full refund", () => {
  assert.match(ANTIGUA_CANCELLATION_COPY.customerCancellation, /outside 14 days/i);
  assert.match(ANTIGUA_CANCELLATION_COPY.customerCancellation, /14th day/i);
  assert.match(ANTIGUA_CANCELLATION_COPY.unableToConfirm, /full refund/i);
  assert.match(ANTIGUA_CANCELLATION_COPY.paymentNotConfirmation, /confirm.*separately|separately.*confirm/i);
});

test("customer email never exposes SEG or internal codes", () => {
  const mail = requestedCustomerEmail({
    brand,
    product: classic!,
    reference: "W2ATG-TEST0001",
    cruise: {
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    },
    guests: { adults: 1, children: 0, infants: 0 },
    amountLabel: "USD $77.00",
    customerName: "Alex Traveller",
  });
  const blob = JSON.stringify(mail);
  assert.doesNotMatch(blob, /\bSEG\b|caagclssc|Shore Excursions Group|info@wowatour/i);
  assert.match(blob, /request|confirm/i);
});

test("ops email includes internal supply notes for Graham", () => {
  const mail = supplierRequestEmail({
    product: classic!,
    reference: "W2ATG-TEST0001",
    cruise: {
      date: "2026-12-15",
      shipName: "Celebrity Beyond",
      shipSlug: "not-listed",
      cruiseLine: "",
      isCustomShip: true,
      scheduleMatched: false,
    },
    guests: { adults: 1, children: 0, infants: 1 },
    amountLabel: "USD $77.00",
    customer: {
      name: "Alex Traveller",
      email: "alex@example.com",
      phone: "+447700900123",
    },
    destinationLabel: "Antigua Shore Excursions — new booking request",
  });
  const blob = JSON.stringify(mail);
  assert.match(blob, /caagclssc|SEG_MANUAL/i);
});

test("reject foreign destination product lookup", () => {
  assert.equal(findAntiguaBookingProduct("belize-cave-tubing"), null);
  assert.equal(findAntiguaBookingProduct("highlights-and-beach-break"), null);
  assert.equal(findAntiguaBookingProduct("soufriere-volcano-waterfalls-tour"), null);
});
