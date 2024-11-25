FROM python:3.14.0a2-slim-bullseye

# Set the working directory within the container
WORKDIR /demo_webapp

# Copy the necessary files and directories into the container
COPY demo_webapp/ demo_webapp/
COPY demo_webapp/templates /demo_webapp/templates/
COPY demo_webapp/static /demo_webapp/static/

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r ./demo_webapp/requirements.txt

# Expose port 5000 for the Flask application
EXPOSE 5000

CMD ["flask", "--app", "demo_webapp", "run", "-h", "0.0.0.0", "-p", "5000"]

