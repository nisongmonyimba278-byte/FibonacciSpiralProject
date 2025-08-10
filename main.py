"""
main.py — Entry point
"""
import argparse
from fib import fib_sequence
from plot_spiral import plot_spiral

def main():
    parser = argparse.ArgumentParser(description="Print Fibonacci numbers and draw a spiral.")
    parser.add_argument("-n", "--numbers", type=int, default=20, help="How many Fibonacci numbers to print (default: 20)")
    parser.add_argument("--turns", type=int, default=12, help="Quarter-turns of the spiral to draw (default: 12)")
    parser.add_argument("--squares", action="store_true", help="Overlay Fibonacci squares & quarter-circle arcs")
    parser.add_argument("--save", action="store_true", help="Save the figure to output/spiral.png")
    parser.add_argument("--no-show", action="store_true", help="Do not show a window for the figure")
    args = parser.parse_args()

    n = max(1, args.numbers)
    seq = fib_sequence(n)
    print("Fibonacci sequence (first {}):".format(n))
    print(", ".join(map(str, seq)))

    save_path = "output/spiral.png" if args.save else None
    plot_spiral(n_numbers=n, quarter_turns=max(1, args.turns), show_squares=args.squares, save_path=save_path, show=not args.no_show)

if __name__ == "__main__":
    main()
