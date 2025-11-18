"""
Utility functions for applying Tufte styling to matplotlib plots.

This module provides helper functions for despining, range framing,
tick reduction, and other styling operations.
"""

from typing import Optional, Union, List, Tuple
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.ticker import MaxNLocator

from .styles import TUFTE_RC_PARAMS, TICK_STYLES, TUFTE_FONTS


def to_array(data: Union[List, np.ndarray, 'pd.Series']) -> np.ndarray:
    """
    Convert various data types to numpy array.

    Args:
        data: Input data (list, numpy array, or pandas Series)

    Returns:
        NumPy array representation of the data
    """
    if hasattr(data, 'values'):  # Pandas Series/DataFrame
        return data.values
    return np.asarray(data)


def despine(
    ax: Axes,
    top: bool = True,
    right: bool = True,
    left: bool = False,
    bottom: bool = False
) -> None:
    """
    Remove specified spines from axes.

    Following Tufte's principle of minimizing non-data ink,
    removes unnecessary axis spines.

    Args:
        ax: Matplotlib Axes object
        top: Remove top spine (default: True)
        right: Remove right spine (default: True)
        left: Remove left spine (default: False)
        bottom: Remove bottom spine (default: False)
    """
    if top:
        ax.spines['top'].set_visible(False)
    if right:
        ax.spines['right'].set_visible(False)
    if left:
        ax.spines['left'].set_visible(False)
    if bottom:
        ax.spines['bottom'].set_visible(False)


def range_frame(
    ax: Axes,
    x_data: Optional[np.ndarray] = None,
    y_data: Optional[np.ndarray] = None,
    x_padding: float = 0.02,
    y_padding: float = 0.02
) -> None:
    """
    Apply Tufte's range frame: spines only extend from min to max of data.

    This is a key feature of Tufte-style plots - the axis spines themselves
    are bounded to show the data range at a glance, rather than extending
    arbitrarily beyond the data.

    Args:
        ax: Matplotlib Axes object
        x_data: X-axis data (optional)
        y_data: Y-axis data (optional)
        x_padding: Fractional padding for x-axis limits (default: 2%)
        y_padding: Fractional padding for y-axis limits (default: 2%)
    """
    if x_data is not None:
        x_min, x_max = np.min(x_data), np.max(x_data)
        x_range = x_max - x_min
        if x_range > 0:
            # Set axis limits with padding for visual breathing room
            ax.set_xlim(
                x_min - x_padding * x_range,
                x_max + x_padding * x_range
            )
            # Set spine bounds to exact data range (no padding)
            ax.spines['bottom'].set_bounds(x_min, x_max)
        else:
            # Single value or all same
            ax.set_xlim(x_min - 0.5, x_max + 0.5)
            ax.spines['bottom'].set_bounds(x_min, x_max)

    if y_data is not None:
        y_min, y_max = np.min(y_data), np.max(y_data)
        y_range = y_max - y_min
        if y_range > 0:
            # Set axis limits with padding for visual breathing room
            ax.set_ylim(
                y_min - y_padding * y_range,
                y_max + y_padding * y_range
            )
            # Set spine bounds to exact data range (no padding)
            ax.spines['left'].set_bounds(y_min, y_max)
        else:
            # Single value or all same
            ax.set_ylim(y_min - 0.5, y_max + 0.5)
            ax.spines['left'].set_bounds(y_min, y_max)


def minimal_ticks(ax: Axes, max_ticks: int = TICK_STYLES['max_ticks']) -> None:
    """
    Reduce number of axis ticks to minimal set.

    Args:
        ax: Matplotlib Axes object
        max_ticks: Maximum number of ticks per axis (default: 7)
    """
    ax.xaxis.set_major_locator(MaxNLocator(nbins=max_ticks, prune='both'))
    ax.yaxis.set_major_locator(MaxNLocator(nbins=max_ticks, prune='both'))


def set_tufte_style(ax: Axes) -> None:
    """
    Apply core Tufte styling to an axes object.

    This includes:
    - Despining (remove top and right spines)
    - Setting fonts
    - Reducing tick density
    - Applying consistent styling

    Args:
        ax: Matplotlib Axes object
    """
    # Despine
    despine(ax, top=True, right=True, left=False, bottom=False)

    # Minimal ticks
    minimal_ticks(ax)

    # Set tick parameters
    ax.tick_params(
        axis='both',
        which='major',
        length=TICK_STYLES['length'],
        width=TICK_STYLES['width'],
        labelsize=TUFTE_FONTS['tick_size']
    )

    # Remove minor ticks
    ax.tick_params(axis='both', which='minor', length=0)


def normalize_to_percentage(
    data: np.ndarray,
    bins: Union[int, str, np.ndarray]
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Calculate histogram values normalized to percentage (sum to 100%).

    Args:
        data: Input data array
        bins: Number of bins, binning strategy ('auto', 'fd', etc.), or bin edges

    Returns:
        Tuple of (bin_heights, bin_edges) where bin_heights sum to 100
    """
    counts, bin_edges = np.histogram(data, bins=bins)
    total = np.sum(counts)

    if total > 0:
        percentages = (counts / total) * 100.0
    else:
        percentages = counts.astype(float)

    return percentages, bin_edges


def apply_tufte_rcparams() -> dict:
    """
    Apply Tufte rcParams to matplotlib globally.

    Returns:
        Dictionary of previous rcParams (for restoration if needed)
    """
    previous_params = {}
    for key, value in TUFTE_RC_PARAMS.items():
        if key in plt.rcParams:
            previous_params[key] = plt.rcParams[key]
        plt.rcParams[key] = value
    return previous_params


def validate_data(data: Union[List, np.ndarray], name: str = "data") -> np.ndarray:
    """
    Validate and convert input data to numpy array.

    Args:
        data: Input data
        name: Name of the data parameter (for error messages)

    Returns:
        Validated numpy array

    Raises:
        ValueError: If data is empty or invalid
        TypeError: If data cannot be converted to array
    """
    try:
        arr = to_array(data)
    except Exception as e:
        raise TypeError(f"Could not convert {name} to array: {e}")

    if arr.size == 0:
        raise ValueError(f"{name} is empty")

    # Check for all NaN
    if np.all(np.isnan(arr)):
        raise ValueError(f"{name} contains only NaN values")

    return arr


def create_figure_and_axes(
    figsize: Tuple[float, float],
    ax: Optional[Axes] = None
) -> Tuple[plt.Figure, Axes]:
    """
    Create figure and axes, or use provided axes.

    Args:
        figsize: Figure size (width, height) in inches
        ax: Existing axes (optional)

    Returns:
        Tuple of (figure, axes)
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.get_figure()

    return fig, ax
