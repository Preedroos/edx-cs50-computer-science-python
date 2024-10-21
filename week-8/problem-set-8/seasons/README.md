# Age in Minutes Calculator

## Overview

This Python script calculates the number of minutes a person has lived based on their date of birth. It takes a date input in ISO format (YYYY-MM-DD) and outputs the number of minutes since that date in a human-readable format.

## Features

- **User Input**: Prompts the user to enter their date of birth.
- **Date Validation**: Checks if the entered date is valid using the ISO format.
- **Minute Calculation**: Calculates the total number of minutes from the entered birthdate to the current date.
- **Human-Readable Output**: Converts the number of minutes into words for better readability.

## How to Use

1. Ensure you have the `inflect` library installed. If not, install it using pip:

   ```bash
   pip install inflect
   ```

2. Run the script in your Python environment:

   ```bash
   python script.py
   ```

3. When prompted, enter your date of birth in the format YYYY-MM-DD:

   ```
   Date of Birth: 2000-01-01
   ```

4. The script will output the number of minutes you've lived in a human-readable format:

### Example

```bash
Date of Birth: 2000-01-01
11694240 minutes
```

```bash
Date of Birth: invalid-date
```

This will terminate the program with a non-zero exit code due to an invalid date.

## License

This project is licensed under the MIT License.