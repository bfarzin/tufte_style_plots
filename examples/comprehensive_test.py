"""
Comprehensive test suite for tufte_style_plots package.

This script tests the package with 25+ different scenarios to identify:
- What works well
- What breaks
- Limitations and boundaries

Run with: python examples/comprehensive_test.py
"""

import sys
import os
import traceback

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
import matplotlib.pyplot as plt

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    print("Warning: pandas not available, skipping pandas tests")

import tufte_style_plots as tufte


class TestResult:
    """Track test results."""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.passed = False
        self.error = None
        self.warning = None


def run_test(test_name, test_description, test_func):
    """Run a single test and track results."""
    result = TestResult(test_name, test_description)
    print(f"\n{'='*70}")
    print(f"Test {test_name}: {test_description}")
    print(f"{'='*70}")

    try:
        test_func()
        result.passed = True
        print(f"✓ PASSED")
    except Exception as e:
        result.passed = False
        result.error = str(e)
        print(f"✗ FAILED: {e}")
        traceback.print_exc()

    plt.close('all')  # Clean up
    return result


# ==============================================================================
# HISTOGRAM TESTS
# ==============================================================================

def test_histogram_01():
    """Normal distribution, 1000 points"""
    data = np.random.normal(0, 1, 1000)
    fig, ax = tufte.histogram(data, title='Normal Distribution')
    assert fig is not None
    assert ax is not None


def test_histogram_02():
    """Uniform distribution, 500 points"""
    data = np.random.uniform(-5, 5, 500)
    fig, ax = tufte.histogram(data, title='Uniform Distribution', xlabel='Value')


def test_histogram_03():
    """Exponential distribution (right skewed)"""
    data = np.random.exponential(2, 1000)
    fig, ax = tufte.histogram(data, title='Exponential Distribution')


def test_histogram_04():
    """Bimodal distribution"""
    data = np.concatenate([
        np.random.normal(-2, 0.5, 500),
        np.random.normal(2, 0.5, 500)
    ])
    fig, ax = tufte.histogram(data, title='Bimodal Distribution')


def test_histogram_05():
    """Small dataset (20 points)"""
    data = np.random.randn(20)
    fig, ax = tufte.histogram(data, title='Small Dataset (n=20)', bins=5)


def test_histogram_06():
    """Large dataset (100k points)"""
    data = np.random.randn(100000)
    fig, ax = tufte.histogram(data, title='Large Dataset (n=100k)', bins=50)


def test_histogram_07():
    """Integer data"""
    data = np.random.randint(1, 10, 1000)
    fig, ax = tufte.histogram(data, title='Integer Data', bins=9)


def test_histogram_08():
    """Negative values only"""
    data = -np.abs(np.random.randn(500))
    fig, ax = tufte.histogram(data, title='Negative Values')


def test_histogram_09():
    """Single value repeated"""
    data = np.ones(100) * 5.0
    fig, ax = tufte.histogram(data, title='Single Value Repeated')


def test_histogram_10():
    """Very small range (0.001)"""
    data = np.random.uniform(1.0, 1.001, 100)
    fig, ax = tufte.histogram(data, title='Tiny Range')


def test_histogram_11():
    """Python list instead of numpy array"""
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10
    fig, ax = tufte.histogram(data, title='Python List Input')


def test_histogram_12():
    """Pandas Series (if available)"""
    if not PANDAS_AVAILABLE:
        raise ImportError("Pandas not available")
    data = pd.Series(np.random.randn(1000))
    fig, ax = tufte.histogram(data, title='Pandas Series Input')


# ==============================================================================
# LINE PLOT TESTS
# ==============================================================================

def test_line_01():
    """Simple sine wave"""
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = tufte.line(x, y, title='Sine Wave', xlabel='x', ylabel='sin(x)')


def test_line_02():
    """Multiple lines (2 series)"""
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    fig, ax = tufte.line(x, [y1, y2], labels=['sin(x)', 'cos(x)'], title='Trig Functions')


def test_line_03():
    """Multiple lines (4 series)"""
    x = np.linspace(0, 5, 50)
    y1 = x
    y2 = x**2
    y3 = x**3
    y4 = np.sqrt(x)
    fig, ax = tufte.line(
        x, [y1, y2, y3, y4],
        labels=['linear', 'quadratic', 'cubic', 'sqrt'],
        title='Multiple Functions'
    )


