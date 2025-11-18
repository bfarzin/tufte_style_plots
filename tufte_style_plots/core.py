"""
Core plotting functions for Tufte-style visualizations.

This module implements the main API functions:
- histogram: Normalized histogram (bars sum to 100%)
- line: Minimal line plot
- scatter: Clean scatter plot with optional marginal histograms
"""

from typing import Optional, Union, List, Tuple, Dict
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.gridspec import GridSpec

from .styles import (
    TUFTE_COLORS,
    GRAYSCALE_PALETTE,
    MARKER_STYLES,
    FIGURE_SIZES,
    LINE_STYLES
)
from .utils import (
    validate_data,
    to_array,
    create_figure_and_axes,
    set_tufte_style,
    range_frame,
    normalize_to_percentage
)


def histogram(
    data: Union[List, np.ndarray],
    bins: Union[int, str, np.ndarray] = 'auto',
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: str = 'Percentage',
    figsize: Tuple[float, float] = FIGURE_SIZES['default'],
    ax: Optional[Axes] = None,
    color: str = TUFTE_COLORS['primary']
) -> Tuple[Figure, Axes]:
    """
    Create a Tufte-style histogram normalized to 100%.

    Args:
        data: Data to plot (list, numpy array, or pandas Series)
        bins: Number of bins, binning strategy, or bin edges (default: 'auto')
        title: Plot title (optional)
        xlabel: X-axis label (optional)
        ylabel: Y-axis label (default: 'Percentage')
        figsize: Figure size in inches (default: (8, 5))
        ax: Existing axes to plot on (optional)
        color: Bar color (default: black)

    Returns:
        Tuple of (figure, axes)

    Example:
        >>> import tufte_style_plots as tufte
        >>> import numpy as np
        >>> data = np.random.normal(0, 1, 1000)
        >>> fig, ax = tufte.histogram(data, title='Normal Distribution')
    """
    # Validate data
    data_array = validate_data(data, "data")

    # Create figure and axes
    fig, ax = create_figure_and_axes(figsize, ax)

    # Calculate normalized histogram
    percentages, bin_edges = normalize_to_percentage(data_array, bins)

    # Plot bars
    bin_width = bin_edges[1] - bin_edges[0]
    ax.bar(
        bin_edges[:-1],
        percentages,
        width=bin_width,
        align='edge',
        color=color,
        edgecolor='none',
        linewidth=0
    )

    # Apply Tufte styling
    set_tufte_style(ax)

    # Set labels
    if title:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Range frame on x-axis (y-axis starts at 0 for percentages)
    range_frame(ax, x_data=data_array, y_data=None)
    ax.set_ylim(bottom=0)

    return fig, ax


