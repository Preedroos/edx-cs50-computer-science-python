# Fuel Gauge Program

## Overview

This Python script converts a fraction representing fuel levels into a percentage and displays a corresponding fuel gauge indicator. The gauge shows "E" for empty, "F" for full, and a percentage for levels in between.

## Features

- **Fraction Input**: The user inputs a fraction (e.g., `1/4`).
- **Percentage Conversion**: The script converts the fraction to a percentage, ensuring the numerator does not exceed the denominator.
- **Fuel Gauge Output**: The output varies based on the percentage:
  - **"E"** for empty (0% to <1%)
  - **"F"** for full (99% to 100%)
  - Displays the percentage for any other value.

## How to Use

1. Run the script.
2. Enter a fraction when prompted (format: `numerator/denominator`).
3. The script will display the fuel gauge indicator based on the input fraction.

### Example

```
Fraction: 1/4
25%

Fraction: 0/1
E

Fraction: 4/4
F

Fraction: 3/4
75%
```

## License

This project is licensed under the MIT License.