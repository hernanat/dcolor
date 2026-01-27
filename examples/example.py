#!/usr/bin/env python3
"""
Plot a selection of functions to see what they look like under various plotting schemes.
"""

import argparse
from dataclasses import dataclass
from pprint import pprint
import sys
from typing import List, Optional

import matplotlib.pyplot as plt
import numpy as np
import dcolor
import dcolor.color_maps as cmaps

FILE_DPI = 1000


@dataclass
class DomainPlot:
    function: dcolor.ComplexFunction
    title: str


@dataclass
class DomainPlotGroup:
    plots: List[DomainPlot]
    name: str


LINEAR_PLOTS = DomainPlotGroup(
    plots=[
        DomainPlot(function=lambda z: z, title="$f(z) = z$"),
        DomainPlot(function=lambda z: z + 4, title="$f(z) = z + 4$"),
        DomainPlot(function=lambda z: z - 4, title="$f(z) = z - 4$"),
        DomainPlot(function=lambda z: z + 4j, title="$f(z) = z + 4j$"),
        DomainPlot(function=lambda z: z - 4j, title="$f(z) = z - 4j$"),
    ],
    name="linear",
)

POLYNOMIAL_PLOTS = DomainPlotGroup(
    plots=[
        DomainPlot(function=lambda z: z**3 - 1, title="$f(z) = z^3 - 1$"),
        DomainPlot(function=lambda z: z**2 + 4 + 4j, title="$f(z) = z^2 + 4 + 4j$"),
        DomainPlot(function=lambda z: z**8 + 4 + 4j, title="$f(z) = z^8 + 4 + 4j$"),
        DomainPlot(function=lambda z: z**16 + 4 + 4j, title="$f(z) = z^16 + 4 + 4j$"),
    ],
    name="polynomial",
)

ALGEBRAIC_PLOTS = DomainPlotGroup(
    plots=[
        DomainPlot(function=lambda z: 1 / z, title="$f(z) = \\frac{1}{z}$"),
        DomainPlot(
            function=lambda z: (((z + 4) * (z - 4) * (z + 4j) * (z - 4j)) ** (1 / 8)),
            title="$f(z) = ((z+4)(z-4)(z + 4j)(z - 4j))^{\\frac{1}{8}}$",
        ),
        DomainPlot(
            function=lambda z: ((z**2 - 1) * (z - 2 - 1j) ** 2) / (z**2 + 2 + 2j),
            title="$f(z) = \\frac{(z^2 - 1)(z - 2 - 1j)^2}{z^2 +2+ 2j}$",
        ),
    ],
    name="algebraic",
)

SPECIAL_PLOTS = DomainPlotGroup(
    plots=[
        DomainPlot(function=lambda z: np.sin(z), title="$f(z) = \\sin(z)$"),
        DomainPlot(function=lambda z: np.cos(z), title="$f(z) = \\cos(z)$"),
        DomainPlot(
            function=lambda z: np.sin(1 / z), title="$f(z) = \\sin(\\frac{1}{z})$"
        ),
        DomainPlot(
            function=lambda z: np.cos(1 / z), title="$f(z) = \\cos(\\frac{1}{z})$"
        ),
        DomainPlot(function=lambda z: z**z, title="$f(z) = z^z$"),
    ],
    name="special",
)

ALL_GROUPS = [LINEAR_PLOTS, POLYNOMIAL_PLOTS, ALGEBRAIC_PLOTS, SPECIAL_PLOTS]


def plot_one(plot: DomainPlot, color_map, file=None):
    """Plot an example plot"""
    plt.gcf().clear()
    dcolor.plot(
        plot.function,
        xlim=(-8, 8),
        ylim=(-8, 8),
        cmap=color_map,
        show=False,
    )
    plt.title(plot.title)
    plt.tight_layout()

    if file is not None:
        plt.savefig(file)
    else:
        plt.show()


