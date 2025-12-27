"""Test Python bindings to Rust Fibonacci function.

This module tests the PyO3 bindings that expose the Rust fibonacci function
to Python as fibonacci_rust.
"""


def test_import_fibonacci_rust():
    """Test that fibonacci_rust can be imported from python_rust module."""
    from python_rust import fibonacci_rust
    
    assert callable(fibonacci_rust)


def test_rust_binding_basic():
    """Test basic functionality of Rust binding with known values."""
    from python_rust import fibonacci_rust
    
    # Test known Fibonacci value
    assert fibonacci_rust(10) == 55


def test_rust_binding_repeated_calls():
    """Test that multiple calls to fibonacci_rust work correctly."""
    from python_rust import fibonacci_rust
    
    # Multiple calls should all return correct values
    assert fibonacci_rust(5) == 5
    assert fibonacci_rust(10) == 55
    assert fibonacci_rust(15) == 610
    assert fibonacci_rust(20) == 6765


def test_rust_binding_base_cases():
    """Test base cases for Fibonacci sequence."""
    from python_rust import fibonacci_rust
    
    # Base cases as defined in Fibonacci sequence
    assert fibonacci_rust(0) == 0
    assert fibonacci_rust(1) == 1
    assert fibonacci_rust(2) == 1
