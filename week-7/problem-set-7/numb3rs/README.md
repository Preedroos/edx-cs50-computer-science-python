# IPv4 Address Validator

## Overview

This Python script validates an IPv4 address input by the user. It checks if the address follows the correct format and ensures that each byte is within the valid range.

## Features

- **User Input**: Prompts the user to input an IPv4 address.
- **Validation**: Uses regular expressions to verify that the address is in the correct format:
  - The first byte must be between `1` and `255`.
  - Each byte of the address must be a number between `0` and `255`.
  
## How to Use

1. Run the script in your Python environment:

   ```bash
   python script.py
   ```

2. When prompted, enter an IPv4 address:

   ```
   IPv4 Address: <your_input>
   ```

3. The script will print `True` if the address is valid and `False` otherwise.

### Example

```bash
IPv4 Address: 192.168.1.1
True
```

```bash
IPv4 Address: 256.100.50.25
False
```

## License

This project is licensed under the MIT License.