from PIL import Image
import os

def resize_image(image, max_size=(800, 800)):
    img = Image.open(image)

    # Resize the image while maintaining the aspect ratio
    img.thumbnail(max_size)

    # Save the resized image back to the same path
    img.save(image.path)