import { cleanup, render, screen } from "@testing-library/react";
import RatingIndicators from "./RatingIndicators";

function renderRatingIndicators(rating: number) {
  return render(<RatingIndicators rating={rating} />);
}

describe("RatingIndicators", () => {
  it("renders when given a numeric rating", () => {
    renderRatingIndicators(3);
    expect(screen.getByTestId("rating-indicators")).toBeInTheDocument();
  });

  it("renders the correct number of filled and empty bubbles", () => {
    const testCases = [
      { rating: 5, filled: 5, empty: 0 },
      { rating: 4, filled: 4, empty: 1 },
      { rating: 3, filled: 3, empty: 2 },
      { rating: 2, filled: 2, empty: 3 },
      { rating: 1, filled: 1, empty: 4 },
      { rating: 0, filled: 0, empty: 5 },
    ];

    testCases.forEach(({ rating, filled, empty }) => {
      renderRatingIndicators(rating);
      expect(screen.queryAllByText("●")).toHaveLength(filled);
      expect(screen.queryAllByText("○")).toHaveLength(empty);
      cleanup();
    });
  });

  it("renders nothing when rating is invalid", () => {
    const testCases = [{ rating: -1 }, { rating: 6 }];

    testCases.forEach(({ rating }) => {
      renderRatingIndicators(rating);
      expect(screen.queryByTestId("rating-indicators")).not.toBeInTheDocument();
      cleanup();
    })
    }
  );
});
