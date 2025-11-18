# tufte_style_plots

**Zero-configuration Tufte-style visualizations for Python**

A minimalist plotting library that creates beautiful, data-focused visualizations following Edward Tufte's principles. No configuration required—just plot.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## Features

- **Zero configuration** - Beautiful plots with one line of code
- **Tufte principles** - Maximizes data-ink ratio, minimizes chart junk
- **Matplotlib backend** - Fully compatible with matplotlib workflows
- **Clean API** - Three simple functions: `histogram()`, `line()`, `scatter()`
- **Multiple data types** - Works with lists, NumPy arrays, Pandas Series

---

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/bfarzin/tufte_style_plots.git
cd tufte_style_plots

# Install dependencies
pip install -e .
```

### Basic Usage

```python
import tufte_style_plots as tufte
import numpy as np

# Histogram - automatically normalized to 100%
data = np.random.normal(0, 1, 1000)
fig, ax = tufte.histogram(data, title='Normal Distribution')

# Line plot - clean and minimal
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = tufte.line(x, y, title='Sine Wave')

# Scatter plot - with optional marginal distributions
x = np.random.randn(200)
y = 2*x + np.random.randn(200)
fig, axes = tufte.scatter(x, y, marginals=True, title='Correlation')

# Save high-resolution output
fig.savefig('plot.png', dpi=300)
```

---

## Examples

### Histogram

```python
import tufte_style_plots as tufte
import numpy as np

# Create data
data = np.random.normal(0, 1, 1000)

# Create histogram (automatically normalized to 100%)
fig, ax = tufte.histogram(
    data,
    title='Distribution of Sample Data',
    xlabel='Value',
    bins=30
)
```

**Features:**
- Bars sum to 100% (percentage scale)
- No borders on bars
- Range frame (axes span only data extent)
- Minimal y-axis ticks
- Clean typography

### Line Plot

```python
# Single line
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = tufte.line(x, y, xlabel='x', ylabel='sin(x)')

# Multiple lines
y1 = np.sin(x)
y2 = np.cos(x)
fig, ax = tufte.line(
    x, [y1, y2],
    labels=['sin(x)', 'cos(x)'],
    title='Trigonometric Functions'
)

# With markers for sparse data
x_sparse = np.linspace(0, 10, 20)
y_sparse = np.sin(x_sparse)
fig, ax = tufte.line(x_sparse, y_sparse, markers=True)
```

**Features:**
- Thin, clean lines
- Grayscale palette for multiple series
- Optional hollow circle markers
- Minimal legend (frameless)
- Range frames on both axes

### Scatter Plot

```python
# Basic scatter
x = np.random.randn(200)
y = 2*x + np.random.randn(200)
fig, ax = tufte.scatter(
    x, y,
    title='Linear Correlation',
    xlabel='X',
    ylabel='Y'
)

# Scatter with marginal distributions
fig, axes = tufte.scatter(
    x, y,
    marginals=True,
    title='With Marginal Histograms'
)
# axes is a dict: {'main': ax_main, 'top': ax_top, 'right': ax_right}
```

**Features:**
- Clean scatter points with transparency
- Optional marginal histograms (top and right)
- Perfect alignment of marginals with main plot
- Customizable marker size and alpha

---

## API Reference

### `histogram(data, **kwargs)`

Create a Tufte-style histogram normalized to 100%.

**Parameters:**
- `data`: array-like - Data to plot
- `bins`: int or str (default: 'auto') - Number of bins or strategy
- `title`: str (optional) - Plot title
- `xlabel`: str (optional) - X-axis label
- `ylabel`: str (default: 'Percentage') - Y-axis label
- `figsize`: tuple (default: (8, 5)) - Figure size in inches
- `color`: str (default: black) - Bar color
- `ax`: Axes (optional) - Existing axes to plot on

**Returns:** `(fig, ax)` - Matplotlib Figure and Axes objects

---

### `line(x, y, **kwargs)`

Create a Tufte-style line plot.

**Parameters:**
- `x`: array-like - X-axis data
- `y`: array-like or list of arrays - Y-axis data (single or multiple series)
- `labels`: str or list of str (optional) - Line labels for legend
- `title`: str (optional) - Plot title
- `xlabel`, `ylabel`: str (optional) - Axis labels
- `figsize`: tuple (default: (8, 5)) - Figure size
- `markers`: bool (default: False) - Show markers at data points
- `colors`: list of str (optional) - Custom line colors
- `ax`: Axes (optional) - Existing axes to plot on

**Returns:** `(fig, ax)` - Matplotlib Figure and Axes objects

---

### `scatter(x, y, marginals=False, **kwargs)`

Create a Tufte-style scatter plot with optional marginal histograms.

**Parameters:**
- `x`, `y`: array-like - Data to plot
- `marginals`: bool (default: False) - Show marginal histograms
- `title`: str (optional) - Plot title
- `xlabel`, `ylabel`: str (optional) - Axis labels
- `figsize`: tuple (optional) - Figure size (auto if not specified)
- `color`: str (default: black) - Marker color
- `alpha`: float (default: 0.6) - Marker transparency
- `size`: float (default: 30) - Marker size
- `ax`: Axes (optional) - Existing axes (ignored if marginals=True)

**Returns:**
- If `marginals=False`: `(fig, ax)`
- If `marginals=True`: `(fig, axes_dict)` where axes_dict has keys 'main', 'top', 'right'

---

## Design Philosophy

This library implements Edward Tufte's principles of data visualization:

1. **Maximize data-ink ratio** - Every visual element conveys information
2. **Minimize chart junk** - Remove unnecessary decorations
3. **Range frames** - Axes span only the data extent
4. **Despine** - Remove top and right axis lines
5. **Minimal typography** - Clean serif fonts, appropriate sizes
6. **Grayscale first** - Use color sparingly and intentionally
7. **White space** - Let the data breathe

---

## Limitations

**Known issues:**

- **NaN values** - Must be filtered before plotting (automatic filtering in v0.2.0)
- **Infinite values** - Must be filtered before plotting
- **Large scatter plots** - Performance degrades above ~10,000 points

See [`docs/LIMITATIONS.md`](docs/LIMITATIONS.md) for detailed information on boundaries and edge cases.

**Workarounds:**

```python
# Filter NaN and Inf values
data_clean = data[np.isfinite(data)]
tufte.histogram(data_clean)

