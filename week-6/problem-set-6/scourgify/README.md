# CSV Name Rearranger

## Overview

This Python script reads a specified CSV file containing names in a "last, first" format and writes the rearranged names to a new CSV file in a "first, last" format, along with an additional "house" column. It ensures proper argument handling and validates the input file.

## Features

- **Command-Line Argument Handling**: 
  - Exits with an error message if fewer than two arguments are provided or if more than two arguments are supplied.
- **CSV File Validation**: 
  - Checks if the provided input file has a `.csv` extension.
  - Verifies that the specified input file exists before attempting to read it.
- **Data Rearrangement**: 
  - Rearranges names from "last, first" to "first, last" format and saves them in a new CSV file.

## How to Use

1. Run the script from the command line, providing the path to the input CSV file and the desired output CSV file as arguments:

   ```bash
   python script.py <input_csv_file> <output_csv_file>
   ```

2. The script will output a new CSV file with names rearranged.

### Example

```bash
python script.py names.csv rearranged_names.csv
```

### Input CSV Format

The input CSV file should have the following format:

```
name,house
Doe, John,Gryffindor
Smith, Jane,Hufflepuff
```

### Output CSV Format

The output CSV file will be formatted as follows:

```
first,last,house
John,Doe,Gryffindor
Jane,Smith,Hufflepuff
```

### Error Messages

- If fewer than two arguments are provided:
  ```
  Too few command-line arguments
  ```

- If more than two arguments are provided:
  ```
  Too many command-line arguments
  ```

- If the input file does not have a `.csv` extension:
  ```
  Not a CSV file
  ```

- If the specified input file does not exist:
  ```
  File does not exist
  ```

## License

This project is licensed under the MIT License.