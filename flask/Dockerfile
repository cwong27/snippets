FROM python:3.14.0a2-slim-bullseye

# Set the working directory within the container
WORKDIR /vuln_webapp

# Copy the necessary files and directories into the container
COPY vuln_webapp/ vuln_webapp/
COPY vuln_webapp/templates /vuln_webapp/templates/
COPY vuln_webapp/static /vuln_webapp/static/

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r ./vuln_webapp/requirements.txt

# Expose port 5000 for the Flask application
EXPOSE 5000

CMD ["flask", "--app", "vuln_webapp", "run", "-h", "0.0.0.0", "-p", "5000"]

