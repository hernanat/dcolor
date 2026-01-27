"""
dcolor

Package for generating complex plots using [domain coloring](https://en.wikipedia.org/wiki/Domain_coloring).

The main plotting function is `dcolor.dcolor`, with arguments as:

    dcolor.dcolor(
      lambda z : ...,
      xlim=(-8, 8),
      ylim=(-8, 8),
    )

By default, this will automatically show the plot in a matplotlib figure.
For more information, see the documentation for `dcolor.dcolor`
"""
from .dcolor import dcolor, DColor, ComplexFunction
from .color_maps import (
    magnitude_oscillating,
    raw_magnitude_oscillating,
    green_magnitude,
)

__all__ = [
    "dcolor",
    "DColor",
    "ComplexFunction",
    "magnitude_oscillating",
    "raw_magnitude_oscillating",
    "green_magnitude"
]
