# Use a lightweight Python 3.13 image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your entire project code into the container
COPY . .

# Command to run tests (results will be mapped to your host machine later)
CMD ["pytest", "-n", "3", "--alluredir=allure-results", "--clean-alluredir", "-v"]