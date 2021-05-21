# Inherit from the Python Docker image
FROM python:3.7-slim

# Install the Flask package via pip
RUN pip install flask==1.0.2 flask_mysqldb

# Copy the source code to app folder
COPY * /app/

# Change the working directory
WORKDIR /app/

# Set the command as the script name
CMD ["python", "app.py"]
