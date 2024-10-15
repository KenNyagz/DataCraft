# Use an official Python 3.10 image
FROM python:3.10.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Install system dependencies for MySQL and Python
RUN apt-get update && apt-get install -y \
    default-mysql-client \
    libmysqlclient-dev \
    gcc

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Set the working directory to the Django project folder (freelanceCove)
WORKDIR /app/freelanceCove

# Expose the port Django uses
EXPOSE 8000

# Run Django migrations and then start the development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
