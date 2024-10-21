# Bitcoin Value Converter

## Overview

This Python script converts a specified amount of Bitcoin to its equivalent value in USD, using real-time data from the CoinDesk API.

## Features

- **Real-Time Bitcoin Price**: The script fetches the current Bitcoin price in USD from the CoinDesk API.
- **Command-Line Input**: The user provides the amount of Bitcoin via the command line.
- **Error Handling**: The script manages potential issues, such as missing or invalid input, and problems with the API request.

## Requirements

- **Python 3.x**
- **requests library** (install using `pip`)

### Installing the `requests` Library

```bash
pip install requests
```

## How to Use

1. Run the script from the command line, providing the amount of Bitcoin as an argument:

```bash
python script.py <btc_amount>
```

Example:

```bash
python script.py 0.5
```

2. The script will fetch the current Bitcoin price and output the value of the specified Bitcoin amount in USD.

### Example Output

```
$17,234.6500
```

### Error Handling

- If no argument is provided, the script exits with:
  ```
  Missing command-line argument
  ```
- If the argument is not a valid number, the script exits with:
  ```
  Command-line argument is not a number
  ```

## License

This project is licensed under the MIT License.