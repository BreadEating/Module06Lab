FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY train.py evaluate.py check_performance.py ./

# Create artifacts directory
RUN mkdir -p artifacts

# Copy model artifacts (will be available after CI pipeline runs)
COPY artifacts/ artifacts/

# Set environment variable to ensure Python output is not buffered
ENV PYTHONUNBUFFERED=1

# Default command - run evaluation to show model performance
CMD ["python", "evaluate.py"]