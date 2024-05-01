def can_paint_ribbon(n, m, k):
    # If k >= n, Tia can repaint all parts to the same color no matter what Raj does
    if k >= n:
        return "No"
    # If m == 1, Tia can repaint all parts to the same color no matter what Raj does
    if m == 1:
        return "No"
    # If k == 0, Tia cannot repaint any part, so Raj can paint the ribbon in any way he wants
    if k == 0:
        return "Yes"
    # If m >= k + 1, Raj can choose m different colors for the first k + 1 segments
    # This way, Tia cannot repaint k segments to have the same color
    if m >= k + 1:
        return "Yes"
    # Otherwise, if m < k + 1, it's not possible for Raj to prevent Tia from making all parts have the same color
    return "No"

# Example usage:
n, m, k = map(int, input().split())
print(can_paint_ribbon(n, m, k))
