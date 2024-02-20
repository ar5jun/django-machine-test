# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /books_management

# Copy the current directory contents into the container at /app
COPY . /books_management

ENV PYTHONUNBUFFERED=1

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir Django \
django-rest-auth==0.9.5 \
djangorestframework==3.14.0 \
djangorestframework-simplejwt==5.3.1 \
requests

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
