
from flask import Flask, request, jsonify, send_from_directory
import os
import uuid
import base64
from PIL import Image
from io import BytesIO
from neural_style_transfer import neural_style_transfer

app = Flask(__name__)

from flask import render_template  # Add at top if not already

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/process_images', methods=['POST'])
def process_images():
    data = request.get_json()
    content_data = data['contentImageData']
    style_data = data['styleImageData']

    # Save images from base64
    content_path = "content.jpg"
    style_path = "style.jpg"

    content_image = Image.open(BytesIO(base64.b64decode(content_data.split(",")[1])))
    style_image = Image.open(BytesIO(base64.b64decode(style_data.split(",")[1])))

    content_image.save(content_path)
    style_image.save(style_path)

    # Ensure static folder exists
    if not os.path.exists("static"):
        os.makedirs("static")

    output_filename = f"output_{uuid.uuid4().hex}.jpg"
    output_path = os.path.join("static", output_filename)

    # Perform style transfer
    neural_style_transfer(content_path, style_path, output_path)

    return jsonify({"imageUrl": "/" + output_path})

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
