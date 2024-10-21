# Time Converter: 12-hour to 24-hour Format

## Overview

This Python script converts time from a 12-hour format (with AM/PM) to a 24-hour format. It validates the input to ensure it adheres to the expected format before performing the conversion.

## Features

- **User Input**: Prompts the user to input a time range in 12-hour format.
- **Input Validation**: Uses regular expressions to check if the input is correctly formatted.
- **Time Conversion**: Converts valid 12-hour times to 24-hour format.
- **Output**: Displays the converted time range.

## How to Use

1. Run the script in your Python environment:

   ```bash
   python script.py
   ```

2. When prompted, enter a time range in 12-hour format, for example:

   ```
   2:30 PM to 4:15 AM
   ```

3. The script will print the converted time range in 24-hour format:

### Example

```bash
Hours: 2:30 PM to 4:15 AM
00:30 to 16:15
```

```bash
Hours: 12:00 AM to 12:00 PM
00:00 to 12:00
```

### Error Handling

If the input format is incorrect, the script raises a `ValueError`. You can handle this by catching the exception in your own implementation if desired.

## License

This project is licensed under the MIT License.