def line(
    x: Union[List, np.ndarray],
    y: Union[List, np.ndarray, List[Union[List, np.ndarray]]],
    labels: Optional[Union[str, List[str]]] = None,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: Tuple[float, float] = FIGURE_SIZES['default'],
    markers: bool = False,
    ax: Optional[Axes] = None,
    colors: Optional[List[str]] = None
) -> Tuple[Figure, Axes]:
    """
    Create a Tufte-style line plot with minimal decoration.

    Args:
        x: X-axis data (list, numpy array, or pandas Series)
        y: Y-axis data (single array or list of arrays for multiple lines)
        labels: Line labels for legend (str for single line, list for multiple)
        title: Plot title (optional)
        xlabel: X-axis label (optional)
        ylabel: Y-axis label (optional)
        figsize: Figure size in inches (default: (8, 5))
        markers: Show data point markers (default: False)
        ax: Existing axes to plot on (optional)
        colors: Custom colors for lines (optional, defaults to grayscale)

    Returns:
        Tuple of (figure, axes)

    Example:
        >>> import tufte_style_plots as tufte
        >>> import numpy as np
        >>> x = np.linspace(0, 10, 100)
        >>> y = np.sin(x)
        >>> fig, ax = tufte.line(x, y, title='Sine Wave')
    """
    # Validate x data
    x_array = validate_data(x, "x")

    # Handle single vs multiple y arrays
    if isinstance(y, list) and len(y) > 0 and isinstance(y[0], (list, np.ndarray)):
        # Multiple y arrays
        y_arrays = [validate_data(y_i, f"y[{i}]") for i, y_i in enumerate(y)]
        multiple_series = True
    else:
        # Single y array
        y_arrays = [validate_data(y, "y")]
        multiple_series = False

    # Validate all y arrays have same length as x
    for i, y_arr in enumerate(y_arrays):
        if len(y_arr) != len(x_array):
            raise ValueError(f"x and y[{i}] must have the same length")

    # Create figure and axes
    fig, ax = create_figure_and_axes(figsize, ax)

    # Determine colors
    if colors is None:
        colors = GRAYSCALE_PALETTE[:len(y_arrays)]
    elif len(colors) < len(y_arrays):
        # Extend with grayscale if not enough colors provided
        colors = list(colors) + GRAYSCALE_PALETTE[len(colors):len(y_arrays)]

    # Handle labels
    if labels is None:
        label_list = [None] * len(y_arrays)
    elif isinstance(labels, str):
        label_list = [labels]
    else:
        label_list = list(labels)

    # Ensure enough labels
    while len(label_list) < len(y_arrays):
        label_list.append(None)

    # Plot lines
    for i, (y_arr, color, label) in enumerate(zip(y_arrays, colors, label_list)):
        if markers:
            ax.plot(
                x_array,
                y_arr,
                color=color,
                linewidth=LINE_STYLES['data_width'],
                marker='o',
                markersize=4,
                markerfacecolor='none',
                markeredgecolor=color,
                markeredgewidth=1,
                label=label
            )
        else:
            ax.plot(
                x_array,
                y_arr,
                color=color,
                linewidth=LINE_STYLES['data_width'],
                label=label
            )

    # Apply Tufte styling
    set_tufte_style(ax)

    # Set labels
    if title:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)

    # Range frame
    all_y = np.concatenate(y_arrays)
    range_frame(ax, x_data=x_array, y_data=all_y)

    # Add legend if labels provided
    if any(label is not None for label in label_list):
        ax.legend(frameon=False, loc='best')

    return fig, ax


def scatter(
    x: Union[List, np.ndarray],
    y: Union[List, np.ndarray],
    marginals: bool = False,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: Optional[Tuple[float, float]] = None,
    color: str = TUFTE_COLORS['primary'],
    alpha: float = MARKER_STYLES['alpha'],
    size: float = MARKER_STYLES['size'],
    ax: Optional[Axes] = None
) -> Union[Tuple[Figure, Axes], Tuple[Figure, Dict[str, Axes]]]:
    """
    Create a Tufte-style scatter plot with optional marginal histograms.

    Args:
        x: X-axis data (list, numpy array, or pandas Series)
        y: Y-axis data (list, numpy array, or pandas Series)
        marginals: Show marginal histograms on top/right (default: False)
        title: Plot title (optional)
        xlabel: X-axis label (optional)
        ylabel: Y-axis label (optional)
        figsize: Figure size in inches (auto-determined if None)
        color: Marker color (default: black)
        alpha: Marker transparency (default: 0.6)
        size: Marker size in points squared (default: 30)
        ax: Existing axes to plot on (ignored if marginals=True)

    Returns:
        If marginals=False: Tuple of (figure, axes)
        If marginals=True: Tuple of (figure, dict) where dict has keys
                          'main', 'top', 'right' for the three axes

    Example:
        >>> import tufte_style_plots as tufte
        >>> import numpy as np
        >>> x = np.random.randn(200)
        >>> y = 2*x + np.random.randn(200)
        >>> fig, ax = tufte.scatter(x, y, title='Correlation')
    """
    # Validate data
    x_array = validate_data(x, "x")
    y_array = validate_data(y, "y")

    if len(x_array) != len(y_array):
        raise ValueError("x and y must have the same length")

    # Determine figure size
    if figsize is None:
        figsize = FIGURE_SIZES['square'] if marginals else FIGURE_SIZES['default']

    if marginals:
        return _scatter_with_marginals(
            x_array, y_array, title, xlabel, ylabel, figsize, color, alpha, size
        )
    else:
        return _scatter_basic(
            x_array, y_array, title, xlabel, ylabel, figsize, color, alpha, size, ax
        )


