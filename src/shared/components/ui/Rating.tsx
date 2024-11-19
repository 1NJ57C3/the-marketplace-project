import RatingIndicators from "./RatingIndicators";

interface RatingProps {
  rating: number;
  reviewCount: number;
}

function Rating({ rating, reviewCount }: RatingProps) {
  return (
    <div className="rating" data-testid="rating">
      <RatingIndicators rating={rating} /> (
      <a
        href=""
        data-testid="review-count"
        aria-label={`${reviewCount} Reviews`}
        title={`${reviewCount} Reviews`}
      >
        {reviewCount}
      </a>
      )
    </div>
  );
}

export default Rating;
