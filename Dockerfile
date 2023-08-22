# Use the official Python 3.9 slim-buster image as the base image
FROM python:3.9-slim-buster
# Copy the contents of the current directory into the /app directory in the image
COPY . /app
# Set the working directory to /app
WORKDIR /app
# Update the package list and install the AWS Command Line Interface (CLI)
RUN apt update -y && apt install awscli -y
# Update the package list and install Python package requirements from requirements.txt
RUN apt-get update && pip install -r requirements.txt
# Define the default command to run when the container is started
CMD ["python", "Step-counter/Step_counting_algorithm.ipynb"]