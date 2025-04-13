import "./RatingIndicators.css";

interface RatingIndicatorsProps {
  rating: number;
}

function RatingIndicators({ rating }: RatingIndicatorsProps) {
  if (rating < 0 || rating > 5) return null;

  const indicators: React.ReactNode[] = [];
  const description = `Rated ${rating.toFixed(1)} out of 5`;

  const roundedRating = Math.round(rating * 2) / 2;
  const whole = Math.trunc(roundedRating);

  for (let i = 0; i < 5; i++) {
    if (i === whole && roundedRating % 1 === 0.5) {
      indicators.push(<span key={`rating-${i}`}>◐</span>);
    } else {
      indicators.push(
        <span key={`rating-${i}`}>{i < roundedRating ? "●" : "○"}</span>
      );
    }
  }

  return (
    <div
      className="rating-indicators"
      data-testid="rating-indicators"
      title={description}
      aria-label={description}
    >
      {indicators}
    </div>
  );
}

export default RatingIndicators;
