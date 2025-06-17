import os
import subprocess

# Check if model.pkl exists, if not, run main.py to create it
if not os.path.exists('model.pkl'):
    print("Model file not found. Training model...")
    subprocess.run(['python', 'main.py'])
    print("Model training complete.")

# Run the FastAPI server
print("Starting API server...")
subprocess.run(['uvicorn', 'server:app', '--host', '0.0.0.0', '--port', '8888'])
