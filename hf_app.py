import os
import uuid
import gradio as gr
from PIL import Image
from neural_style_transfer import neural_style_transfer

os.makedirs("static", exist_ok=True)

def run_style_transfer(content_image, style_image):
    if content_image is None or style_image is None:
        raise gr.Error("Please upload both a content image and a style image.")

    content_path = os.path.join("static", f"content_{uuid.uuid4().hex}.jpg")
    style_path = os.path.join("static", f"style_{uuid.uuid4().hex}.jpg")
    output_path = os.path.join("static", f"output_{uuid.uuid4().hex}.jpg")

    Image.fromarray(content_image).save(content_path)
    Image.fromarray(style_image).save(style_path)


    result_path = neural_style_transfer(content_path, style_path)

    
    final_path = result_path if isinstance(result_path, str) and os.path.exists(result_path) else output_path

    if not os.path.exists(final_path):
        raise gr.Error("Stylized image was not generated. Check your backend function return value.")

    return final_path

demo = gr.Interface(
    fn=run_style_transfer,
    inputs=[
        gr.Image(type="numpy", label="Content Image"),
        gr.Image(type="numpy", label="Style Image"),
    ],
    outputs=gr.Image(type="filepath", label="Stylized Output"),
    title="Neural Style Transfer",
    description="Upload a content image and a style image to generate a stylized output."
)

if __name__ == "__main__":
    demo.launch()
