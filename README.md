# DColor: A Domain Coloring Python Module

## What is DColor?

DColor is a Python3 module for visualizing complex-valued functions using a [Domain Coloring](https://en.wikipedia.org/wiki/Domain_coloring) scheme.

## Requirements

DColor leverages two well-known Python libraries: Numpy and Matplotlib. Before being able to use DColor, you must install these using the following commands:

`$ python3 -m pip install -U numpy`

`$ python3 -m pip install -U matplotlib`

## clone the repository

`git clone https://github.com/hernanat/dcolor.git`

## run example

`python dcolorExample.py`

It generates a series of examples.
When each image appears clicking the close button starts the next example.
Lambda expressions are used to define and pass functions to the plot() function.
The last example is:

`dc.plot(lambda z : ((z**2-1)*(z-2- 1j)**2)/(z**2 +2+ 2j),
    title='((z**2-1)*(z-2- 1j)**2)/(z**2 +2+ 2j)')


Which results in the following plot:

![dcolor example](/images/dcolor.png)

## hsvcolor

This is like dcolor except that it does not convert the HSV image to RGB

`python hsvcolorExample.py`

Will create the images.
The last image produces:

![hsvcolor example](/images/hsvcolor.png)

## rgbcolor

This is designed to show  the magnitude of abs(z).
White means big, shades of green means intermediate, and black means small.

`python rgbcolorExample.py`

Will create the images.
The last image produces:

![hsvcolor example](/images/rgbcolor.png)


## Website and Documentation

Currently, this is a one-person project and so these are still under construction. Contact me by e-mail at roguegdi27@gmail.com if you would like to help out with anything.

## Contributing

If you are interested in contributing or have any suggested changes, clone the repo and make a pull request :)
