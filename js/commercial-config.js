/**
 * Public commercial status for Antigua Shore Excursions (Phase 15D).
 * Internal supply references must never appear on customer pages.
 *
 * Gate values:
 * - PRODUCTION_READY_LOCKED — journey visible; live Pay & request disabled
 * - BOOKING_ENABLED — live checkout allowed (requires Worker LIVE unlock too)
 */
window.ATG_COMMERCIAL = {
  bookingsApiUrl: "https://antigua-bookings-prod.dark-violet-8d91.workers.dev",
  email: "hello@antiguashoreexcursion.com",
  siteName: "Antigua Shore Excursions",
  defaultPublicBookingStatus: "BOOKING_ENABLED",
  cancellation:
    "Free cancellation outside 14 days before your excursion. From the 14th day before your excursion, bookings are non-refundable.",
  paymentNotConfirmation:
    "Secure your booking request with payment today. We'll confirm your excursion separately, and if we're unable to confirm it, you'll receive a full refund.",
  unableToConfirm:
    "If we are unable to confirm your excursion after payment, you will receive a full refund to your original payment method.",
  meetingInstructions:
    "Meeting instructions will be provided with your confirmed excursion details. Expect an approximately 5–10 minute walk from the cruise ship pier.",
  overTenGuidance:
    "For groups larger than 10, email hello@antiguashoreexcursion.com before requesting.",
  products: {
    "classic-beach-day": {
      productId: "classic-beach-day",
      slug: "classic-beach-day",
      name: "Classic Beach Day",
      shortTitle: "Classic Beach Day",
      productPath: "/classic-beach-day/",
      bookingPath: "/book/classic-beach-day/",
      receivedPath: "/book/classic-beach-day/received/",
      adultUsd: 77,
      childUsd: null,
      infantUsd: 0,
      guestModel: "ages3_plus_infant",
      durationLabel: "4 hours",
      maxGuests: 10,
      publicBookingStatus: "BOOKING_ENABLED",
      displayPrice: "Guests (ages 3+) $77 · Infants (0–2) free",
    },
  },
};
