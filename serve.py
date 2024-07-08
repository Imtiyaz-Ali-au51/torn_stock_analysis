from waitress import serve
import app  # assuming your Flask app is defined in app.py

print("Starting the Waitress server...")

try:
    serve(app.app, host='0.0.0.0', port=8080)
    print("Waitress server started on port 8080...")
except Exception as e:
    print(f"An error occurred: {e}")