def test_line_04():
    """Line with markers"""
    x = np.linspace(0, 10, 20)
    y = np.sin(x) + np.random.normal(0, 0.1, 20)
    fig, ax = tufte.line(x, y, markers=True, title='Line with Markers')


def test_line_05():
    """Noisy data"""
    x = np.linspace(0, 100, 1000)
    y = np.sin(x/10) + np.random.normal(0, 0.5, 1000)
    fig, ax = tufte.line(x, y, title='Noisy Signal')


def test_line_06():
    """Decreasing trend"""
    x = np.linspace(0, 10, 100)
    y = 10 * np.exp(-x/3)
    fig, ax = tufte.line(x, y, title='Exponential Decay')


def test_line_07():
    """Flat line (constant)"""
    x = np.linspace(0, 10, 50)
    y = np.ones_like(x) * 5
    fig, ax = tufte.line(x, y, title='Constant Value')


def test_line_08():
    """Very few points (3 points)"""
    x = [0, 5, 10]
    y = [1, 3, 2]
    fig, ax = tufte.line(x, y, markers=True, title='Very Few Points')


def test_line_09():
    """Discontinuous data (NaN values)"""
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    y[40:60] = np.nan  # Create gap
    fig, ax = tufte.line(x, y, title='Discontinuous Data')


# ==============================================================================
# SCATTER PLOT TESTS
# ==============================================================================

def test_scatter_01():
    """Simple linear correlation"""
    x = np.random.randn(200)
    y = 2*x + np.random.randn(200)
    fig, ax = tufte.scatter(x, y, title='Linear Correlation', xlabel='X', ylabel='Y')


def test_scatter_02():
    """No correlation (random)"""
    x = np.random.randn(200)
    y = np.random.randn(200)
    fig, ax = tufte.scatter(x, y, title='No Correlation')


def test_scatter_03():
    """Perfect correlation"""
    x = np.linspace(0, 10, 100)
    y = 2*x + 3
    fig, ax = tufte.scatter(x, y, title='Perfect Correlation')


def test_scatter_04():
    """Cluster pattern"""
    cluster1_x = np.random.normal(-2, 0.5, 100)
    cluster1_y = np.random.normal(-2, 0.5, 100)
    cluster2_x = np.random.normal(2, 0.5, 100)
    cluster2_y = np.random.normal(2, 0.5, 100)
    x = np.concatenate([cluster1_x, cluster2_x])
    y = np.concatenate([cluster1_y, cluster2_y])
    fig, ax = tufte.scatter(x, y, title='Two Clusters')


def test_scatter_05():
    """Large dataset (1000 points)"""
    x = np.random.randn(1000)
    y = np.random.randn(1000)
    fig, ax = tufte.scatter(x, y, title='Large Dataset', alpha=0.3)


def test_scatter_06():
    """Small dataset (10 points)"""
    x = np.random.randn(10)
    y = np.random.randn(10)
    fig, ax = tufte.scatter(x, y, title='Small Dataset (n=10)', size=100)


# ==============================================================================
# SCATTER WITH MARGINALS TESTS
# ==============================================================================

def test_scatter_marginals_01():
    """Basic scatter with marginals"""
    x = np.random.randn(200)
    y = 2*x + np.random.randn(200)
    fig, axes = tufte.scatter(x, y, marginals=True, title='With Marginals')
    assert 'main' in axes
    assert 'top' in axes
    assert 'right' in axes


def test_scatter_marginals_02():
    """Scatter with marginals - no correlation"""
    x = np.random.randn(300)
    y = np.random.randn(300)
    fig, axes = tufte.scatter(x, y, marginals=True, title='Marginals - No Correlation')


def test_scatter_marginals_03():
    """Scatter with marginals - different distributions"""
    x = np.random.exponential(2, 200)
    y = np.random.normal(0, 1, 200)
    fig, axes = tufte.scatter(x, y, marginals=True, title='Different Distributions')


# ==============================================================================
# EDGE CASES AND ERROR TESTS
# ==============================================================================

def test_edge_01():
    """Empty array (should fail)"""
    data = np.array([])
    fig, ax = tufte.histogram(data)


def test_edge_02():
    """Single data point"""
    data = np.array([5.0])
    fig, ax = tufte.histogram(data, title='Single Point')


def test_edge_03():
    """All NaN values (should fail)"""
    data = np.array([np.nan, np.nan, np.nan])
    fig, ax = tufte.histogram(data)