def plot_group(group: DomainPlotGroup, color_map, file=None):
    """Plot a group of example plots on one matplotlib figure"""
    plt.gcf().clear()
    for i, plot in enumerate(group.plots):
        if i > 6:
            print(f"Omitting plot {i} for {plot.title}")
            continue
        plt.subplot(2 if len(group.plots) > 3 else 1, 3, i + 1)

        dcolor.plot(
            plot.function,
            xlim=(-8, 8),
            ylim=(-8, 8),
            cmap=color_map,
            show=False,
        )
        plt.title(plot.title)

    plt.tight_layout()

    if file is not None:
        plt.gcf().set_size_inches(10, 7.5)
        plt.savefig(file)
    else:
        plt.show()


def plot_single(which, color_map, file_prefix: Optional[str] = None):
    """Plot a single plot from available"""
    plot_groups = which.split(".")

    group_name = plot_groups[0]
    target_group = next(
        (group for group in ALL_GROUPS if group.name == group_name), None
    )
    if target_group is None:
        print(
            f"Could not interpret {plot_groups[1]} as a valid group name.\nValid names are:"
        )
        pprint([group.name for group in ALL_GROUPS])
        sys.exit(1)

    plot_number = None
    if len(plot_groups) > 1:
        try:
            plot_number = int(plot_groups[1])
        except ValueError:
            print(
                f"Could not interpret {plot_groups[1]} as a valid plot number.\n"
                f"Please supply a number between 1 and {len(target_group.plots)}"
            )
            sys.exit(1)

    if plot_number is None:
        plot_group(
            target_group,
            color_map,
            f"{file_prefix}_{group_name}.png" if file_prefix else None,
        )
    else:
        plot_one(
            target_group.plots[plot_number - 1],
            color_map,
            f"{file_prefix}_{group_name}_{plot_number}.png" if file_prefix else None,
        )


def main():
    color_maps = [cmap for cmap in cmaps.__all__]  # TODO: very hacky
    single_plots = [
        *[group.name for group in ALL_GROUPS],
        *[
            f"{group.name}.{i+1}"
            for group in ALL_GROUPS
            for i in range(len(group.plots))
        ],
    ]

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-i",
        "--individual",
        action="store_true",
        help="Plot each example plot individually.",
    )
    parser.add_argument(
        "-g", "--grouped", action="store_true", help="Plot each example plot in groups."
    )
    parser.add_argument(
        "-s",
        "--single",
        metavar="SINGLE",
        choices=single_plots,
        help=f"Show a single example plot (or group of plots). Available options are: "
        + ", \n".join(f"{group.name}[.1-{len(group.plots)}]" for group in ALL_GROUPS),
    )
    parser.add_argument(
        "-c",
        "--color-map",
        metavar="COLOR_MAP",
        choices=color_maps,
        default="magnitude_oscillating",
        help="The color map to use. Available options are: " + ", \n".join(color_maps),
    )
    parser.add_argument(
        "-f",
        "--file",
        action="store_true",
        help="Write output(s) to file(s), rather than displaying them."
        "Plots are written to `{color_map}_{plot_name}.png`.",
    )

    args = parser.parse_args()

    try:
        color_map = getattr(cmaps, args.color_map)
        assert callable(color_map)
    except:
        print(
            "Bad color map specified with `-c`. Available options are:"
            + ", \n".join(color_maps)
        )
        sys.exit(1)

    if args.color_map is None:
        sys.exit(1)

    if args.single is not None:
        plot_single(args.single, color_map, args.color_map if args.file else None)
        return

    if args.individual:
        for group in ALL_GROUPS:
            for i, plot in enumerate(group.plots):
                plot_one(
                    plot,
                    color_map,
                    f"{args.color_map}_{group.name}_{i}.png" if args.file else None,
                )
        return

    if args.grouped:
        for group in ALL_GROUPS:
            plot_group(
                group,
                color_map,
                f"{args.color_map}_{group.name}.png" if args.file else None,
            )
        return

    print("`-i` or `-g` not specified, printing help")
    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
