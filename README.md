# sop-test

A small Python project starter with an installable package, command-line entry
point, and tests.

## Requirements

- Python 3.10 or newer

## Set up and run

From the project directory:

```powershell
python -m pip install -e .
python -m sop_test
```

The editable install also makes the `sop-test` command available in the active
environment:

```powershell
sop-test
```

## Test

After the editable install:

```powershell
python -m unittest discover -s tests
```
