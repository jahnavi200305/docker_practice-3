# Use official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Command to run the Flask app
CMD ["python", "app.py"]
