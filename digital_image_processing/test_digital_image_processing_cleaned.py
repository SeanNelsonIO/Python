
from cv2 import COLOR_BGR2GRAY, cvtColor, imread
from numpy import array, uint8
from PIL import Image

from digital_image_processing import change_contrast as cc
from digital_image_processing import convert_to_negative as cn
from digital_image_processing import sepia as sp
from digital_image_processing.dithering import burkes as bs
from digital_image_processing.edge_detection import canny as canny
from digital_image_processing.filters import convolve as conv
from digital_image_processing.filters import gaussian_filter as gg
from digital_image_processing.filters import median_filter as med
from digital_image_processing.filters import sobel_filter as sob
from digital_image_processing.resize import resize as rs

img = imread(r"digital_image_processing/image_data/lena_small.jpg")
gray = cvtColor(img, COLOR_BGR2GRAY)



def test_convert_to_negative():
    negative_img = cn.convert_to_negative(img)
    
    assert negative_img.any()



def test_change_contrast():
    with Image.open("digital_image_processing/image_data/lena_small.jpg") as img:
        
        assert str(cc.change_contrast(img, 110)).startswith(
            "<PIL.Image.Image image mode=RGB size=100x100 at"
        )



def test_gen_gaussian_kernel():
    resp = canny.gen_gaussian_kernel(9, sigma=1.4)
    
    assert resp.all()



def test_canny():
    canny_img = imread("digital_image_processing/image_data/lena_small.jpg", 0)
    
    assert canny_img.all()
    canny_array = canny.canny(canny_img)
    
    assert canny_array.any()



def test_gen_gaussian_kernel_filter():
    assert gg.gaussian_filter(gray, 5, sigma=0.9).all()


def test_convolve_filter():
    
    Laplace = array([[0.25, 0.5, 0.25], [0.5, -3, 0.5], [0.25, 0.5, 0.25]])
    res = conv.img_convolve(gray, Laplace).astype(uint8)
    assert res.any()


def test_median_filter():
    assert med.median_filter(gray, 3).any()


def test_sobel_filter():
    grad, theta = sob.sobel_filter(gray)
    assert grad.any() and theta.any()


def test_sepia():
    sepia = sp.make_sepia(img, 20)
    assert sepia.all()


def test_burkes(file_path: str = "digital_image_processing/image_data/lena_small.jpg"):
    burkes = bs.Burkes(imread(file_path, 1), 120)
    burkes.process()
    assert burkes.output_img.any()


def test_nearest_neighbour(
    file_path: str = "digital_image_processing/image_data/lena_small.jpg",
):
    nn = rs.NearestNeighbour(imread(file_path, 1), 400, 200)
    nn.process()
    assert nn.output.any()
