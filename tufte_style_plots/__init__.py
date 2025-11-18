"""
tufte_style_plots - Zero-configuration Tufte-style visualizations

A Python library for creating minimalist, data-focused visualizations
following Edward Tufte's principles of data visualization.

Example usage:
    >>> import tufte_style_plots as tufte
    >>> import numpy as np
    >>>
    >>> # Histogram normalized to 100%
    >>> data = np.random.normal(0, 1, 1000)
    >>> fig, ax = tufte.histogram(data, title='Normal Distribution')
    >>>
    >>> # Clean line plot
    >>> x = np.linspace(0, 10, 100)
    >>> y = np.sin(x)
    >>> fig, ax = tufte.line(x, y, title='Sine Wave')
    >>>
    >>> # Scatter with marginal distributions
    >>> x = np.random.randn(200)
    >>> y = 2*x + np.random.randn(200)
    >>> fig, axes = tufte.scatter(x, y, marginals=True)
"""

__version__ = "0.1.0"
__author__ = "Bobak Farzin"
__license__ = "MIT"

from .core import histogram, line, scatter
from .utils import despine, range_frame, set_tufte_style

__all__ = [
    # Main plotting functions
    'histogram',
    'line',
    'scatter',
    # Utility functions
    'despine',
    'range_frame',
    'set_tufte_style',
    # Metadata
    '__version__',
    '__author__',
    '__license__',
]
