// Small two-tone pictograms use different silhouettes, not cropped lead scenes.
const glyphs = {
  gaza: '<path d="M4 9h5v12H4zm7-5h5v17h-5zm7 8h4v9h-4z" fill="#f4d1a1"/><path d="M3 21h20M7 12v2m6-7v2m0 3v2m7 1v2"/>',
  climate: '<circle cx="13" cy="13" r="9" fill="#a9d9c8"/><path d="M4 13h18M13 4c-5 5-5 13 0 18 5-5 5-13 0-18Z"/>',
  loan: '<circle cx="13" cy="13" r="9" fill="#ffd27f"/><path d="M17 8c-6-4-10 11-1 10M8 11h7m-8 3h7"/>',
  voyager: '<path d="M5 5c6 0 11 4 12 10C12 18 4 12 5 5Z" fill="#c0daf0"/><path d="m7 14 5-4m0 5 7 6m-5-4 5-5m-9 8 9-3m1-11v4m-2-2h4"/>',
  port: '<path d="M5 20V5h15L12 12H5m15-7v11"/><path d="M3 19h20l-3 4H6Z" fill="#f7c77d"/>',
  trade: '<path d="M4 7h9v13H4Z" fill="#f7dca6"/><path d="M6 11h5m-5 3h5m4-4h8m-3-3 3 3-3 3m2 4h-7m3-3-3 3 3 3"/>',
  inflation: '<path d="M4 15h4v7H4zm7-4h4v11h-4zm7-4h4v15h-4z" fill="#e8d487"/><path d="m4 11 8-5 6-3m-4 0h4v4"/>',
  sanctions: '<path d="m13 4 8 3v6c0 4-3 7-8 9-5-2-8-5-8-9V7Z" fill="#addace"/><path d="m9 9 8 8m0-8-8 8"/>',
  energy: '<path d="m14 3-9 12h7l-1 8 10-13h-7Z" fill="#ffce78"/>',
  border: '<path d="M4 18l5-9 4 7 5-9 4 11Z" fill="#d6db9a"/><path d="M13 4v3m0 2v3m0 7v3"/>',
};
function deskIcon(kind, tone) {
  return `<svg viewBox="0 0 26 26"><rect width="26" height="26" rx="4" fill="${tone}"/><g fill="none" stroke="#fff4dc" stroke-width="1.45" stroke-linecap="round" stroke-linejoin="round">${glyphs[kind]}</g></svg>`;
}
