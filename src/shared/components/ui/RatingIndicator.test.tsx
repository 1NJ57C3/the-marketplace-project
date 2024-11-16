import { render, screen } from "@testing-library/react";
import RatingIndicator from "./RatingIndicator";

describe("RatingIndicator", () => {
  it("renders when given a numeric rating", () => {
    // Render with a simple numeric rating
    render(<RatingIndicator rating={3} />);
    // Check if the rating value is displayed correctly
    expect(screen.getByTestId("rating-indicator")).toBeInTheDocument();
  });

  it("renders the correct number of filled bubbles", () => {
    // Render with a rating
    render(<RatingIndicator rating={4} />);
    // Check for the correct number of filled symbols (●)
    expect(screen.getAllByText("●")).toHaveLength(4);
  });

  it("renders the correct number of empty bubbles", () => {
    // Render with a partial rating
    render(<RatingIndicator rating={2} />);
    // Check for the correct number of empty symbols (○)
    expect(screen.getAllByText("○")).toHaveLength(3);
  });

  it("renders nothing when rating is invalid", () => {
    // Render with an invalid rating
    const { container } = render(<RatingIndicator rating={-1} />);
    // Expect no visual output
    expect(container.textContent).toBe("");
  });
});
