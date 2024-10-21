# Date Parser Application

## Overview

This Python script prompts the user to input a date and converts it into a standardized format (`YYYY-MM-DD`). It supports two input formats:

1. Numerical format: `MM/DD/YYYY`
2. Written format: `Month Day, Year` (e.g., `January 1, 2020`)

After receiving the input, the program validates the date and displays it in the `YYYY-MM-DD` format.

## Features

- **Input Parsing**: The script can parse dates in both numerical and written formats.
- **Date Validation**: It ensures that the input date has valid month, day, and year values before formatting.
- **Standard Output**: Once validated, the date is printed in a standardized format: `YYYY-MM-DD`.

## How to Use

1. Run the script.
2. Enter a date in one of the following formats:
   - `MM/DD/YYYY` (e.g., `12/25/2023`)
   - `Month Day, Year` (e.g., `December 25, 2023`)
3. If the date is valid, the script will display the date in the `YYYY-MM-DD` format.
4. If the date is invalid, the program will ask for input again.

### Example Usage

```
Date: 12/25/2023
Output: 2023-12-25

Date: December 25, 2023
Output: 2023-12-25
```

## Functions

### `main()`
- The main loop that takes user input and attempts to parse and validate the date. If the date is valid, it prints the standardized date and exits the loop.

### `parse_date(date)`
- Parses the user input depending on the format. It returns a tuple `(month, day, year)` if successful, otherwise `False`.

### `validate_date(month, day, year)`
- Validates the month, day, and year to ensure that:
  - The month is between 1 and 12.
  - The day is between 1 and 31.
  - The year is non-negative.

## Error Handling

- If the input format is incorrect or contains invalid data (e.g., invalid month or day), the program will silently catch the error and ask for a new input without breaking.

## Requirements

- Python 3.x

