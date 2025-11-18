# tufte_style_plots - Technical Specification

**Version:** 1.0
**Last Updated:** 2025-11-18
**Status:** Draft

---

## Vision

A **zero-configuration, opinionated** Python visualization library that produces Tufte-style plots with a simple, clean API. Users should get beautiful, minimal visualizations by default without any styling work.

### Core Principle
```python
import tufte_style_plots as tufte

# This just works - clean, minimal, beautiful
tufte.histogram(data)
tufte.line(x, y)
tufte.scatter(x, y, marginals=True)
```

No configuration, no styling, no cleanup. It just works.

---

## Design Philosophy

### 1. Opinionated Over Configurable
- **Sensible defaults** that follow Tufte principles strictly
- **Minimal API surface** - only essential parameters
- **Consistency** - all plots share the same visual language
- Power users can access underlying matplotlib objects for customization

### 2. Zero Configuration
- No style sheets to apply
- No rcParams to set
- No manual despining or cleanup
- Import and use immediately

### 3. Matplotlib Backend
- Thin wrapper over matplotlib
- Returns matplotlib Figure/Axes objects
- Compatible with matplotlib workflows
- Users can further customize if needed

---

## API Specification

### Core Functions

#### `tufte.histogram(data, **kwargs)`
**Purpose:** Normalized histogram where bars sum to 100%

**Parameters:**
- `data`: array-like - Data to plot (list, numpy array, pandas Series)
- `bins`: int or sequence, optional (default: 'auto') - Number of bins or bin edges
- `title`: str, optional - Plot title
- `xlabel`: str, optional - X-axis label
- `ylabel`: str, optional (default: 'Percentage') - Y-axis label
- `figsize`: tuple, optional (default: (8, 5)) - Figure size
- `ax`: matplotlib Axes, optional - Existing axes to plot on

**Returns:**
- `fig, ax`: matplotlib Figure and Axes objects

**Behavior:**
- Bars sum to 100% (normalized density)
- No borders on bars
- Range frame (axes only span data extent)
- Minimal y-axis ticks (0%, 25%, 50%, 75%, 100% or similar)
- No top/right spines
- Light gray or no gridlines
- Clean typography (serif font)

**Example:**
```python
import tufte_style_plots as tufte
import numpy as np

data = np.random.normal(0, 1, 1000)
fig, ax = tufte.histogram(data, title='Distribution of Sample Data')
```

---

#### `tufte.line(x, y, **kwargs)`
**Purpose:** Clean line plot with minimal decoration

**Parameters:**
- `x`: array-like - X-axis data
- `y`: array-like or list of array-like - Y-axis data (can be multiple lines)
- `labels`: str or list of str, optional - Line labels for legend
- `title`: str, optional - Plot title
- `xlabel`: str, optional - X-axis label
- `ylabel`: str, optional - Y-axis label
- `figsize`: tuple, optional (default: (8, 5)) - Figure size
- `markers`: bool, optional (default: False) - Show data point markers
- `ax`: matplotlib Axes, optional - Existing axes to plot on

**Returns:**
- `fig, ax`: matplotlib Figure and Axes objects

**Behavior:**
- Thin, clean lines (1-1.5pt)
- Range frame on both axes
- No top/right spines
- Minimal axis ticks (5-7 ticks max)
- Optional markers at data points (hollow circles if enabled)
- Direct labeling preferred (labels at line ends) over legend
- If legend needed: minimal, no box, no background

**Example:**
```python
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = tufte.line(x, [y1, y2], labels=['sin(x)', 'cos(x)'])
```

---

#### `tufte.scatter(x, y, marginals=False, **kwargs)`
**Purpose:** Clean scatter plot with optional marginal histograms

**Parameters:**
- `x`: array-like - X-axis data
- `y`: array-like - Y-axis data
- `marginals`: bool, optional (default: False) - Show marginal histograms on top/right
- `title`: str, optional - Plot title
- `xlabel`: str, optional - X-axis label
- `ylabel`: str, optional - Y-axis label
- `figsize`: tuple, optional (default: (8, 8) if marginals else (8, 5)) - Figure size
- `color`: str, optional (default: 'black') - Marker color
- `alpha`: float, optional (default: 0.6) - Marker transparency
- `size`: float, optional (default: 30) - Marker size
- `ax`: matplotlib Axes, optional - Existing axes to plot on (ignored if marginals=True)

**Returns:**
- If `marginals=False`: `fig, ax` (Figure and main Axes)
- If `marginals=True`: `fig, ax_dict` where `ax_dict = {'main': ax_main, 'top': ax_top, 'right': ax_right}`

