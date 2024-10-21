# Vanity Plate Validator

## Overview

This Python script validates vanity license plates based on specific rules to ensure they meet the criteria for being considered valid.

## Features

- **Length Check**: Plates must have a minimum of 2 characters and a maximum of 6 characters.
- **Letter Requirement**: Plates must start with at least two letters.
- **Number Placement**: 
  - The first number cannot be '0'.
  - Numbers must appear at the end of the plate if present (no numbers in the middle).

## How to Use

1. Run the script.
2. Enter a vanity plate when prompted.
3. The script will output whether the plate is "Valid" or "Invalid" based on the established criteria.

### Example

```
Plate: ABC123
Valid

Plate: A12
Invalid

Plate: 123AB
Invalid

Plate: AB1234
Valid

Plate: AB0
Invalid
```

## License

This project is licensed under the MIT License.