from waitress import serve
from app import app  # assuming your Flask app is defined in app.py

if __name__ == '__main__':
    print("Running Waitress server...")
    serve(app, host='0.0.0.0', port=8080)
