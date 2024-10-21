# CSV Table Viewer

## Overview

This Python script reads a specified CSV file and displays its contents in a well-formatted table using the `tabulate` library. It ensures proper argument handling and validates the input file.

## Features

- **Command-Line Argument Handling**: 
  - Exits with an error message if no arguments are provided or if more than one argument is supplied.
- **CSV File Validation**: 
  - Checks if the provided file has a `.csv` extension.
  - Verifies that the specified file exists before attempting to read it.
- **Table Formatting**: 
  - Uses the `tabulate` library to display the CSV data in a grid format.

## How to Use

1. Run the script from the command line, providing the path to a CSV file as an argument:

   ```bash
   python script.py <path_to_csv_file>
   ```

2. The script will output the contents of the CSV file formatted as a table.

### Example

```bash
python script.py pizzas.csv
```

Output:

```
+----------+---------+----------+
|   Name   |  Size   |  Price   |
+----------+---------+----------+
| Margherita | Medium  | $10.99   |
| Pepperoni  | Large   | $12.99   |
| Veggie     | Small   | $8.99    |
+----------+---------+----------+
```

### Error Messages

- If no arguments are provided:
  ```
  Too few command-line arguments
  ```

- If more than one argument is provided:
  ```
  Too many command-line arguments
  ```

- If the file does not have a `.csv` extension:
  ```
  Not a CSV file
  ```

- If the specified file does not exist:
  ```
  File does not exist
  ```

## Requirements

- `tabulate` library: You can install it using pip:

   ```bash
   pip install tabulate
   ```

## License

This project is licensed under the MIT License.