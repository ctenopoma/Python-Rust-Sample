//! Test suite for fibonacci function
//! These tests verify correctness of the core Rust implementation

#[cfg(test)]
mod tests {
    use python_rust::fibonacci;

    #[test]
    fn test_base_case_zero() {
        assert_eq!(fibonacci(0), 0);
    }

    #[test]
    fn test_base_case_one() {
        assert_eq!(fibonacci(1), 1);
    }

    #[test]
    fn test_known_value_10() {
        assert_eq!(fibonacci(10), 55);
    }

    #[test]
    fn test_known_value_20() {
        assert_eq!(fibonacci(20), 6765);
    }

    #[test]
    fn test_known_value_35() {
        assert_eq!(fibonacci(35), 9227465);
    }

    #[test]
    fn test_maximum_safe_value() {
        assert_eq!(fibonacci(93), 12200160415121876738);
    }
}
