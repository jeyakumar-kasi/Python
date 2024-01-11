# Pull the lastest Image
FROM python:3.12.0-alpine

# Set Environment Vars
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set Working Dir
WORKDIR /myproject

# Copy project dir
COPY ./ ./

# Install dependencies
RUN pip install -r requirements.txt



