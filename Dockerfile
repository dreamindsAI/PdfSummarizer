# Set base image
FROM python:3.10

# Set working dir
WORKDIR /app/

# Copy and install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

# Expose port
EXPOSE 8000

# Entry point
CMD [ "python3","main.py"]