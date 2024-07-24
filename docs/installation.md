# Installation Guide for 0-DTE Options Analysis Dashboard

This guide will walk you through the process of setting up the 0-DTE Options Analysis Dashboard on your local machine.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)

## Steps

1. **Clone the repository** (if you haven't already):
   ```
   git clone https://github.com/yourusername/intraday-volatility-model.git
   cd intraday-volatility-model
   ```
   If you don't have Git, you can download the project as a ZIP file and extract it.

2. **Create a virtual environment** (recommended):
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

5. **Verify the installation**:
   ```
   python main.py
   ```
   This should start the Dash server. You should see output indicating that the server is running, typically on `http://127.0.0.1:8050/`.

6. **Access the dashboard**:
   Open a web browser and go to the URL indicated in the console output (typically `http://127.0.0.1:8050/`).

## Troubleshooting

- If you encounter any package-related errors, ensure that you're using the correct version of Python and that all packages in `requirements.txt` are installed correctly.
- If the server fails to start due to a port conflict, you can specify a different port in `main.py`.

## Updating

To update the dashboard to the latest version:

1. Pull the latest changes (if using Git):
   ```
   git pull origin main
   ```

2. Reinstall the requirements in case there are new dependencies:
   ```
   pip install -r requirements.txt
   ```

For any issues or feature requests, please open an issue on the GitHub repository.