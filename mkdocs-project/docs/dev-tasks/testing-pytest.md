# Development Tasks / Testing / pytest

Python programs can be tested using the `pytest` tool.
See the [pytest installation instructions](../dev-env/pytest/).

See the [pytest documentation](http://doc.pytest.org/en/latest/).

The `pytest` software can also be used to do functional testing on any program.
Need to describe a clean way to regenerate expected results in file, which is then compared with new results,
perhaps similar to TSTool testing features.

## Running pytest

To run pytest, simply run the following in the top-level folder where Python tests exist:

```
$ pytest
```

The pytest software will look for files named `test_*.py` and `*_test.py`.
It will then run functions in the file with names that start with `test_`.

## Simple Example

See the [simple test file](testing-pytest-examples/test_example.py).

## Tests for Function Returned Values

Need to show some examples.

## Test of Program Output With Expected Results in Script

Need to show example.

## Test of Program Output with Expected Results in an Existing File

Need to show example.
