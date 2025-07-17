

# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy your app code into the container
COPY . .

# Install dependencies (just pytest here)
RUN pip install --no-cache-dir -r requirements.txt

# Default command: run tests
CMD ["pytest", "-v"]