def test_edge_04():
    """Mixed NaN and valid values"""
    data = np.array([1, 2, np.nan, 4, 5, np.nan, 7])
    fig, ax = tufte.histogram(data, title='Mixed NaN Values')


def test_edge_05():
    """Infinite values"""
    data = np.array([1, 2, 3, np.inf, 5, 6])
    fig, ax = tufte.histogram(data, title='With Infinity')


def test_edge_06():
    """Mismatched x and y lengths (should fail)"""
    x = np.array([1, 2, 3])
    y = np.array([1, 2, 3, 4, 5])
    fig, ax = tufte.line(x, y)


# ==============================================================================
# MAIN TEST RUNNER
# ==============================================================================

def main():
    """Run all tests and generate report."""
    print("\n" + "="*70)
    print("TUFTE STYLE PLOTS - COMPREHENSIVE TEST SUITE")
    print("="*70)

    # Define all tests
    tests = [
        # Histogram tests
        ("H01", "Normal distribution", test_histogram_01),
        ("H02", "Uniform distribution", test_histogram_02),
        ("H03", "Exponential distribution", test_histogram_03),
        ("H04", "Bimodal distribution", test_histogram_04),
        ("H05", "Small dataset (n=20)", test_histogram_05),
        ("H06", "Large dataset (n=100k)", test_histogram_06),
        ("H07", "Integer data", test_histogram_07),
        ("H08", "Negative values only", test_histogram_08),
        ("H09", "Single value repeated", test_histogram_09),
        ("H10", "Very small range", test_histogram_10),
        ("H11", "Python list input", test_histogram_11),
        ("H12", "Pandas Series input", test_histogram_12),

        # Line plot tests
        ("L01", "Simple sine wave", test_line_01),
        ("L02", "Two lines (sin/cos)", test_line_02),
        ("L03", "Four lines (polynomials)", test_line_03),
        ("L04", "Line with markers", test_line_04),
        ("L05", "Noisy data", test_line_05),
        ("L06", "Exponential decay", test_line_06),
        ("L07", "Flat line (constant)", test_line_07),
        ("L08", "Very few points", test_line_08),
        ("L09", "Discontinuous data (NaN)", test_line_09),

        # Scatter plot tests
        ("S01", "Linear correlation", test_scatter_01),
        ("S02", "No correlation", test_scatter_02),
        ("S03", "Perfect correlation", test_scatter_03),
        ("S04", "Cluster pattern", test_scatter_04),
        ("S05", "Large dataset (n=1000)", test_scatter_05),
        ("S06", "Small dataset (n=10)", test_scatter_06),

        # Scatter with marginals
        ("M01", "Basic marginals", test_scatter_marginals_01),
        ("M02", "Marginals - no correlation", test_scatter_marginals_02),
        ("M03", "Marginals - different distributions", test_scatter_marginals_03),

        # Edge cases
        ("E01", "Empty array (expected fail)", test_edge_01),
        ("E02", "Single data point", test_edge_02),
        ("E03", "All NaN values (expected fail)", test_edge_03),
        ("E04", "Mixed NaN values", test_edge_04),
        ("E05", "Infinite values", test_edge_05),
        ("E06", "Mismatched lengths (expected fail)", test_edge_06),
    ]

    # Run all tests
    results = []
    for test_name, test_desc, test_func in tests:
        result = run_test(test_name, test_desc, test_func)
        results.append(result)

    # Generate report
    print("\n\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)

    passed = sum(1 for r in results if r.passed)
    failed = sum(1 for r in results if not r.passed)
    total = len(results)

    print(f"\nTotal Tests: {total}")
    print(f"Passed: {passed} ({100*passed/total:.1f}%)")
    print(f"Failed: {failed} ({100*failed/total:.1f}%)")

    # Show failed tests
    if failed > 0:
        print("\n" + "="*70)
        print("FAILED TESTS")
        print("="*70)
        for r in results:
            if not r.passed:
                print(f"\n{r.name}: {r.description}")
                print(f"  Error: {r.error}")

    # Show passed tests
    print("\n" + "="*70)
    print("PASSED TESTS")
    print("="*70)
    for r in results:
        if r.passed:
            print(f"✓ {r.name}: {r.description}")

    print("\n" + "="*70)
    print("Test suite complete!")
    print("="*70)

    return results


if __name__ == "__main__":
    results = main()
