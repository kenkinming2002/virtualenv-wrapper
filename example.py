#!/usr/bin/env virtualenv-wrapper
import virtualenv_wrapper
if virtualenv_wrapper.begin_setup():
    virtualenv_wrapper.install("PyQt5")
    virtualenv_wrapper.install("matplotlib")
    virtualenv_wrapper.end_setup()

# Example copied from https://matplotlib.org/stable/users/explain/quick_start.html#a-simple-example
import matplotlib.pyplot as plt
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.
