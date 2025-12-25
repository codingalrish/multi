# Use a lightweight Python base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application logic
COPY app.py .

# Run the application
EXPOSE 80
CMD ["python", "app.py"]
