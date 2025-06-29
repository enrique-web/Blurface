# Blurface

A simple Python utility for applying blur effects to images using Pillow (PIL).

## Description

Blurface uses the Pillow library to apply simple blur and Gaussian blur effects to images. It is designed to provide an easy way to soften images, create artistic effects, or anonymize sensitive information such as faces.

## Features

- Apply simple blur to images
- Apply Gaussian blur with customizable radius
- Easy to use with minimal code
- Supports common image formats (JPEG, PNG, etc.)

## Installation

Make sure you have Python 3 installed.

Install Pillow:

```
pip install pillow
```

Clone the repository:

```
git clone https://github.com/enrique-web/Blurface.git
cd Blurface
```

## Usage

Example code to apply blur effects:

```
from PIL import Image, ImageFilter

def apply_simple_blur(input_path, output_path):
    image = Image.open(input_path)
    blurred = image.filter(ImageFilter.BLUR)
    blurred.save(output_path)
    print(f"Saved simple blurred image to {output_path}")

def apply_gaussian_blur(input_path, output_path, radius=5):
    image = Image.open(input_path)
    blurred = image.filter(ImageFilter.GaussianBlur(radius=radius))
    blurred.save(output_path)
    print(f"Saved gaussian blurred image to {output_path}")

if __name__ == "__main__":
    input_image = "input.jpg"
    apply_simple_blur(input_image, "simple_blur.jpg")
    apply_gaussian_blur(input_image, "gaussian_blur.jpg", radius=10)
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
