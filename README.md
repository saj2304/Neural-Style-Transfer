---
title: Neural Style Transfer
emoji: 🎨
colorFrom: blue
colorTo: purple
sdk: gradio
app_file: hf_app.py
pinned: false
---

# 🎨 Neural Style Transfer

## 📌 Overview
This project implements Neural Style Transfer, a deep learning technique that blends the content of one image with the style of another image using Convolutional Neural Networks (CNNs).

The system takes two inputs:
- 🖼 Content Image
- 🎨 Style Image

and produces a stylized output image.

---

## 🚀 Features
- Apply artistic styles to images
- Real-time / near real-time processing
- Web interface using Flask / Gradio
- Supports multiple styles
- Uses deep learning models

---

## 🛠️ Tech Stack
- Python 🐍
- OpenCV
- TensorFlow
- TensorFlow Hub
- Flask (Backend)
- Gradio (UI for deployment)
- NumPy
- Matplotlib

---

## 📂 Project Structure



```text
Neural-Style-Transfer/
│
├── hf_app.py
├── app.py
├── API.py
├── neural_style_transfer.py
├── templates/
├── static/
├── notebooks/
├── models/
├── requirements.txt
├── README.md

```

---
▶️ How to Run (Local)
1. Clone repository
git clone https://github.com/saj2304/Neural-Style-Transfer.git
2. Install dependencies
pip install -r requirements.txt
3. Run the project
python app.py
4. Open in browser
http://127.0.0.1:5000/
---
🌐 Live Demo

👉 [Will be available after Hugging Face deployment.](https://huggingface.co/spaces/saj2304/neural-style-transfer)

---
📊 Results

Successfully applied artistic styles

Generated high-quality stylized images

Maintained content structure

---
⚠️ Limitations

High computation time

Requires GPU for faster performance

Large model size

---
🔮 Future Improvements

Optimize model for faster performance

Add more artistic styles

Improve UI/UX

Deploy a scalable version

---
👩‍💻 Author

Shreya J

---
GitHub: https://github.com/saj2304

---
⭐ If you like this project, give it a star!

---
