#DColor: A Domain Coloring Python Module

##What is DColor?

DColor is a Python3 module for visualizing complex-valued functions using a [Domain Coloring](https://en.wikipedia.org/wiki/Domain_coloring) scheme.

##Requirements

DColor leverages two well-known Python libraries: Numpy and Matplotlib. Before being able to use DColor, you must install these using the following commands:

`$ python3 -m pip install -U numpy`

`$ python3 -m pip install -U matplotlib`

##Quick Start

Prepare the source file in your local environment, and create an instance of the **DColor** object. For example:

`dc = DColor(xmin=-10, xmax=10, ymin=-10, ymax=10, samples=4000)`

Lambda expressions are used to define and pass functions to the plot() function. For example:

`dc.plot(lambda z : ((z+1-2j)*(z+2+2j)*((z-2)**2))/(z**3))`

Which results in the following plot:

![Example 1](/images/ex1.png)

##Website and Documentation

Currently, this is a one-person project and so these are still under construction. Contact me by e-mail at roguegdi27@gmail.com if you would like to help out with anything.

##Contributing

If you are interested in contributing or have any suggested changes, clone the repo and make a pull request :)
