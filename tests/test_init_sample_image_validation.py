import cv2
import pytest

sample_image_path = r"data/image-samples/985_data.jpg"

def test_sample_image_validation():
    img = cv2.imread(sample_image_path)
    assert len(img.shape) == 3 # checks if the image has 3 channels