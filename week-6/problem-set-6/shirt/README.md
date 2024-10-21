# Image Resizer and Shirt Paster

## Overview

This Python script resizes an input image to 600x600 pixels and overlays a predefined shirt image on top of it. The output is saved as a new image file with the same format as the input. It validates input arguments, file types, and ensures the input file exists.

## Features

- **Command-Line Argument Handling**: 
  - Exits with an error message if the number of arguments is less than two or greater than two.
  
- **File Type Validation**: 
  - Checks if the input and output files are in `.jpg`, `.jpeg`, or `.png` formats, case-insensitively.
  - Ensures both input and output files have the same file extension.

- **Image Processing**: 
  - Resizes the input image to 600x600 pixels using the `PIL` (Pillow) library.
  - Overlays a shirt image (`shirt.png`) on top of the resized image.

## How to Use

1. Ensure you have the required `Pillow` library installed:

   ```bash
   pip install pillow
   ```

2. Run the script from the command line, providing the input image file and the desired output image file as arguments:

   ```bash
   python script.py <input_image> <output_image>
   ```

### Example

```bash
python script.py input.jpg output.jpg
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

- If the input or output file does not have a valid extension:
  ```
  Invalid input
  ```

- If the input and output files have different extensions:
  ```
  Input and output have different extensions
  ```

- If the specified input file does not exist:
  ```
  Input does not exist
  ```

## License

This project is licensed under the MIT License.