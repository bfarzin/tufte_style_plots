"""
Tufte style constants and configurations.

This module defines colors, fonts, sizes, and other visual constants
that implement Edward Tufte's principles of data visualization.
"""

from typing import Dict, List

# Color palette
TUFTE_COLORS: Dict[str, str] = {
    'primary': '#000000',      # Black - main data color
    'secondary': '#666666',    # Dark gray - secondary series
    'tertiary': '#999999',     # Medium gray - tertiary series
    'accent_red': '#E74C3C',   # Muted red - accent color
    'accent_blue': '#3498DB',  # Muted blue - accent color
    'grid': '#E5E5E5',         # Very light gray - gridlines
    'spine': '#666666',        # Medium gray - axes
}

# Grayscale palette for multiple series
GRAYSCALE_PALETTE: List[str] = [
    '#000000',  # Black
    '#666666',  # Dark gray
    '#999999',  # Medium gray
    '#CCCCCC',  # Light gray
]

# Typography
TUFTE_FONTS: Dict[str, object] = {
    'family': 'serif',
    'serif': ['Palatino', 'Georgia', 'Computer Modern', 'Times New Roman', 'DejaVu Serif'],
    'title_size': 14,
    'label_size': 11,
    'tick_size': 9,
    'legend_size': 9,
}

# Line and marker styles
LINE_STYLES: Dict[str, float] = {
    'data_width': 1.5,      # Width of data lines
    'spine_width': 0.75,    # Width of axis spines
    'grid_width': 0.5,      # Width of gridlines
}

MARKER_STYLES: Dict[str, object] = {
    'style': 'o',           # Circle marker
    'size': 30,             # Marker size (in points squared)
    'edge_width': 1.0,      # Edge width for hollow markers
    'alpha': 0.6,           # Transparency
}

# Tick styles
TICK_STYLES: Dict[str, object] = {
    'length': 4,            # Tick length in points
    'width': 0.75,          # Tick width in points
    'max_ticks': 7,         # Maximum number of ticks per axis
}

# Spacing and padding
SPACING: Dict[str, float] = {
    'title_pad': 12,        # Padding above title (points)
    'label_pad': 8,         # Padding for axis labels (points)
    'tick_pad': 4,          # Padding for tick labels (points)
    'legend_pad': 8,        # Padding for legend (points)
}

# Default figure sizes (width, height in inches)
FIGURE_SIZES: Dict[str, tuple] = {
    'default': (8, 5),
    'square': (8, 8),
    'wide': (10, 5),
    'tall': (6, 8),
}

# Grid configuration
GRID_CONFIG: Dict[str, object] = {
    'enabled': False,       # Gridlines off by default
    'axis': 'y',           # If enabled, only horizontal gridlines
    'color': TUFTE_COLORS['grid'],
    'alpha': 0.5,
    'linewidth': LINE_STYLES['grid_width'],
    'linestyle': '-',
}

# Matplotlib rcParams for Tufte style
TUFTE_RC_PARAMS: Dict[str, object] = {
    # Figure
    'figure.facecolor': 'white',
    'figure.edgecolor': 'white',

    # Axes
    'axes.facecolor': 'white',
    'axes.edgecolor': TUFTE_COLORS['spine'],
    'axes.linewidth': LINE_STYLES['spine_width'],
    'axes.labelsize': TUFTE_FONTS['label_size'],
    'axes.titlesize': TUFTE_FONTS['title_size'],
    'axes.titlepad': SPACING['title_pad'],
    'axes.labelpad': SPACING['label_pad'],
    'axes.spines.top': False,
    'axes.spines.right': False,

    # Grid
    'axes.grid': GRID_CONFIG['enabled'],
    'axes.grid.axis': GRID_CONFIG['axis'],
    'grid.color': GRID_CONFIG['color'],
    'grid.alpha': GRID_CONFIG['alpha'],
    'grid.linewidth': GRID_CONFIG['linewidth'],
    'grid.linestyle': GRID_CONFIG['linestyle'],

    # Lines
    'lines.linewidth': LINE_STYLES['data_width'],
    'lines.markersize': 6,
    'lines.markeredgewidth': MARKER_STYLES['edge_width'],

    # Ticks
    'xtick.major.size': TICK_STYLES['length'],
    'xtick.major.width': TICK_STYLES['width'],
    'xtick.minor.size': 0,
    'xtick.labelsize': TUFTE_FONTS['tick_size'],
    'ytick.major.size': TICK_STYLES['length'],
    'ytick.major.width': TICK_STYLES['width'],
    'ytick.minor.size': 0,
    'ytick.labelsize': TUFTE_FONTS['tick_size'],

    # Font
    'font.family': TUFTE_FONTS['family'],
    'font.serif': TUFTE_FONTS['serif'],
    'font.size': TUFTE_FONTS['tick_size'],

    # Legend
    'legend.fontsize': TUFTE_FONTS['legend_size'],
    'legend.frameon': False,
    'legend.numpoints': 1,
    'legend.scatterpoints': 1,

    # Saving
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.facecolor': 'white',
    'savefig.edgecolor': 'white',
}
