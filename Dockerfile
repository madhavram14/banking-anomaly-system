# We use the official Playwright image because it comes with 
# all browser dependencies (Chromium, Firefox) pre-installed.
FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

WORKDIR /app

# Copy and install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your Banking Sentinel code
COPY . .

# Run your Pytest suite by default
CMD ["pytest"]