"""
This file is the entry point for the application in production.
"""
from app.main import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
