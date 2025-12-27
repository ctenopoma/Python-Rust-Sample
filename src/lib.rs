//! Python-Rust Fibonacci Library.
//!
//! This crate provides an efficient implementation of the Fibonacci sequence
//! using iterative algorithms. It is designed to be exposed to Python via `PyO3`
//! bindings for high-performance sequence calculations.
//!
//! # Examples
//!
//! ```
//! use python_rust::fibonacci;
//! let result = fibonacci(10);
//! assert_eq!(result, 55);
//! ```

#[allow(unused_imports)]
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
/// use python_rust::fibonacci;
///
/// assert_eq!(fibonacci(0), 0);
/// assert_eq!(fibonacci(1), 1);
/// assert_eq!(fibonacci(10), 55);
/// assert_eq!(fibonacci(20), 6765);
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
#[must_use]
pub fn fibonacci(n: u32) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => {
            let (mut a, mut b) = (0, 1);
            for _ in 2..=n {
                let temp = a + b;
                a = b;
                b = temp;
            }
            b
        }
    }
}

