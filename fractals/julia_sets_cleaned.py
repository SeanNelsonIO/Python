

import warnings
from typing import Any, Callable

import numpy
from matplotlib import pyplot

c_cauliflower = 0.25 + 0.0j
c_polynomial_1 = -0.4 + 0.6j
c_polynomial_2 = -0.1 + 0.651j
c_exponential = -2.0
nb_iterations = 56
window_size = 2.0
nb_pixels = 666


def eval_exponential(c_parameter: complex, z_values: numpy.ndarray) -> numpy.ndarray:
    
    return numpy.exp(z_values) + c_parameter


def eval_quadratic_polynomial(
    c_parameter: complex, z_values: numpy.ndarray
) -> numpy.ndarray:
    
    return z_values * z_values + c_parameter


def prepare_grid(window_size: float, nb_pixels: int) -> numpy.ndarray:
    
    x = numpy.linspace(-window_size, window_size, nb_pixels)
    x = x.reshape((nb_pixels, 1))
    y = numpy.linspace(-window_size, window_size, nb_pixels)
    y = y.reshape((1, nb_pixels))
    return x + 1.0j * y


def iterate_function(
    eval_function: Callable[[Any, numpy.ndarray], numpy.ndarray],
    function_params: Any,
    nb_iterations: int,
    z_0: numpy.ndarray,
    infinity: float = None,
) -> numpy.ndarray:
    

    z_n = z_0.astype("complex64")
    for i in range(nb_iterations):
        z_n = eval_function(function_params, z_n)
        if infinity is not None:
            numpy.nan_to_num(z_n, copy=False, nan=infinity)
            z_n[abs(z_n) == numpy.inf] = infinity
    return z_n


def show_results(
    function_label: str,
    function_params: Any,
    escape_radius: float,
    z_final: numpy.ndarray,
) -> None:
    

    abs_z_final = (abs(z_final)).transpose()
    abs_z_final[:, :] = abs_z_final[::-1, :]
    pyplot.matshow(abs_z_final < escape_radius)
    pyplot.title(f"Julia set of ${function_label}$, $c={function_params}$")
    pyplot.show()


def ignore_overflow_warnings() -> None:
    
    warnings.filterwarnings(
        "ignore", category=RuntimeWarning, message="overflow encountered in multiply"
    )
    warnings.filterwarnings(
        "ignore",
        category=RuntimeWarning,
        message="invalid value encountered in multiply",
    )
    warnings.filterwarnings(
        "ignore", category=RuntimeWarning, message="overflow encountered in absolute"
    )
    warnings.filterwarnings(
        "ignore", category=RuntimeWarning, message="overflow encountered in exp"
    )


if __name__ == "__main__":

    z_0 = prepare_grid(window_size, nb_pixels)

    ignore_overflow_warnings()  

    nb_iterations = 24
    escape_radius = 2 * abs(c_cauliflower) + 1
    z_final = iterate_function(
        eval_quadratic_polynomial,
        c_cauliflower,
        nb_iterations,
        z_0,
        infinity=1.1 * escape_radius,
    )
    show_results("z^2+c", c_cauliflower, escape_radius, z_final)

    nb_iterations = 64
    escape_radius = 2 * abs(c_polynomial_1) + 1
    z_final = iterate_function(
        eval_quadratic_polynomial,
        c_polynomial_1,
        nb_iterations,
        z_0,
        infinity=1.1 * escape_radius,
    )
    show_results("z^2+c", c_polynomial_1, escape_radius, z_final)

    nb_iterations = 161
    escape_radius = 2 * abs(c_polynomial_2) + 1
    z_final = iterate_function(
        eval_quadratic_polynomial,
        c_polynomial_2,
        nb_iterations,
        z_0,
        infinity=1.1 * escape_radius,
    )
    show_results("z^2+c", c_polynomial_2, escape_radius, z_final)

    nb_iterations = 12
    escape_radius = 10000.0
    z_final = iterate_function(
        eval_exponential,
        c_exponential,
        nb_iterations,
        z_0 + 2,
        infinity=1.0e10,
    )
    show_results("e^z+c", c_exponential, escape_radius, z_final)
