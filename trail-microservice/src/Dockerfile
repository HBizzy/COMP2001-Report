# Use an appropriate base image
FROM python:3.9-slim

# Set environment variable to accept the EULA for Microsoft packages
ENV ACCEPT_EULA=Y

# Install dependencies
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    curl \
    gcc \
    g++ \
    gnupg \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Add Microsoft repository and install SQL Server ODBC driver and tools
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends msodbcsql17 mssql-tools \
    && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile \
    && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc \
    && apt-get clean

# Set environment variables
ENV PATH="$PATH:/opt/mssql-tools/bin"

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Clean up APT when done
RUN apt-get -y clean

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]