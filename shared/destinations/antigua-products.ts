import { antiguaBookingCore } from "./antigua";
import type { AgeBand, BookableProductConfig, ProductCapacity, ProductPricing } from "../world-booking/types";

/**
 * Operational routing: Wow A Tour ops mailbox for Graham’s manual fulfilment.
 * Public customers never see SEG. Graham places corresponding bookings via his
 * established SEG affiliate / white-label account using INTERNAL supply refs only.
 */
const OPERATIONS = {
  id: "wow-a-tour-operations",
  displayName: "Wow A Tour",
  notificationEmail: "info@wowatour.com",
  routingStatus: "production_ready" as const,
};

const REQUEST_SETTLEMENT = "charge_refund" as const;

/** Graham online max — never describe as supplier / vehicle / boat capacity. */
const ATG_CAPACITY: ProductCapacity = {
  minGuests: 1,
  maxGuestsPerBooking: 10,
  maxGuestsPerBookingSource: "approved",
  supplierGroupSize: null,
  maxGuestsPerGuide: null,
};

/**
 * Launch model (Phase 15D Graham-approved):
 * Ages 0–2 infant FREE (recorded).
 * Ages 3+ paying guest USD 77 (no invented child discount).
 * Technical adult band = paying guests ages 3+; child band not sold.
 */
const PAYING_INFANT_BANDS: readonly AgeBand[] = [
  { id: "adult", label: "Guests (ages 3+)", minAge: 3, maxAge: null, pricingStatus: "priced" },
  { id: "child", label: "Children", minAge: 3, maxAge: 11, pricingStatus: "not_sold" },
  { id: "infant", label: "Infants (0–2)", minAge: 0, maxAge: 2, pricingStatus: "priced" },
];

function payingGuestInfantUsd(payingAmount: number): ProductPricing {
  return {
    model: "adult_child",
    currency: "USD",
    adultAmount: payingAmount,
    childAmount: null,
    childPricingStatus: "not_sold",
    infantAmount: 0,
    infantPricingStatus: "priced",
    pricingNeedsConfirmation: false,
  };
}

const SHARED_PENDING = [
  "Customer cancellation APPROVED: free outside 14 days before excursion; from the 14th day non-refundable.",
  "Unable to confirm after payment: full refund to original payment method.",
  "Meeting: approximately 5–10 minute walk from cruise ship pier; exact instructions after confirmation.",
  "Fulfilment: Graham places corresponding booking via established SEG affiliate / white-label route (INTERNAL).",
  "Payment received ≠ excursion confirmed.",
  "Online max 10 guests per booking (Graham online limit — not supplier capacity).",
  "At least one paying guest (ages 3+) required.",
  "commercial_status=SEG_FULFILMENT_READY · fulfilment_mode=SEG_MANUAL · supplier=UNKNOWN · direct_supplier_status=NOT_CONTACTED · net_cost=UNKNOWN · margin=UNKNOWN",
] as const;

export const ANTIGUA_CANCELLATION_COPY = {
  customerCancellation:
    "Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable. If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  freeWindow: "Free cancellation outside 14 days before your excursion.",
  insideWindow: "From the 14th day before your excursion, bookings are non-refundable.",
  unableToConfirm:
    "If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  paymentNotConfirmation:
    "Secure your booking request with payment today. We'll confirm your excursion separately, and if we're unable to confirm it, you'll receive a full refund.",
  meetingInstructions: "Meeting instructions will be provided with your confirmed excursion details.",
  overTenGuidance: "For groups larger than 10, email hello@antiguashoreexcursion.com before requesting.",
} as const;

const CLASSIC: BookableProductConfig = {
  id: "classic-beach-day",
  destinationId: antiguaBookingCore.id,
  slug: "classic-beach-day",
  name: "Classic Beach Day",
  durationLabel: "4 hours",
  bookingMode: "request",
  availability: "live",
  bookingPath: "/book/classic-beach-day",
  receivedPath: "/book/classic-beach-day/received",
  confirmedPath: "/book/classic-beach-day/received",
  productPath: "/classic-beach-day/",
  pricing: payingGuestInfantUsd(77),
  ageBands: PAYING_INFANT_BANDS,
  capacity: ATG_CAPACITY,
  requiredCustomerFields: ["name", "email", "phone"],
  supplier: OPERATIONS,
  paymentSettlement: REQUEST_SETTLEMENT,
  schedulePortSlug: "antigua",
  pendingCommercialRules: [
    ...SHARED_PENDING,
    "Paying guest USD 77 (ages 3+) · Infant 0–2 FREE (must record) · require ≥1 paying guest",
    "Fryes Beach · lunch + non-alcoholic welcome drink · transport included in excursion",
    "Optional Cades Reef boat/snorkel NOT included (own expense)",
    "Optional water sports NOT included (own expense)",
    "Not wheelchair accessible · moderate activity",
    "Do not invent beach furniture, supplier name, availability, or return-to-ship guarantees",
  ],
  supplierReferenceNotes: [
    "INTERNAL SUPPLY: SEG_MANUAL · caagclssc",
    "INTERNAL CODE: caagclssc",
    "Supplier contact: UNKNOWN · NOT_CONTACTED · net/margin UNKNOWN",
    "Fulfilment: place via established SEG affiliate / white-label route (manual — do not automate).",
    "Selling: Paying guest USD 77 (ages 3+) · Infant FREE (0–2 recorded).",
    "Customer cancellation: Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable.",
    "Unable to confirm after payment: full refund to original payment method.",
  ],
};

export const ANTIGUA_BOOKABLE_PRODUCTS: readonly BookableProductConfig[] = [CLASSIC];

export function findAntiguaBookingProduct(productId: string): BookableProductConfig | null {
  return ANTIGUA_BOOKABLE_PRODUCTS.find((p) => p.id === productId) ?? null;
}

export function listAntiguaBookingProducts(): readonly BookableProductConfig[] {
  return ANTIGUA_BOOKABLE_PRODUCTS;
}
