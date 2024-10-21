# Python File Line Counter

## Overview

This Python script counts the number of non-empty, non-comment lines in a specified Python file. It ensures proper usage and checks for file validity before performing the count.

## Features

- **Command-Line Argument Handling**: 
  - Exits with an error message if no arguments are provided or if more than one argument is supplied.
- **File Validation**: 
  - Checks if the provided file has a `.py` extension.
  - Verifies that the specified file exists.
- **Line Counting**: 
  - Counts lines that are neither empty nor comments.

## How to Use

1. Run the script from the command line, providing the path to a Python file as an argument:

   ```bash
   python script.py <path_to_python_file>
   ```

2. The script will output the count of valid lines in the specified file.

### Example

```bash
python script.py example.py
```

Output:

```
10
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

- If the file does not have a `.py` extension:
  ```
  Not a Python file
  ```

- If the specified file does not exist:
  ```
  File does not exist
  ```

## License

This project is licensed under the MIT License.