"""
plot_spiral.py — Draw a golden spiral and optional Fibonacci tiling.
"""
import math
from typing import List, Tuple, Optional
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc

GOLDEN_RATIO = (1 + 5 ** 0.5) / 2  # φ

def _golden_spiral_points(a: float, quarter_turns: int, points_per_quarter: int = 200):
    """
    Generate x,y points for a golden spiral r = a * φ^(θ/(π/2)).
    quarter_turns: number of 90-degree segments to draw (e.g., 12 = 3 full turns).
    """
    total_points = quarter_turns * points_per_quarter + 1
    thetas = [i * (math.pi / 2) / points_per_quarter for i in range(total_points)]
    xs, ys = [], []
    for theta in thetas:
        r = a * (GOLDEN_RATIO ** (theta / (math.pi / 2)))  # grows by φ every 90°
        xs.append(r * math.cos(theta))
        ys.append(r * math.sin(theta))
    return xs, ys

def _place_fib_squares(sizes: List[int]) -> List[Tuple[float, float, int]]:
    """
    Compute lower-left positions (x,y) for Fibonacci squares placed in the classic tiling.
    Returns a list of tuples (x, y, size) for each square, in order.
    Algorithm:
      - Start with two 1x1 squares side-by-side.
      - Then add squares around the growing rectangle in this repeating order:
        above, left, below, right.
    """
    if not sizes:
        return []
    if len(sizes) == 1:
        return [(0.0, 0.0, sizes[0])]

    # Place the first two: second immediately to the right of the first
    positions = [(0.0, 0.0, sizes[0])]
    x0, y0, s0 = positions[0]
    positions.append((x0 + s0, y0, sizes[1]))

    # Current bounding box of the rectangle containing all placed squares
    xmin, ymin = 0.0, 0.0
    width = sizes[0] + sizes[1]
    height = max(sizes[0], sizes[1])  # which is 1 initially

    # For the rest, cycle through: above, left, below, right
    for i in range(2, len(sizes)):
        s = sizes[i]
        orient = (i - 2) % 4
        if orient == 0:  # above
            positions.append((xmin, ymin + height, s))
            height += s
        elif orient == 1:  # left
            positions.append((xmin - s, ymin, s))
            xmin -= s
            width += s
        elif orient == 2:  # below
            positions.append((xmin, ymin - s, s))
            ymin -= s
            height += s
        else:  # right
            positions.append((xmin + width, ymin, s))
            width += s
    return positions

def _add_quarter_arc(ax, x, y, s, orient_index: int):
    """
    Add a quarter-circle arc inside a square of side s located at (x,y) (lower-left).
    The arc approximates the Fibonacci spiral path through each square.
    `orient_index` follows the same sequence used when placing squares:
      0: above, 1: left, 2: below, 3: right
    """
    # For each orientation, arc center is at the corner joining prior squares,
    # and angles sweep 90 degrees to follow the spiral continuously.
    if orient_index == 0:  # above: arc centered at (x + s, y + s), from 180° to 270°
        center = (x + s, y + s); theta1, theta2 = 180, 270
    elif orient_index == 1:  # left: center at (x, y + s), from 270° to 0°
        center = (x, y + s); theta1, theta2 = 270, 360
    elif orient_index == 2:  # below: center at (x, y), from 0° to 90°
        center = (x, y); theta1, theta2 = 0, 90
    else:  # right: center at (x + s, y), from 90° to 180°
        center = (x + s, y); theta1, theta2 = 90, 180

    arc = Arc(center, width=2*s, height=2*s, angle=0, theta1=theta1, theta2=theta2, linewidth=1.6)
    ax.add_patch(arc)

def plot_spiral(n_numbers: int = 20, quarter_turns: int = 12, show_squares: bool = False, save_path: Optional[str] = None, show: bool = True):
    """
    Draw the golden spiral and optionally overlay Fibonacci squares + arcs.
    """
    import matplotlib.pyplot as plt  # ensure backend picked after potential import

    # Spiral curve
    a = 0.2  # starting radius; adjust to taste
    xs, ys = _golden_spiral_points(a=a, quarter_turns=quarter_turns)

    fig, ax = plt.subplots(figsize=(8,8))
    ax.plot(xs, ys, linewidth=2)

    if show_squares:
        # Compute Fibonacci sizes for the overlay, but keep it modest to avoid huge squares
        sizes = [1, 1]
        while len(sizes) < max(3, min(n_numbers, 10)):  # cap squares overlay to 10 for clarity
            sizes.append(sizes[-1] + sizes[-2])
        squares = _place_fib_squares(sizes)

        # Draw squares and arcs
        for idx, (x, y, s) in enumerate(squares):
            rect = Rectangle((x, y), s, s, fill=False, linewidth=1.0)
            ax.add_patch(rect)
            if idx >= 2:
                _add_quarter_arc(ax, x, y, s, orient_index=(idx - 2) % 4)

        # Expand view to include all squares
        xsq = [x for x,_,s in squares] + [x+s for x,_,s in squares]
        ysq = [y for _,y,s in squares] + [y+s for _,y,s in squares]
        pad = 0.5
        ax.set_xlim(min(xsq)-pad, max(xsq)+pad)
        ax.set_ylim(min(ysq)-pad, max(ysq)+pad)
    else:
        # Fit the spiral nicely
        ax.axis('equal')
        ax.margins(0.1)

    ax.set_title("Fibonacci / Golden Spiral")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.5)

    if save_path:
        fig.savefig(save_path, dpi=160, bbox_inches="tight")
    if show:
        plt.show()
    else:
        plt.close(fig)