def _scatter_basic(
    x_array: np.ndarray,
    y_array: np.ndarray,
    title: Optional[str],
    xlabel: Optional[str],
    ylabel: Optional[str],
    figsize: Tuple[float, float],
    color: str,
    alpha: float,
    size: float,
    ax: Optional[Axes]
) -> Tuple[Figure, Axes]:
    """Create basic scatter plot without marginals."""
    # Create figure and axes
    fig, ax = create_figure_and_axes(figsize, ax)

    # Plot scatter
    ax.scatter(
        x_array,
        y_array,
        s=size,
        c=color,
        alpha=alpha,
        edgecolors='none',
        linewidths=0
    )

    # Apply Tufte styling
    set_tufte_style(ax)

    # Set labels
    if title:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)

    # Range frame
    range_frame(ax, x_data=x_array, y_data=y_array)

    return fig, ax


def _scatter_with_marginals(
    x_array: np.ndarray,
    y_array: np.ndarray,
    title: Optional[str],
    xlabel: Optional[str],
    ylabel: Optional[str],
    figsize: Tuple[float, float],
    color: str,
    alpha: float,
    size: float
) -> Tuple[Figure, Dict[str, Axes]]:
    """Create scatter plot with marginal histograms."""
    # Create figure with GridSpec
    fig = plt.figure(figsize=figsize)
    gs = GridSpec(
        3, 3,
        figure=fig,
        height_ratios=[1, 4, 0.1],
        width_ratios=[4, 1, 0.1],
        hspace=0.05,
        wspace=0.05
    )

    # Create axes
    ax_main = fig.add_subplot(gs[1, 0])
    ax_top = fig.add_subplot(gs[0, 0], sharex=ax_main)
    ax_right = fig.add_subplot(gs[1, 1], sharey=ax_main)

    # Main scatter plot
    ax_main.scatter(
        x_array,
        y_array,
        s=size,
        c=color,
        alpha=alpha,
        edgecolors='none',
        linewidths=0
    )

    # Top histogram (x distribution)
    percentages_x, bin_edges_x = normalize_to_percentage(x_array, bins='auto')
    bin_width_x = bin_edges_x[1] - bin_edges_x[0]
    ax_top.bar(
        bin_edges_x[:-1],
        percentages_x,
        width=bin_width_x,
        align='edge',
        color=color,
        edgecolor='none',
        alpha=0.7
    )

    # Right histogram (y distribution) - horizontal bars
    percentages_y, bin_edges_y = normalize_to_percentage(y_array, bins='auto')
    bin_width_y = bin_edges_y[1] - bin_edges_y[0]
    ax_right.barh(
        bin_edges_y[:-1],
        percentages_y,
        height=bin_width_y,
        align='edge',
        color=color,
        edgecolor='none',
        alpha=0.7
    )

    # Apply Tufte styling to main plot
    set_tufte_style(ax_main)
    range_frame(ax_main, x_data=x_array, y_data=y_array)

    # Style marginal plots
    ax_top.spines['top'].set_visible(False)
    ax_top.spines['right'].set_visible(False)
    ax_top.spines['left'].set_visible(False)
    ax_top.spines['bottom'].set_visible(False)
    ax_top.set_yticks([])
    ax_top.tick_params(labelbottom=False)

    ax_right.spines['top'].set_visible(False)
    ax_right.spines['right'].set_visible(False)
    ax_right.spines['left'].set_visible(False)
    ax_right.spines['bottom'].set_visible(False)
    ax_right.set_xticks([])
    ax_right.tick_params(labelleft=False)

    # Set axis limits for marginals to match main plot
    ax_top.set_ylim(bottom=0)
    ax_right.set_xlim(left=0)

    # Set labels on main plot
    if xlabel:
        ax_main.set_xlabel(xlabel)
    if ylabel:
        ax_main.set_ylabel(ylabel)

    # Set title on top plot
    if title:
        ax_top.set_title(title)

    # Return figure and axes dict
    axes_dict = {
        'main': ax_main,
        'top': ax_top,
        'right': ax_right
    }

    return fig, axes_dict
