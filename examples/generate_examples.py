"""
Generate example plots to demonstrate tufte_style_plots visual output.

Creates a gallery of example plots showing various use cases.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
import matplotlib.pyplot as plt
import tufte_style_plots as tufte

# Create output directory
os.makedirs('examples/output', exist_ok=True)

print("Generating example plots...")

# Example 1: Simple histogram
print("1. Histogram - Normal distribution")
data = np.random.normal(0, 1, 1000)
fig, ax = tufte.histogram(data, title='Normal Distribution', xlabel='Value')
fig.savefig('examples/output/01_histogram_normal.png', dpi=150, bbox_inches='tight')
plt.close()

# Example 2: Histogram - Bimodal
print("2. Histogram - Bimodal distribution")
data = np.concatenate([
    np.random.normal(-2, 0.5, 500),
    np.random.normal(2, 0.5, 500)
])
fig, ax = tufte.histogram(data, title='Bimodal Distribution', xlabel='Value')
fig.savefig('examples/output/02_histogram_bimodal.png', dpi=150, bbox_inches='tight')
plt.close()

# Example 3: Simple line plot
print("3. Line plot - Sine wave")
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
fig, ax = tufte.line(x, y, title='Sine Wave', xlabel='x', ylabel='sin(x)')
fig.savefig('examples/output/03_line_sine.png', dpi=150, bbox_inches='tight')
plt.close()

# Example 4: Multiple lines
print("4. Line plot - Multiple functions")
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
fig, ax = tufte.line(
    x, [y1, y2],
    labels=['sin(x)', 'cos(x)'],
    title='Trigonometric Functions',
    xlabel='x',
    ylabel='f(x)'
)
fig.savefig('examples/output/04_line_multiple.png', dpi=150, bbox_inches='tight')
plt.close()

# Example 5: Line with markers
print("5. Line plot - With markers")
x = np.linspace(0, 10, 20)
y = np.sin(x) + np.random.normal(0, 0.1, 20)
fig, ax = tufte.line(x, y, markers=True, title='Noisy Data with Markers', xlabel='x', ylabel='y')
fig.savefig('examples/output/05_line_markers.png', dpi=150, bbox_inches='tight')
plt.close()

# Example 6: Simple scatter
print("6. Scatter - Linear correlation")
np.random.seed(42)
x = np.random.randn(200)
y = 2*x + np.random.randn(200)
fig, ax = tufte.scatter(
    x, y,
    title='Linear Correlation',
    xlabel='Independent Variable',
    ylabel='Dependent Variable'
)
fig.savefig('examples/output/06_scatter_correlation.png', dpi=150, bbox_inches='tight')
plt.close()

# Example 7: Scatter - Clusters
print("7. Scatter - Two clusters")
cluster1_x = np.random.normal(-2, 0.5, 100)
cluster1_y = np.random.normal(-2, 0.5, 100)
cluster2_x = np.random.normal(2, 0.5, 100)
cluster2_y = np.random.normal(2, 0.5, 100)
x = np.concatenate([cluster1_x, cluster2_x])
y = np.concatenate([cluster1_y, cluster2_y])
fig, ax = tufte.scatter(x, y, title='Two Clusters', alpha=0.5)
fig.savefig('examples/output/07_scatter_clusters.png', dpi=150, bbox_inches='tight')
plt.close()

# Example 8: Scatter with marginals - correlation
print("8. Scatter with marginals - Linear correlation")
np.random.seed(42)
x = np.random.randn(300)
y = 2*x + np.random.randn(300)
fig, axes = tufte.scatter(
    x, y,
    marginals=True,
    title='Scatter with Marginal Distributions',
    xlabel='X Variable',
    ylabel='Y Variable'
)
fig.savefig('examples/output/08_scatter_marginals_correlation.png', dpi=150, bbox_inches='tight')
plt.close()

# Example 9: Scatter with marginals - no correlation
print("9. Scatter with marginals - No correlation")
x = np.random.randn(300)
y = np.random.randn(300)
fig, axes = tufte.scatter(
    x, y,
    marginals=True,
    title='Independent Variables',
    xlabel='X',
    ylabel='Y'
)
fig.savefig('examples/output/09_scatter_marginals_independent.png', dpi=150, bbox_inches='tight')
plt.close()

# Example 10: Large dataset scatter
print("10. Scatter - Large dataset")
x = np.random.randn(2000)
y = 0.5*x + np.random.randn(2000)
fig, ax = tufte.scatter(x, y, title='Large Dataset (n=2000)', alpha=0.3, size=10)
fig.savefig('examples/output/10_scatter_large.png', dpi=150, bbox_inches='tight')
plt.close()

print("\nAll examples generated successfully!")
print("Output directory: examples/output/")
print("\nGenerated files:")
for i in range(1, 11):
    filename = f"examples/output/{i:02d}_*.png"
    print(f"  {filename}")
