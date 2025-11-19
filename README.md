# Fibonacci Spiral Project
This simple Python project prints Fibonacci numbers and draws a spiral on a graph.

## What it does
- Prints the first _N_ Fibonacci numbers to the terminal.
- Plots a **golden spiral** (a logarithmic spiral that grows by the golden ratio every 90°).
- Optionally overlays the first _N_ **Fibonacci squares** and quarter-circle arcs to visualize the classic Fibonacci tiling.
- Saves the spiral image to `output/spiral.png`.

## Quick start 
1. **Unzip** this project.
2. Open the folder in **VS Code**.
3. Press `Ctrl+Shift+P` → “**Terminal: Create New Integrated Terminal**” (PowerShell).
4. Run:
   ```powershell
   .\run.ps1
   ```
   (If you see an execution policy warning, you can run this once: 
   `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` and then run `.
un.ps1` again.)

The script will create a virtual environment, install dependencies, and run the app.

## Manual run (optional)
```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py -n 20 --turns 10 --save
```

## CLI Options
- `-n, --numbers` : How many Fibonacci numbers to generate (default: 20).
- `--turns`       : How many quarter-turns of the spiral to draw (default: 12).
- `--squares`     : Overlay Fibonacci squares and arcs (off by default).
- `--save`        : Save figure to `output/spiral.png` in addition to showing it.
- `--no-show`     : Don’t pop up a window (useful on headless systems).

## Files
- `main.py`           – Entry point (parses args, prints sequence, draws spiral).
- `fib.py`            – Fibonacci sequence helpers.
- `plot_spiral.py`    – Plotting utilities (golden spiral + optional squares/arcs).
- `requirements.txt`  – Dependencies (matplotlib).
- `run.ps1`           – PowerShell helper to set up venv and run the app.
