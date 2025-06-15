FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY train.py evaluate.py check_performance.py ./
COPY tests/ tests/

# Copy model artifacts
COPY artifacts/ artifacts/

# Default command
CMD ["python", "evaluate.py"]