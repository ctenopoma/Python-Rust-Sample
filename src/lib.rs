//! Python-Rust Fibonacci Library.
//!
//! This crate provides an efficient implementation of the Fibonacci sequence
//! using iterative algorithms. It is designed to be exposed to Python via PyO3
//! bindings for high-performance sequence calculations.
//!
//! # Examples
//!
//! ```
//! let result = fibonacci(10);
//! assert_eq!(result, 55);
//! ```

#[allow(unused_imports)]
use pyo3::prelude::*;
