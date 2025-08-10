# run.ps1 — Set up a venv, install deps, and run the app.
$ErrorActionPreference = "Stop"

# Go to the directory where this script lives
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

# Create venv if it doesn't exist
if (!(Test-Path ".\.venv")) {
    Write-Host "Creating virtual environment (.venv)..."
    python -m venv .venv
}

# Activate venv
Write-Host "Activating virtual environment..."
. ".\.venv\Scripts\Activate.ps1"

# Upgrade pip and install requirements
Write-Host "Upgrading pip and installing requirements..."
python -m pip install --upgrade pip
pip install -r requirements.txt

# Run the app with some sensible defaults
Write-Host "Running the app..."
python main.py -n 20 --turns 12 --squares --save
Write-Host "Done! Image saved to output\spiral.png"
