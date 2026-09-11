/**
 * Antigua destination booking core.
 * Product catalogue: shared/destinations/antigua-products.ts
 * Public editorial: scripts/build-antigua-site.py
 * Internal supply mapping: product.supplierReferenceNotes (never public HTML)
 */
import type { DestinationBookingCore } from "../world-booking/types";

export const antiguaBookingCore = {
  id: "antigua",
  siteName: "Antigua Shore Excursions",
  siteHostname: "antiguashoreexcursion.com",
  siteUrl: "https://antiguashoreexcursion.com",
  bookingEmail: "hello@antiguashoreexcursion.com",
  originatingSite: "antiguashoreexcursion.com",
  originatingPort: "St John's, Antigua",
  bookingRefPrefix: "W2ATG",
  sessionKeyPrefix: "w2-atg-booking",
  sessionKeyVersion: 1,
  currencyCode: "USD",
  bookableWindow: {
    start: "2026-09-01",
    end: "2028-12-31",
  },
  /** No Antigua schedule import — cruise date/ship are customer-entered. */
  schedulePortSlug: "antigua",
  customShipSlug: "not-listed",
  contactPath: "/contact",
  termsPath: "/terms",
  privacyPath: "/privacy",
} as const satisfies DestinationBookingCore;
