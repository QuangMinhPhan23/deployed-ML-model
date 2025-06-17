FROM python:3.12
LABEL author="Quang Minh"
LABEL description="A machine learning model serving API for personality prediction"

# Set the working directory
WORKDIR /src

# Copy all files needed
COPY main.py /src/main.py
COPY server.py /src/server.py
COPY requirements.txt /src/requirements.txt
COPY run.py /src/run.py
# Try to copy model if it exists, but don't fail if it doesn't
COPY model.pkl* /src/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8888

# Run the application with our wrapper script that ensures model exists
CMD ["python", "run.py"]