# CLAUDE.md - AI Assistant Guide for tufte_style_plots

**Last Updated:** 2025-11-18
**Project Owner:** Bobak Farzin
**License:** MIT

## Project Overview

`tufte_style_plots` is a Python library for creating minimalist, data-focused visualizations following Edward Tufte's principles of data visualization. The project emphasizes:

- **Data-ink ratio maximization**: Remove chart junk, focus on data
- **Minimalist design**: Clean, elegant plots without unnecessary decorations
- **Clarity and precision**: Clear communication of quantitative information
- **Integration with popular plotting libraries**: Likely matplotlib/seaborn compatible

## Repository Structure

```
tufte_style_plots/
├── .git/               # Git version control
├── .gitignore          # Python-specific gitignore (comprehensive)
├── LICENSE             # MIT License (2025, Bobak Farzin)
├── README.md           # Project README (minimal currently)
└── CLAUDE.md           # This file - AI assistant guide
```

### Expected Future Structure

As development progresses, the repository will likely evolve to:

```
tufte_style_plots/
├── tufte_style_plots/  # Main package directory
│   ├── __init__.py
│   ├── core.py         # Core plotting functionality
│   ├── styles.py       # Tufte style configurations
│   ├── utils.py        # Helper utilities
│   └── examples/       # Example plots and usage
├── tests/              # Test suite (pytest recommended)
│   ├── __init__.py
│   └── test_*.py
├── docs/               # Documentation
├── examples/           # Usage examples and notebooks
├── setup.py or pyproject.toml  # Package configuration
├── requirements.txt or poetry.lock  # Dependencies
└── .github/            # GitHub workflows (CI/CD)
```

## Development Status

**Current State:** Initial repository setup - no code yet

The repository contains:
- Standard Python .gitignore (supports pip, poetry, uv, pdm, pixi, etc.)
- MIT License
- Minimal README

**Next Steps for Development:**
1. Create package structure
2. Define core plotting API
3. Implement Tufte style presets
4. Add examples and documentation
5. Set up testing framework
6. Configure CI/CD

## Technology Stack

### Current
- Python (version TBD)
- Git for version control

### Expected Dependencies
- **matplotlib**: Core plotting library (likely)
- **numpy**: Numerical operations
- **pandas**: Data handling (optional)
- **seaborn**: Additional plotting utilities (optional)

### Development Tools
- **pytest**: Testing framework (recommended)
- **black** or **ruff**: Code formatting
- **mypy**: Type checking (if using type hints)
- **sphinx**: Documentation generation

## Development Workflows

### Git Branch Strategy

**Current Branch:** `claude/claude-md-mi4m04cw7d367odp-01LDoCvKjSiFrqvtXikpBDfK`

All development should occur on branches prefixed with `claude/` and ending with the session ID to ensure proper authentication.

### Commit Conventions

Follow conventional commits for clarity:
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `test:` Test additions/modifications
- `refactor:` Code refactoring
- `style:` Code style changes (formatting)
- `chore:` Maintenance tasks

Example: `feat: add minimalist bar chart style`

### Git Operations

**Pushing changes:**
```bash
git push -u origin <branch-name>
```
- Branch names MUST start with 'claude/' and end with session ID
- Retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s) on network errors

**Fetching/pulling:**
```bash
git fetch origin <branch-name>
git pull origin <branch-name>
```
- Same retry policy applies

## Code Conventions

### Python Style Guidelines

1. **PEP 8 Compliance**: Follow Python's official style guide
2. **Type Hints**: Use type hints for better code clarity (Python 3.7+)
   ```python
   def create_tufte_plot(data: np.ndarray, title: str) -> plt.Figure:
       ...
   ```
3. **Docstrings**: Use Google or NumPy style docstrings
   ```python
   def minimize_chartjunk(ax: plt.Axes) -> None:
       """Remove unnecessary chart elements following Tufte principles.

       Args:
           ax: The matplotlib Axes object to modify.
       """
   ```
4. **Formatting**: Use black or ruff for consistent formatting
5. **Line Length**: 88-100 characters (black default) or 79 (PEP 8)

### Code Organization

1. **Separation of Concerns**: Keep plotting logic, styling, and utilities separate
2. **DRY Principle**: Avoid code duplication
3. **Single Responsibility**: Each function should do one thing well
4. **Naming Conventions**:
   - Functions/methods: `snake_case`
   - Classes: `PascalCase`
   - Constants: `UPPER_SNAKE_CASE`
   - Private members: `_leading_underscore`

### Testing Conventions

