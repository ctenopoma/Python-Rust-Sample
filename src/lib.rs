//! Python-Rust Fibonacci Library.
//!
//! This crate provides both iterative and recursive implementations of the
//! Fibonacci sequence. The iterative version offers efficient performance,
//! while the recursive version is provided for comparison and educational
//! purposes. Both are exposed to Python via `PyO3` bindings.
//!
//! # Examples
//!
//! ```
//! use python_rust::fibonacci;
//! let result = fibonacci(10);
//! assert_eq!(result, 55);
//! ```

use pyo3::prelude::*;

/// Calculate the nth Fibonacci number using an iterative algorithm.
///
/// This function computes Fibonacci numbers using an efficient iterative
/// approach with O(n) time complexity and O(1) space complexity.
///
/// # Arguments
///
/// * `n` - The position in the Fibonacci sequence (0-indexed). Must be
///   non-negative and ≤ 93 to avoid u64 overflow.
///
/// # Returns
///
/// Returns the nth Fibonacci number as a u64.
///
/// # Examples
///
/// ```
/// use python_rust::fibonacci_iterative;
///
/// assert_eq!(fibonacci_iterative(0), 0);
/// assert_eq!(fibonacci_iterative(1), 1);
/// assert_eq!(fibonacci_iterative(10), 55);
/// assert_eq!(fibonacci_iterative(20), 6765);
/// ```
///
/// # Panics
///
/// In debug builds, panics if n > 93 due to u64 overflow.
/// In release builds, wraps around (produces incorrect results).
///
/// # Note
///
/// The maximum safe input is n = 93, which produces fib(93) = 12,200,160,415,121,876,738.
/// Values beyond this will overflow u64 capacity.
#[pyfunction]
#[must_use]
pub fn fibonacci_iterative(n: u32) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => {
            let (mut a, mut b) = (0_u64, 1_u64);
            for _ in 2..=n {
                let temp = a + b;
                a = b;
                b = temp;
            }
            b
        }
    }
}

/// Calculate the nth Fibonacci number using a naive recursive algorithm.
///
/// This implementation has exponential time complexity O(2^n) and is intended
/// for educational purposes or comparisons with the iterative version.
///
/// # Arguments
///
/// * `n` - The position in the Fibonacci sequence (0-indexed). Must be
///   non-negative and ≤ 93 to avoid u64 overflow.
///
/// # Returns
///
/// Returns the nth Fibonacci number as a u64.
///
/// # Examples
///
/// ```
/// use python_rust::fibonacci_recursive;
///
/// assert_eq!(fibonacci_recursive(0), 0);
/// assert_eq!(fibonacci_recursive(1), 1);
/// assert_eq!(fibonacci_recursive(10), 55);
/// ```
///
/// # Panics
///
/// In debug builds, panics if n > 93 due to u64 overflow.
/// In release builds, wraps around (produces incorrect results).
#[pyfunction]
#[must_use]
pub fn fibonacci_recursive(n: u32) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2),
    }
}

/// Backwards-compatible alias that defaults to the iterative implementation.
#[pyfunction]
#[must_use]
pub fn fibonacci(n: u32) -> u64 {
    fibonacci_recursive(n)
}

/// Python module exposing the Rust Fibonacci function.
///
/// This module provides high-performance Fibonacci calculations to Python
/// through `PyO3` bindings. The Rust functions are exposed as:
/// - `fibonacci` (iterative, backward-compatible)
/// - `fibonacci_iterative`
/// - `fibonacci_recursive`
#[pymodule]
fn python_rust(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fibonacci_iterative, m)?)?;
    m.add_function(wrap_pyfunction!(fibonacci_recursive, m)?)?;
    m.add_function(wrap_pyfunction!(fibonacci, m)?)?;
    Ok(())
}
