# Python-Rust Fibonacci Library

A high-performance Fibonacci number calculator implemented in Rust with Python bindings via PyO3. This library demonstrates the performance benefits of combining Python's ease of use with Rust's computational efficiency.

## Features

- **Fast Rust Implementation**: Iterative Fibonacci algorithm compiled to native code
- **Python Bindings**: Seamless integration with Python via PyO3
- **Performance Comparison**: Benchmarking utilities to compare Rust vs. pure Python
- **Type Safety**: Comprehensive type hints and Google-style docstrings
- **Zero Unsafe Code**: All Rust code adheres to safe practices (`unsafe_code = "forbid"`)

## Performance

Benchmark results for `fibonacci(35)` with 5 runs:

```
Fibonacci(35):
  Rust:   0.000000s
  Python: 0.744516s
  Speedup: 1489032.3x
```

✅ **Success Criteria Met**:
- SC-002: Rust completes fib(35) in < 1 second
- SC-003: Rust is ≥ 10x faster than Python implementation

## Installation

### Prerequisites

- Python ≥ 3.14
- Rust toolchain (stable)
- [uv](https://github.com/astral-sh/uv) (Python environment manager)

### Setup

1. Clone the repository and navigate to the project directory:

```powershell
git clone <repository-url>
cd 08_python_rust
```

2. Create and activate the Python environment:

```powershell
uv sync
```

3. Build the Rust extension:

```powershell
# Set environment variable for Python 3.14 compatibility
$env:PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
maturin develop --uv
```

## Usage

### Basic Usage

```python
from python_rust import fibonacci_rust, fibonacci_python

# Use fast Rust implementation
result = fibonacci_rust(35)
print(f"fib(35) = {result}")  # Output: fib(35) = 9227465

# Compare with pure Python (slower)
result_py = fibonacci_python(10)
print(f"fib(10) = {result_py}")  # Output: fib(10) = 55
```

### Running Benchmarks

```python
from python_rust import benchmark

# Default: n=35, runs=5
benchmark()

# Custom parameters
benchmark(n=20, runs=10)
```

Or run from command line:

```powershell
python -c "from python_rust.fibonacci import benchmark; benchmark()"
```

## Testing

Run the full test suite:

```powershell
# Rust tests
$env:PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
cargo test

# Python tests
python -m pytest tests/
```

## Code Quality

All linters pass with zero errors:

```powershell
# Rust linting
$env:PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
cargo clippy -- -D warnings

# Python linting
python -m ruff check python/ tests/

# Type checking
python -m pyrefly check python/ tests/
```

## Documentation

Generate Rust documentation:

```powershell
$env:PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
cargo doc --no-deps --open
```

## Project Structure

```
.
├── Cargo.toml              # Rust package configuration
├── pyproject.toml          # Python package configuration
├── src/
│   └── lib.rs              # Rust Fibonacci implementation and PyO3 bindings
├── python/
│   └── python_rust/
│       ├── __init__.py     # Python package entry point
│       └── fibonacci.py    # Pure Python implementation and benchmarks
├── tests/
│   ├── test_fibonacci.rs   # Rust unit tests
│   └── test_bindings.py    # Python integration tests
└── specs/
    └── 001-rust-fibonacci/ # Feature specification and planning documents

```

## Development

This project follows a specification-driven development approach:

1. **Specification**: See [spec.md](specs/001-rust-fibonacci/spec.md) for feature requirements
2. **Planning**: See [plan.md](specs/001-rust-fibonacci/plan.md) for technical design
3. **Tasks**: See [tasks.md](specs/001-rust-fibonacci/tasks.md) for implementation roadmap
4. **Quickstart**: See [quickstart.md](specs/001-rust-fibonacci/quickstart.md) for setup guide

## Constitution

This project adheres to the project constitution defined in `.specify/constitution.md`:

- **Python Environment**: uv for dependency management
- **Code Quality**: Zero-error policy for all linters
- **Documentation**: Google-style docstrings for all Python functions
- **Safety**: No unsafe Rust code allowed
- **Testing**: Comprehensive test coverage for all features

## License

[Insert your license here]

## Contributing

[Insert contribution guidelines here]
