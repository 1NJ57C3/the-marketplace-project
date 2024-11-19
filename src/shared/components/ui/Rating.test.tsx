import { cleanup, render, screen } from "@testing-library/react";
import Rating from "./Rating";

function renderRating(rating: number, reviewCount: number) {
  return render(<Rating rating={rating} reviewCount={reviewCount} />);
}

describe("Rating", () => {
  const testCases = [
    { rating: 4, reviewCount: 120 },
    { rating: 4.7, reviewCount: 138 },
    { rating: 4.2, reviewCount: 19324 },
    { rating: 3.8, reviewCount: 2873 },
  ];

  it("renders when given appropriate numerical arguments", () => {
    renderRating(4, 120);
    expect(screen.getByTestId("rating")).toBeInTheDocument();
    expect(screen.getByTestId("rating-indicators")).toBeInTheDocument();
  });

  it("renders correct number of reviews", () => {
    testCases.forEach(({ rating, reviewCount }) => {
      renderRating(rating, reviewCount);
      expect(screen.getByTestId("rating-indicators")).toBeInTheDocument();
      expect(screen.getByText(reviewCount)).toBeInTheDocument();
      cleanup();
    });
  });

  it("provides correct accessible labels", () => {
    testCases.forEach(({ rating, reviewCount }) => {
      renderRating(rating, reviewCount);
      expect(screen.getByTestId("review-count")).toHaveAccessibleName(
        `${reviewCount} Reviews`
      );
      cleanup();
    });
  });
});
