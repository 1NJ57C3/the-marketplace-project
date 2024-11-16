import React from "react";
import "./RatingDisplay.css";

interface RatingDisplayProps {
  rating: number;
};

function RatingDisplay({ rating }: RatingDisplayProps) {
  // if (rating < 0) throw new Error("Rating must be a positive number"); // TODO revise test to accept Error?
  if (rating < 0) return null;

  const indicators: React.ReactNode[] = [];
  const description = `Rated ${rating} out of 5`;

  for (let i = 0; i < 5; i++) {
    indicators.push(<span key={`rating-${i}`}>{i < rating ? "●" : "○"}</span>);
  }

  return (
    <div
      className="rating-display"
      data-testid="rating-display"
      title={description}
      aria-label={description}
    >
      {indicators}
    </div>
  );
}

export default RatingDisplay;
