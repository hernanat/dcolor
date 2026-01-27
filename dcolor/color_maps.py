"""
dcolor.color_maps

Module providing complex color maps used in domain coloring.
These functions take a 2D array of complex values and convert them to RGB triples.
"""
from typing import Callable, Literal
from typing_extensions import TypeAlias, TypeAliasType

from matplotlib.colors import hsv_to_rgb
import numpy as np
import numpy.typing as npt

__all__ = ["magnitude_oscillating", "raw_magnitude_oscillating", "green_magnitude"]

ComplexPlane = TypeAliasType(
    "ComplexPlane", np.ndarray[Literal[2], np.dtype[np.complexfloating]]
)  # 2D representation of the complex plane
Image = TypeAliasType(
    "Image", np.ndarray[Literal[3], np.dtype[np.floating]]
)  # RGB image
# TODO: if going the Matplotlib-style norm, cmap kwargs, this may need its own class
ComplexColorMap: TypeAlias = Callable[[ComplexPlane], Image]  # C -> [0, 1]^3


def normalize(arr: npt.NDArray) -> npt.NDArray:
    """Used for normalizing data in array based on min/max values"""
    arrMin = np.min(arr)
    arrMax = np.max(arr)
    arr = arr - arrMin
    return arr / (arrMax - arrMin)


def magnitude_oscillating(zz: ComplexPlane) -> Image:
    """
    Converts a complex 2D array `zz` to an RGB image with normal domain coloring.

    Hue is taken from the complex argument of `zz`.
    Saturation and value vary with the logarithm of the magnitude of `zz`,
    giving the appearance of logarithmic countours.
    """
    H = (np.angle(zz) % (2.0 * np.pi)) / (2.0 * np.pi)  # Hue determined by arg(z)
    r = np.log2(1.0 + np.abs(zz))
    S = (1.0 + np.abs(np.sin(2.0 * np.pi * r))) / 2.0
    V = (1.0 + np.abs(np.cos(2.0 * np.pi * r))) / 2.0

    return hsv_to_rgb(np.dstack((H, S, V)))


def raw_magnitude_oscillating(zz: ComplexPlane) -> Image:
    """
    Converts a complex 2D array `zz` to an RGB image.

    Same as `magnitude_oscillating`, but with a "rawer" conversion to RGB,
    rather than going through matplotlib.colors
    """
    h = normalize(np.angle(zz) % (2.0 * np.pi))  # Hue determined by arg(z)
    r = np.log2(1.0 + np.abs(zz))
    s = (1.0 + np.abs(np.sin(2.0 * np.pi * r))) / 2.0
    v = (1.0 + np.abs(np.cos(2.0 * np.pi * r))) / 2.0

    r = np.empty_like(h)
    g = np.empty_like(h)
    b = np.empty_like(h)

    i = (h * 6.0).astype(int)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))

    idx = i % 6 == 0
    r[idx] = v[idx]
    g[idx] = t[idx]
    b[idx] = p[idx]

    idx = i == 1
    r[idx] = q[idx]
    g[idx] = v[idx]
    b[idx] = p[idx]

    idx = i == 2
    r[idx] = p[idx]
    g[idx] = v[idx]
    b[idx] = t[idx]

    idx = i == 3
    r[idx] = p[idx]
    g[idx] = q[idx]
    b[idx] = v[idx]

    idx = i == 4
    r[idx] = t[idx]
    g[idx] = p[idx]
    b[idx] = v[idx]

    idx = i == 5
    r[idx] = v[idx]
    g[idx] = p[idx]
    b[idx] = q[idx]

    idx = s == 0
    r[idx] = v[idx]
    g[idx] = v[idx]
    b[idx] = v[idx]

    return np.stack([r, g, b], axis=-1)


def green_magnitude(zz: ComplexPlane, expand=1.0) -> Image:
    """
    Converts a complex 2D array `zz` to an RGB image.

    Small magnitues are colored black, large ones are white, and values
    between appear green.
    The rate at which this occurs is controlled by `expand`.
    """
    absz = np.abs(zz)
    r = absz * 0.5 / expand
    g = absz * 1.00 / expand
    b = absz * 0.5 / expand
    r = np.clip(r, 0, 1)
    g = np.clip(g, 0, 1)
    b = np.clip(b, 0, 1)
    return np.dstack((r, g, b))