**Behavior:**
- Hollow circles (edge only, no fill) or small filled circles with transparency
- Range frame on both axes
- No top/right spines (unless marginals=True)
- If `marginals=True`:
  - Main scatter in center
  - Normalized histogram on top (x-axis distribution)
  - Normalized histogram on right (y-axis distribution)
  - Marginal plots aligned perfectly with main plot
  - Shared axes for alignment

**Example:**
```python
# Simple scatter
x = np.random.randn(200)
y = 2*x + np.random.randn(200)
fig, ax = tufte.scatter(x, y, title='Correlation Example')

# Scatter with marginals
fig, axes = tufte.scatter(x, y, marginals=True, title='With Distributions')
```

---

### Utility Functions (Internal, but can be exposed)

#### `tufte.utils.despine(ax, top=True, right=True, left=False, bottom=False)`
Remove specified spines from axes.

#### `tufte.utils.range_frame(ax, x_data=None, y_data=None)`
Set axis limits to exactly span data range (no padding).

#### `tufte.utils.set_tufte_style(ax)`
Apply core Tufte styling to an axes object (font, ticks, etc.).

#### `tufte.utils.minimal_ticks(ax, max_ticks=7)`
Reduce number of axis ticks to minimal set.

---

## Visual Style Specification

### Typography
- **Font family:** Serif (prefer: Palatino, Georgia, or Computer Modern if available)
- **Font size:**
  - Title: 14pt
  - Axis labels: 11pt
  - Tick labels: 9pt
  - Legend: 9pt
- **Font weight:** Regular (not bold)

