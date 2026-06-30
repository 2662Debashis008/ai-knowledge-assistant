"use client";

export default function LoadingSpinner() {
  return (
    <div
      aria-label="Loading"
      className="loading-dots"
      role="status"
    >
      <span />
      <span />
      <span />
    </div>
  );
}
