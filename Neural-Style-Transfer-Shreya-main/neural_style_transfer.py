
import matplotlib.pyplot as plt
import numpy as np
from API import transfer_style

def neural_style_transfer(content_path, style_path, output_path, model_path='model'):
    print("Running neural style transfer...")
    stylized_image = transfer_style(content_path, style_path, model_path)
    stylized_image = np.clip(stylized_image, 0, 1)  # Clip image values to valid range
    plt.imsave(output_path, stylized_image)
    return output_path
