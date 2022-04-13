import numpy as np
from PIL import Image


def rgb2gray(rgb: np.array) -> np.array:
    
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    return 0.2989 * r + 0.5870 * g + 0.1140 * b


def gray2binary(gray: np.array) -> np.array:
    
    return (127 < gray) & (gray <= 255)


def erosion(image: np.array, kernel: np.array) -> np.array:
    
    output = np.zeros_like(image)
    image_padded = np.zeros(
        (image.shape[0] + kernel.shape[0] - 1, image.shape[1] + kernel.shape[1] - 1)
    )

    
    image_padded[kernel.shape[0] - 2 : -1 :, kernel.shape[1] - 2 : -1 :] = image

    
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            summation = (
                kernel * image_padded[y : y + kernel.shape[0], x : x + kernel.shape[1]]
            ).sum()
            output[y, x] = int(summation == 5)
    return output



structuring_element = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])

if __name__ == "__main__":
    
    image = np.array(Image.open(r"..\image_data\lena.jpg"))
    
    output = erosion(gray2binary(rgb2gray(image)), structuring_element)
    
    pil_img = Image.fromarray(output).convert("RGB")
    pil_img.save("result_erosion.png")
