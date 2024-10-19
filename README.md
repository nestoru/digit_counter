# Digit Counter
A Python package that provides a function to determine the number of base-10 digits needed to write the integer part of any given number. Supports all numeric types in Python's standard library, including `int`, `float`, `Decimal`, `Fraction`, and more.

## Project Overview
This repository serves as a guideline for developers joining an opinionated Python team. It is designed to assist individuals who are starting projects from scratch by adhering to our coding standards and best practices. The codebase is fully tested, easily executable, and structured for seamless packaging and distribution.

## Project Structure
```
├── LICENSE
├── MANIFEST.in
├── README.md
├── digit_counter
│   ├── __init__.py
│   ├── counter.py
├── setup.py
└── tests
    ├── __init__.py
    ├── test_counter.py
```

## Prerequisites

Ensure you have Python 3.7 or higher installed on your system.

## Virtual Environment

It's recommended to use an isolated environment to manage dependencies:

```
python3 -m venv venv
source venv/bin/activate
```

## To deactivate and remove the virtual environment:
```
deactivate
rm -rf venv
```

## Install dependencies using pip
```
pip install -r requirements.txt
```

## Building the Package
To install the package:
```
pip install -e .
```

## Usage
You can use the count_digits function in your Python code or via the command line.

1. Importing in Python

Import the count_digits function from the digit_counter package and use it as follows:
```
from digit_counter.counter import count_digits

print(count_digits(100))      # Output: 3
print(count_digits(-10))      # Output: 2
print(count_digits(3.1415))   # Output: 1
```

1. Command-Line Interface (CLI)
You can use the digit-counter command to count digits from the terminal in two ways:

a. Direct Script Execution
Run the script directly using Python:
```
python digit_counter/counter.py <number>
```

Example:
```
python digit_counter/counter.py 100
# Output: 3

python digit_counter/counter.py -10
# Output: 2

python digit_counter/counter.py 3.1415
# Output: 1
```

a. Package-Based Execution
After installing the package, use the digit-counter command directly:
```
digit-counter <number>
```

Example:
```
digit-counter 100
# Output: 3

digit-counter -999
# Output: 3

digit-counter 3.1415
# Output: 1
```

## Testing
Run the tests using pytest:
```
pytest
```

## Linting
Ensure code adheres to PEP 8 standards using flake8:
```
flake8 digit_counter
```

## Formatter
Format the code using black as needed:
```
black digit_counter/counter.py
```

## Generating the requirements file
```
pip install pipreqs
pipreqs .
```
