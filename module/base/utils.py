import cv2
import numpy as np
from PIL import Image


def load_image(file, area: tuple[int, int, int, int] = None):
    """
    Load an image like pillow and drop alpha channel.

    Args:
        file (str):
        area (tuple):

    Returns:
        np.ndarray:
    """
    image = Image.open(file)
    if area is not None:
        image = image.crop(area)
    image = np.array(image)
    channel = image.shape[2] if len(image.shape) > 2 else 1
    if channel > 3:
        image = image[:, :, :3].copy()
    return image


def image_size(image):
    """
    Args:
        image (np.ndarray):

    Returns:
        int, int: width, height
    """
    shape = image.shape
    return shape[1], shape[0]


def get_bbox(image, threshold=0):
    """
    A numpy implementation of the getbbox() in pillow.

    Args:
        image (np.ndarray): Screenshot.
        threshold (int): Color <= threshold will be considered black

    Returns:
        tuple: (upper_left_x, upper_left_y, bottom_right_x, bottom_right_y)
    """
    if image_channel(image) == 3:
        image = np.max(image, axis=2)
    x = np.where(np.max(image, axis=0) > threshold)[0]
    y = np.where(np.max(image, axis=1) > threshold)[0]
    return x[0], y[0], x[-1] + 1, y[-1] + 1


def image_channel(image):
    """
    Args:
        image (np.ndarray):

    Returns:
        int: 0 for grayscale, 3 for RGB.
    """
    return image.shape[2] if len(image.shape) == 3 else 0


def crop(image, area, copy):
    x1, y1, x2, y2 = area
    image = image[y1:y2, x1:x2]
    if copy:
        image = image.copy()
    return image


def get_color(image, area):
    """Calculate the average color of a particular area of the image.

    Args:
        image (np.ndarray): Screenshot.
        area (tuple): (upper_left_x, upper_left_y, bottom_right_x, bottom_right_y)

    Returns:
        tuple: (r, g, b)
    """
    temp = crop(image, area, copy=False)
    color = cv2.mean(temp)
    return color[:3]
