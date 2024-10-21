# Email Validator

## Overview

This Python script validates email addresses using the `validator_collection` library. It checks if the input email address is in a valid format.

## Features

- **User Input**: Prompts the user to enter an email address.
- **Email Validation**: Uses the `validators.email` method to check the validity of the entered email address.
- **Error Handling**: Catches exceptions and informs the user if the email address is invalid.

## How to Use

1. Make sure you have the `validator_collection` library installed. If not, install it using pip:

   ```bash
   pip install validator-collection
   ```

2. Run the script in your Python environment:

   ```bash
   python script.py
   ```

3. When prompted, enter an email address, for example:

   ```
   What's your email address? user@example.com
   ```

4. The script will output whether the email address is valid or invalid:

### Example

```bash
What's your email address? user@example.com
Valid
```

```bash
What's your email address? invalid-email
Invalid
```

## License

This project is licensed under the MIT License.