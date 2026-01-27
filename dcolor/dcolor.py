"""
dcolor.dcolor

Module providing main domain coloring functionality.
"""
from typing import Callable, Optional, Tuple
from typing_extensions import TypeAliasType

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import numpy as np
import numpy.typing as npt

import dcolor.color_maps as color_maps

ComplexFunction = TypeAliasType(
    "ComplexFunction",
    Callable[[npt.NDArray[np.complexfloating]], npt.NDArray[np.complexfloating]],
)


def _make_domain(
    xmin: float, xmax: float, ymin: float, ymax: float, samples: int
) -> color_maps.ComplexPlane:
    """Create the domains for Real (x) and Imaginary (y) values respectively"""
    x = np.linspace(xmin, xmax, samples)
    y = np.linspace(ymin, ymax, samples)
    xx, yy = np.meshgrid(x, y)
    return xx + 1j * yy


class DColor:
    """
    A wrapper object around a complex function for plotting using matplotlib.

    `f` --      The complex-valued function to plot. A callable which accepts numpy array of complex values.

    Optional keyword arguments:
    `cmap` --       A function which converts a complex number to an RGB color
                    (or an array of the former to an array of the latter).
                    The default is `dcolor.cmap.magnitude_oscillating`

    `samples` --    The number of samples along each axis to use for plotting.
                    The square of this value is how many values are actually calculated.
    """

    def __init__(
        self,
        f: ComplexFunction,
        *,
        cmap: color_maps.ComplexColorMap = color_maps.magnitude_oscillating,
        samples=1000,
    ):
        self._function = f
        self._samples = samples
        # Extra
        self._cmap = cmap

        self._need_redraw = False
        self.axes: Optional[Axes] = None

    def _set_need_redraw(self):
        """Set that the axes need to redraw. Used as a callback for mouse releases."""
        self._need_redraw = True

    def _plot(self, clear: bool = False):
        """
        Replot the contained function with the current axes limits.
        Intended to be used as a callback after axes bounds change.
        """
        if self.axes is None:
            return

        if clear:
            for image in self.axes.images:
                image.remove()

        xmin, xmax = self.axes.get_xlim()
        ymin, ymax = self.axes.get_ylim()

        # Call, color, and plot the image on the current axes limits
        zz = self._function(_make_domain(xmin, xmax, ymin, ymax, self._samples))
        rgb = self._cmap(zz)
        self.axes.imshow(rgb, origin="lower", extent=(xmin, xmax, ymin, ymax))

    def plot(
        self,
        axes: Optional[Axes] = None,
        xlim: Optional[Tuple[float, float]] = None,
        ylim: Optional[Tuple[float, float]] = None,
        grid: bool = True,
        show: bool = True,
    ):
        """
        Plot the contained function on the given boundaries, add axis labels, and add gridlines.
        """
        if axes is None:
            self.axes = plt.gca()
            axes = self.axes
        else:
            self.axes = axes

        if xlim is not None:
            axes.set_xlim(xlim)
        if ylim is not None:
            axes.set_ylim(ylim)

        self._plot()

        axes.set_xlabel("$\\Re$")
        axes.set_ylabel("$\\Im$")
        axes.axhline(y=0, color="k")
        axes.axvline(x=0, color="k")
        if grid:
            axes.grid(True, which="both", linestyle="dashed")

        if show:
            plt.show()


def dcolor(
    f: ComplexFunction,
    *,
    axes: Optional[Axes] = None,
    xlim: Optional[Tuple[float, float]] = None,
    ylim: Optional[Tuple[float, float]] = None,
    cmap: color_maps.ComplexColorMap = color_maps.magnitude_oscillating,
    samples: int = 1000,
    grid: bool = True,
    show: bool = True,
) -> DColor:
    """
    Plot a complex-valued function `f`. By default, this uses the current matplotlib axes.

    Note that the current figure's DPI settings will be used to draw the image.
    If this matters to you, call `Figure.set_dpi` beforehand.

    Arguments:
    `f` --      The complex-valued function to plot. A callable which accepts numpy array of complex values.

    Optional keyword arguments:
    `axes` --       The matplotlib axes on which to plot. Defaults to the current axes.

    `xlim` --       The x (real) limits to use when plotting.
                    If absent, prior values from `xlim()` are respected.

    `ylim` --       The y (imaginary) limits to use when plotting
                    If absent, prior values from `ylim()` are respected.

    `cmap` --       A function which converts a complex number to an RGB color
                    (or an array of the former to an array of the latter).
                    The default is `dcolor.color_maps.magnitude_oscillating`

    `samples` --    The number of samples along each axis to use for plotting.
                    Note that the square of this value is how many values are actually calculated.

    `grid` --       Whether to draw gridlines at the tick positions. Defaults to True.

    `show` --       Whether to show the plot with Matplotlib. Defaults to True.
    """
    ret = DColor(f, cmap=cmap, samples=samples)
    ret.plot(
        axes=axes,
        xlim=xlim,
        ylim=ylim,
        grid=grid,
        show=show,
    )
    return ret
