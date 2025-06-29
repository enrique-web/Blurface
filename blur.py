from PIL import Image, ImageFilter

def blur_image(input_path: str, output_path: str, blur_type='simple', radius=2):
    """
    Apply blur effect to an image and save the result.

    Parameters:
    - input_path: str, path to input image file.
    - output_path: str, path to save blurred image.
    - blur_type: str, 'simple' for basic blur, 'gaussian' for Gaussian blur.
    - radius: int or float, blur radius (only for Gaussian blur).
    """
    image = Image.open(input_path)

    if blur_type == 'simple':
        blurred = image.filter(ImageFilter.BLUR)
    elif blur_type == 'gaussian':
        blurred = image.filter(ImageFilter.GaussianBlur(radius=radius))
    else:
        raise ValueError("blur_type must be 'simple' or 'gaussian'")

    blurred.save(output_path)
    print(f"Blurred image saved to {output_path}")

# Example usage
if __name__ == "__main__":
    blur_image("input.jpg", "blurred_simple.jpg", blur_type='simple')
    blur_image("input.jpg", "blurred_gaussian.jpg", blur_type='gaussian', radius=5)
