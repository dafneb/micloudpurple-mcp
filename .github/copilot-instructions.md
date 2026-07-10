# Copilot Instructions for Python Projects

## General Guidelines

- Follow [PEP 8](https://peps.python.org/pep-0008/) style guide for formatting and naming conventions.
- Add docstring to all functions and classes using [PEP 257](https://peps.python.org/pep-0257/) conventions.
- Prefer list comprehensions and generator expressions for simple data transformations.
- Highlight any vulnerabilities in the solution you provide as well as solutions to those vulnerabilities.

## Imports

- Use absolute imports whenever possible.
- Group imports in the following order: standard library, third-party libraries, local modules.

## Error Handling

- Use exceptions for error handling; avoid returning error codes.
- Always catch specific exceptions, not the base `Exception` class.

## Libraries

- Use `requests` for HTTP calls.
- Use `unittest` for unit testing.
- Use `logging` instead of `print` for debug/info output.
- Use `cryptography` for encryption/decryption locally stored keys, secrets, or API keys.

## Type Hints

- Use type hints for function signatures and class attributes using [PEP 484](https://peps.python.org/pep-0484/).

## Example Function Template

```python
import logging
from typing import List

def process_data(data: List[int]) -> List[int]:
    """
    Processes a list of integers and returns a new list with each value doubled.

    Args:
        data (List[int]): List of integers to process.

    Returns:
        List[int]: Processed list with each value doubled.
    """
    logging.info("Processing data...")
    return [x * 2 for x in data]
```

## Testing Example

```python
import unittest

class TestProcessData(unittest.TestCase):
    def setUp(self) -> None:
        """Set up test fixtures."""
        self.example_data = "test"

    def tearDown(self) -> None:
        """Clean up after tests."""
        self.example_data = None

    def test_process_data(self):
        """Test the process_data function."""
        self.assertEqual(process_data([1, 2, 3]), [2, 4, 6])

    @unittest.skip("Skipping this test case for demonstration purposes")
    def test_skip(self):
        """An example test case that is skipped."""
        self.assertTrue(True)

    def test_example_raises(self):
        """An example test case that raises an exception."""
        with self.assertRaises(ValueError):
            raise ValueError("This is a test exception")
```

## Project-Specific Patterns

- Use `snake_case` for variable, function, and method names.
- Use `CamelCase` for class names.
