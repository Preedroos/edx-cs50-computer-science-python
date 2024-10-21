# Farewell Program

## Overview

This Python script collects names from user input and prints a farewell message using the `inflect` library. It generates a grammatically correct list of names with proper conjunctions like "and".

## Features

- **Name Collection**: The script allows the user to input multiple names.
- **Grammatically Correct List**: Uses the `inflect` library to create a natural-sounding list of names (e.g., "Adieu, adieu, to Alice, Bob, and Charlie").
- **Exit on Empty Input**: The program stops collecting names when the user submits an empty input.

## Requirements

- **Python 3.x**
- **inflect library** (install using `pip`)

### Installing the `inflect` Library

```bash
pip install inflect
```

## How to Use

1. Run the script.
2. Enter names when prompted.
3. The program will print a farewell message once you submit an empty input.

### Example

```
Name: Alice
Name: Bob
Name: Charlie
Name: 
Adieu, adieu, to Alice, Bob, and Charlie
```

## License

This project is licensed under the MIT License.