from flask import Flask, request, jsonify, render_template
import os
import requests

# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# SauceNAO API Configuration
SAUCENAO_API_KEY = "4a6cf58f0875b8f43f4ccf1a31364453f50735c6"  # Replace with your actual SauceNAO API key
SAUCENAO_URL = "https://saucenao.com/search.php"

@app.route("/")
def home():
    return render_template("place.html")

@app.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Save file
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    # Send image to SauceNAO API
    with open(file_path, "rb") as img_file:
        files = {"file": img_file}
        params = {"api_key": SAUCENAO_API_KEY, "output_type": 2}
        response = requests.post(SAUCENAO_URL, params=params, files=files)

    # Parse response
    try:
        result = response.json()
        if "results" in result and len(result["results"]) > 0:
            first_result = result["results"][0]["data"]
            recognized_text = first_result.get("title", "Unknown Anime Character")
            anime_name = first_result.get("source", "Unknown Anime")
            similarity = first_result.get("similarity", "0%")
        else:
            recognized_text = "Could not recognize the anime character."
            anime_name = "N/A"
            similarity = "0%"

    except Exception as e:
        return jsonify({"error": f"API Error: {str(e)}"}), 500

    return jsonify({
        "message": "File uploaded successfully",
        "character": recognized_text,
        "anime": anime_name,
        "similarity": similarity
    })

if __name__ == "__main__":
    app.run(debug=True)