# Subsample large datasets
if len(x) > 5000:
    indices = np.random.choice(len(x), 5000, replace=False)
    tufte.scatter(x[indices], y[indices], alpha=0.3)
```

---

## Testing

**Comprehensive test suite:** 36 test scenarios covering:
- Different data distributions (normal, uniform, exponential, bimodal)
- Various data sizes (1 to 100,000 points)
- Multiple input types (lists, NumPy, Pandas)
- Edge cases (single point, constant values, NaN, Inf)

**Results:** 30/36 tests passed (83.3%)

Run tests:
```bash
python examples/comprehensive_test.py
```

Generate example plots:
```bash
python examples/generate_examples.py
# Output: examples/output/*.png
```

---

## Project Structure

```
tufte_style_plots/
├── tufte_style_plots/      # Main package
│   ├── __init__.py         # API exports
│   ├── core.py             # Plotting functions
│   ├── styles.py           # Style constants
│   └── utils.py            # Utility functions
├── examples/               # Example scripts
│   ├── comprehensive_test.py
│   ├── generate_examples.py
│   └── output/             # Generated plot images
├── docs/                   # Documentation
│   ├── SPECIFICATION.md    # Technical spec
│   ├── TUFTE_RESOURCES_SURVEY.md
│   ├── LIMITATIONS.md      # Known issues
│   └── CLAUDE.md           # AI assistant guide
├── tests/                  # Unit tests (future)
├── pyproject.toml          # Package configuration
├── README.md               # This file
└── LICENSE                 # MIT License
```

---

## Dependencies

**Required:**
- Python 3.8+
- matplotlib >= 3.5.0
- numpy >= 1.20.0

**Optional:**
- pandas >= 1.3.0 (for Pandas Series support)

---

## Roadmap

### v0.1.0 (Current)
- ✓ Core API: histogram, line, scatter
- ✓ Scatter with marginals
- ✓ Comprehensive testing
- ✓ Documentation

### v0.2.0 (Planned)
- [ ] Automatic NaN/Inf filtering with warnings
- [ ] Box plots (Tufte style)
- [ ] Bar charts (horizontal, minimal)
- [ ] Direct labeling for line plots
- [ ] PyPI distribution

### v0.3.0 (Future)
- [ ] Slope graphs (before/after comparisons)
- [ ] Sparklines (inline mini-plots)
- [ ] Small multiples (panel/facet plots)
- [ ] Enhanced color themes

---

## Contributing

This is currently a personal project by Bobak Farzin. Contributions, suggestions, and bug reports are welcome!

1. Check existing issues or create a new one
2. Fork the repository
3. Create a feature branch
4. Submit a pull request

---

## References

### Edward Tufte's Books
- *The Visual Display of Quantitative Information* (1983)
- *Envisioning Information* (1990)
- *Visual Explanations* (1997)
- *Beautiful Evidence* (2006)

### Inspiration
- See [`docs/TUFTE_RESOURCES_SURVEY.md`](docs/TUFTE_RESOURCES_SURVEY.md) for 20+ existing implementations across Python and R

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Bobak Farzin

---

## Contact

**Author:** Bobak Farzin
**Repository:** https://github.com/bfarzin/tufte_style_plots
**Issues:** https://github.com/bfarzin/tufte_style_plots/issues

---

## Acknowledgments

- Edward Tufte for establishing principles of excellent data visualization
- The matplotlib community for providing a robust plotting backend
- Existing Tufte-style packages (dufte, matplotlib_tufte, ggthemes) for inspiration
