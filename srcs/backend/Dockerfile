# Use a lightweight Python image
FROM python:3.10-slim

RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

#RUN mkdir -p /build

# Copy the requirements file into the container
COPY ./tools/ .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt
RUN poetry lock && \
    poetry install --no-root

# Expose port 8888 to match the Flask app's port
EXPOSE 8888

# Set environment variables
ENV FLASK_APP=./build/main.py  

# Run the Flask application
CMD ["flask", "run", "--debug", "--host=0.0.0.0", "--port=8888"]

