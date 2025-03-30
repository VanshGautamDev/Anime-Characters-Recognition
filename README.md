# Anime-Characters-Recognition
This project is a Flask-based web application that allows users to upload an image of an anime character and recognize it using the SauceNAO API.

🚀 Features

Upload an image to recognize the anime character.
Uses SauceNAO API for character identification.
Flask-based backend for handling requests.
Simple, user-friendly web interface.

🛠 Setup & Installation

Prerequisites
Python 3.x
Flask
Requests
An active SauceNAO API Key (Get one from SauceNAO)

Installation Steps
Clone the Repository
git clone https://github.com/yourusername/anime-recognition.git
cd anime-recognition
Create a Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Set Up Environment Variables
Create a .env file and add your SauceNAO API Key:
SAUCENAO_API_KEY=your_api_key_here

🚀 Running the Project
Start the Flask application:
python script.py
Open your browser and go to:
http://127.0.0.1:5000

📌 API Usage
Endpoint: /upload
Method: POST
Request: Image file upload
Response: JSON containing recognized anime character details

🤖 Tech Stack
Backend: Flask, Python
Frontend: HTML, CSS, JavaScript
API: SauceNAO
📜 License
This project is licensed under the MIT License.
📞 Contact
For any queries or contributions, reach out via vanshgautam29045@gmail.com or open an issue in the GitHub repository.
💡 Star the repository if you found it useful! ⭐