### Colors
- **Default data color:** Dark gray (#333333) or black (#000000)
- **Axis/spine color:** Medium gray (#666666)
- **Grid color:** Very light gray (#E5E5E5) at 50% opacity
- **Multiple series:** Use grayscale first, then minimal accent colors if needed
  - Series 1: #000000 (black)
  - Series 2: #666666 (dark gray)
  - Series 3: #999999 (medium gray)
  - Accent (if needed): #E74C3C (muted red) or #3498DB (muted blue)

### Lines & Markers
- **Line width:** 1.5pt (data lines), 0.75pt (axes)
- **Marker style:** 'o' (circle), hollow (facecolor='none', edgecolor='black')
- **Marker size:** 4-6pt
- **Alpha:** 0.6-0.8 for overlapping data

### Axes & Spines
- **Spine visibility:** Bottom and left only (range frame)
- **Spine width:** 0.75pt
- **Tick length:** 4pt
- **Tick width:** 0.75pt
- **Axis padding:** Minimal (2-3pt)

### Gridlines
- **Default:** No gridlines (or extremely subtle horizontal only)
- **If used:** Horizontal only, very light gray, behind data
- **Style:** Solid, 0.5pt width

### Whitespace
- **Figure padding:** 0.05 (5% of figure size)
- **Title padding:** 12pt above plot area
- **Legend padding:** 8pt from plot edge

---

## Implementation Architecture

### Package Structure

```
tufte_style_plots/
├── tufte_style_plots/
│   ├── __init__.py          # Main API: histogram, line, scatter
│   ├── core.py              # Core plotting function implementations
│   ├── styles.py            # Style constants and configurations
│   ├── utils.py             # Utility functions (despine, range_frame, etc.)
│   └── config.py            # Default configuration values
├── tests/
│   ├── __init__.py
│   ├── test_histogram.py
│   ├── test_line.py
│   ├── test_scatter.py
│   └── test_utils.py
├── examples/
│   ├── basic_histogram.py
│   ├── basic_line.py
│   ├── basic_scatter.py
│   └── marginal_scatter.py
├── docs/
│   ├── SPECIFICATION.md     # This file
│   ├── TUFTE_RESOURCES_SURVEY.md
│   ├── API.md               # API documentation
│   └── EXAMPLES.md          # Usage examples
├── pyproject.toml           # Modern Python packaging
├── README.md
├── LICENSE
├── CLAUDE.md
└── .gitignore
```

### Module Responsibilities

#### `__init__.py`
- Export main API functions: `histogram`, `line`, `scatter`
- Export utility functions (optional): `despine`, `range_frame`
- Package version and metadata

#### `core.py`
- Implementation of `histogram()`, `line()`, `scatter()`
- Each function:
  1. Validates input data
  2. Creates figure/axes if not provided
  3. Plots data with matplotlib
  4. Applies Tufte styling via `utils.set_tufte_style()`
  5. Returns figure and axes

#### `styles.py`
- Constants for colors, fonts, sizes
- rcParams dictionary for Tufte style
- Color palettes (grayscale + minimal accents)

```python
# Example constants
TUFTE_COLORS = {
    'primary': '#000000',
    'secondary': '#666666',
    'tertiary': '#999999',
    'accent_red': '#E74C3C',
    'accent_blue': '#3498DB',
    'grid': '#E5E5E5',
}

TUFTE_FONTS = {
    'family': 'serif',
    'serif': ['Palatino', 'Georgia', 'Computer Modern', 'Times New Roman'],
    'title_size': 14,
    'label_size': 11,
    'tick_size': 9,
}
```

#### `utils.py`
- `despine(ax, ...)`: Remove spines
- `range_frame(ax, data)`: Set limits to data extent
- `set_tufte_style(ax)`: Apply fonts, ticks, etc.
- `minimal_ticks(ax)`: Reduce tick density
- `normalize_to_percentage(data, bins)`: For histogram normalization
- `direct_label(ax, x, y, label)`: For line end labels

#### `config.py`
- Default figure sizes
- Default tick counts
- Default color choices
- User-customizable settings (if needed later)

---

## Data Type Support

### Input Types Accepted
All plotting functions should accept:
- Python lists: `[1, 2, 3, 4, 5]`
- NumPy arrays: `np.array([1, 2, 3, 4, 5])`
- Pandas Series: `df['column']`
- Pandas DataFrame columns (for multi-line plots)

### Type Conversion Strategy
```python
def _to_array(data):
    """Convert various data types to numpy array."""
    if hasattr(data, 'values'):  # Pandas Series/DataFrame
        return data.values
    return np.asarray(data)
```

---

## Technical Requirements

### Dependencies
**Required:**
- `matplotlib >= 3.5.0` - Core plotting backend
- `numpy >= 1.20.0` - Array operations

**Optional:**
- `pandas >= 1.3.0` - DataFrame support (graceful fallback if not installed)

**Development:**
- `pytest >= 7.0` - Testing
- `pytest-cov` - Test coverage
- `black` - Code formatting
- `mypy` - Type checking
- `ruff` - Linting

### Python Version
- **Minimum:** Python 3.8
- **Recommended:** Python 3.10+
- **Type hints:** Full type annotations for all public functions

### Type Hints Example
```python
from typing import Optional, Union, Tuple, List, Dict
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

def histogram(
    data: Union[List, np.ndarray],
    bins: Union[int, str] = 'auto',
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: str = 'Percentage',
    figsize: Tuple[float, float] = (8, 5),
    ax: Optional[Axes] = None
) -> Tuple[Figure, Axes]:
    """Create a Tufte-style histogram normalized to 100%."""
    ...
```

---

## Implementation Phases

### Phase 1: Foundation (MVP)
**Goal:** Core package structure and basic histogram

- [ ] Set up package structure (pyproject.toml, __init__.py, etc.)
- [ ] Implement `styles.py` with constants
- [ ] Implement `utils.py` basic functions (despine, range_frame, set_tufte_style)
- [ ] Implement `core.histogram()`
- [ ] Write tests for histogram
- [ ] Create example script
- [ ] Basic README with installation and usage

**Deliverable:** Working `tufte.histogram()` that can be installed and used

### Phase 2: Line & Scatter Plots
**Goal:** Complete core API

- [ ] Implement `core.line()`
- [ ] Implement `core.scatter()` (without marginals)
- [ ] Write tests for line and scatter
- [ ] Create example scripts
- [ ] Update documentation

**Deliverable:** Full basic API (`histogram`, `line`, `scatter`)

### Phase 3: Marginal Scatter
**Goal:** Advanced scatter plot with distributions

- [ ] Implement marginal histogram layout (GridSpec)
- [ ] Implement `scatter(marginals=True)`
- [ ] Ensure perfect alignment of marginals with main plot
- [ ] Write tests for marginal scatter
- [ ] Create example script

**Deliverable:** `scatter(marginals=True)` working

### Phase 4: Polish & Documentation
**Goal:** Production-ready package

- [ ] Complete API documentation
- [ ] Create comprehensive examples gallery
- [ ] Add docstring examples to all functions
- [ ] Ensure 100% type hint coverage
- [ ] Achieve >90% test coverage
- [ ] Create tutorial notebook
- [ ] Set up CI/CD (GitHub Actions)

**Deliverable:** v1.0.0 release candidate

### Phase 5: Distribution
**Goal:** Public release

- [ ] Publish to PyPI
- [ ] Create documentation site (Read the Docs or GitHub Pages)
- [ ] Announce on relevant forums (r/datascience, Twitter, etc.)
- [ ] Gather user feedback

**Deliverable:** v1.0.0 on PyPI

---

## Future Enhancements (Post-v1.0)

### Additional Plot Types
- **Box plot** (Tufte-style: median dot + whiskers only)
- **Bar chart** (minimal, no borders, horizontal preferred)
- **Slope graph** (before/after comparison)
- **Sparklines** (small, inline plots)
- **Small multiples** (panel/facet plots)

### Advanced Features
- **Direct labeling** utilities (label lines at endpoints instead of legend)
- **Color themes** (allow minimal customization while staying Tufte)
- **Export presets** (PDF with embedded fonts, high-res PNG)
- **Annotation helpers** (minimal, clean annotations)

### Data Analysis Integration
- **Statistical overlays** (mean, median, quartiles shown minimally)
- **Regression lines** (with minimal display)
- **Confidence intervals** (subtle shading)

### Customization (If Requested)
- **Configuration file** support (for users who want to override defaults)
- **Theme variants** (light, dark, grayscale, print)
- **Font selection** (allow users to specify preferred serif font)

---

## Success Metrics

### For v1.0 Release:
1. **Installation:** `pip install tufte_style_plots` works on Python 3.8+
2. **Usage:** All three core functions work with zero configuration
3. **Quality:**
   - >90% test coverage
   - 100% type hints on public API
   - Passes mypy type checking
   - Zero critical bugs
4. **Documentation:**
   - API reference complete
   - At least 5 working examples
   - Tutorial/quickstart guide
5. **Performance:** Plots render in <1 second for typical datasets (1000s of points)

### User Experience Goals:
- **"It just works"** - No configuration required
- **"It looks good"** - Tufte principles automatically applied
- **"It's simple"** - Minimal API surface, easy to remember
- **"It's compatible"** - Works with existing matplotlib workflows

---

## Example Usage (Final API)

```python
import tufte_style_plots as tufte
import numpy as np

# Generate sample data
np.random.seed(42)
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + np.random.normal(0, 0.1, 100)
y2 = np.cos(x) + np.random.normal(0, 0.1, 100)
data = np.random.normal(0, 1, 1000)

# Histogram - normalized to 100%
fig, ax = tufte.histogram(
    data,
    title='Normal Distribution',
    xlabel='Value'
)
fig.savefig('histogram.png', dpi=300)

# Line plot - clean and minimal
fig, ax = tufte.line(
    x,
    [y1, y2],
    labels=['sin(x)', 'cos(x)'],
    title='Trigonometric Functions',
    xlabel='x',
    ylabel='f(x)'
)
fig.savefig('line.png', dpi=300)

# Scatter plot - simple
x_scatter = np.random.randn(200)
y_scatter = 2*x_scatter + np.random.randn(200)
fig, ax = tufte.scatter(
    x_scatter,
    y_scatter,
    title='Correlation Example',
    xlabel='Independent Variable',
    ylabel='Dependent Variable'
)
fig.savefig('scatter.png', dpi=300)

# Scatter with marginals - shows distributions
fig, axes = tufte.scatter(
    x_scatter,
    y_scatter,
    marginals=True,
    title='Scatter with Marginal Distributions'
)
# axes is a dict: {'main': ax_main, 'top': ax_top, 'right': ax_right}
fig.savefig('scatter_marginals.png', dpi=300)
```

---

## Open Questions for Discussion

1. **Normalization:**
   - Should histogram always sum to 100%, or offer option for counts?
   - Current spec: Always 100% (opinionated). Override: user can use matplotlib directly.

2. **Marginal orientation:**
   - Marginal histograms: should they be horizontal/vertical bars, or density curves?
   - Current spec: Histograms (bars) for consistency with main histogram API.

3. **Multiple y-axes:**
   - Should `line()` support dual y-axes (often considered chart junk)?
   - Current spec: No. Use small multiples instead.

4. **Legend vs Direct Labels:**
   - Should we auto-implement direct labeling for line plots?
   - Current spec: Phase 2 implementation, use minimal legend for v1.0.

5. **Error bars:**
   - How to show uncertainty in Tufte style (minimal, non-distracting)?
   - Current spec: Post-v1.0 feature.

---

**Next Steps:**
- Review and approve this specification
- Begin Phase 1 implementation
- Set up package infrastructure (pyproject.toml, tests/, etc.)
- Implement first working histogram function