1. **Test Coverage**: Aim for >80% code coverage
2. **Test Naming**: `test_<function>_<scenario>_<expected_result>`
   ```python
   def test_minimize_chartjunk_removes_spines():
       ...
   ```
3. **Test Organization**: Mirror the package structure in `tests/`
4. **Fixtures**: Use pytest fixtures for common test data

## Tufte Design Principles to Implement

When developing features, adhere to Edward Tufte's principles:

1. **Minimize Non-Data Ink**
   - Remove grid lines or make them very light
   - Eliminate unnecessary borders
   - Remove decorative elements

2. **Maximize Data-Ink Ratio**
   - Focus visualization on the data itself
   - Every visual element should convey information

3. **Remove Chart Junk**
   - No 3D effects
   - No unnecessary colors
   - No redundant labels
   - Simplify axes

4. **Use Small Multiples**
   - Support for panel/facet plots
   - Consistent scales for comparison

5. **Integrate Graphics and Text**
   - Direct labeling when possible
   - Minimize need for legends

6. **Show Data Variation**
   - Emphasize actual data points
   - Use range frames instead of full boxes

## Common Tasks for AI Assistants

### Adding New Plot Types

1. Create function in appropriate module (e.g., `tufte_style_plots/core.py`)
2. Apply Tufte styling principles
3. Add comprehensive docstring with examples
4. Write unit tests in `tests/`
5. Add usage example to `examples/`
6. Update documentation

### Modifying Styles

1. Update style configurations in `tufte_style_plots/styles.py`
2. Ensure backward compatibility
3. Test with existing examples
4. Document changes in docstrings and CHANGELOG

### Adding Dependencies

1. Update `requirements.txt` or `pyproject.toml`
2. Document why the dependency is needed
3. Check for license compatibility (MIT-compatible)
4. Update documentation with new capabilities

### Running Tests

```bash
# Once test infrastructure is set up
pytest tests/
pytest tests/ -v  # Verbose output
pytest tests/ --cov=tufte_style_plots  # With coverage
```

### Building Documentation

```bash
# Once Sphinx is configured
cd docs/
make html
```

## Security and Best Practices

1. **No Credentials in Code**: Never commit API keys, tokens, or passwords
2. **Input Validation**: Validate user inputs to prevent errors
3. **Dependencies**: Keep dependencies updated for security patches
4. **Type Safety**: Use type hints and mypy for type checking
5. **Error Handling**: Provide clear, helpful error messages

## Package Distribution

When ready for distribution:

1. **Version Management**: Use semantic versioning (MAJOR.MINOR.PATCH)
2. **PyPI Publishing**: Package for distribution via pip
3. **Documentation**: Host on Read the Docs or GitHub Pages
4. **Changelog**: Maintain CHANGELOG.md for version history
5. **Release Process**:
   - Update version number
   - Update CHANGELOG
   - Create git tag
   - Build distribution: `python -m build`
   - Upload to PyPI: `twine upload dist/*`

## Resources and References

### Edward Tufte's Work
- "The Visual Display of Quantitative Information"
- "Envisioning Information"
- "Visual Explanations"
- "Beautiful Evidence"

### Python Visualization
- Matplotlib documentation: https://matplotlib.org/
- Seaborn documentation: https://seaborn.pydata.org/
- Python Graph Gallery: https://python-graph-gallery.com/

### Related Projects
- `matplotlib-tufte`: Existing Tufte-style implementations
- `tufte-css`: Web-based Tufte styling (for inspiration)
- `ggtufte`: R's ggplot2 Tufte theme

## Notes for AI Assistants

1. **Proactive Planning**: Use TodoWrite for multi-step tasks
2. **Test-Driven Development**: Write tests alongside features
3. **Documentation-First**: Document as you code, not after
4. **Incremental Commits**: Make small, focused commits with clear messages
5. **Ask for Clarification**: When implementation details are ambiguous, ask the user
6. **Style Consistency**: Maintain consistent code style throughout
7. **Performance Considerations**: Consider performance for large datasets
8. **Matplotlib Integration**: Ensure compatibility with standard matplotlib workflows
9. **Backward Compatibility**: Avoid breaking changes without major version bump
10. **User Experience**: API should be intuitive and well-documented

## Current Development Session

**Branch:** `claude/claude-md-mi4m04cw7d367odp-01LDoCvKjSiFrqvtXikpBDfK`
**Last Commit:** `a8f05bf Initial commit`
**Working Directory Status:** Clean

---

This document should be updated as the project evolves to reflect new conventions, structures, and workflows. AI assistants should read this file at the beginning of each session to understand the current state and conventions of the project.
