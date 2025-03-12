# Use an official Python image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy app files
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
# Set environment variables (correct format)
ENV NAME=flask_api
ENV DB_HOST=flaskapi_postgresql
ENV DB_NAME=flaskapi_db
ENV DB_USER=admin
ENV DB_PASS=Express1234%


# Run Flask app
CMD ["python", "app.py"]
