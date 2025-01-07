from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Ensure the uploads folder exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Save the file to the uploads folder
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Process the file and return fake results for testing
    # Replace this with your face shape processing logic
    results = {
        "oval": 80,
        "round": 60,
        "square": 40,
        "diamond": 70,
        "rectangular": 50,
        "oblong": 30,
        "heart": 20
    }

    # Format results as percentage bars
    percentage_bars = {
        shape: f"{percentage}% match"
        for shape, percentage in results.items()
    }

    return jsonify({"results": percentage_bars})

if __name__ == '__main__':
    app.run(debug=True)
