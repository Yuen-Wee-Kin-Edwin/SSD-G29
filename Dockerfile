# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirement and source files.
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set environment variable for Flask.
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run"]