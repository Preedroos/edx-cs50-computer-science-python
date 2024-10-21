# Shirtificate Generator

## Overview

This Python script generates a personalized PDF certificate for completing the CS50 course. The certificate includes a customizable name and an image as a background, creating a visually appealing certificate.

## Features

- **User Input**: Prompts the user to enter their name.
- **PDF Generation**: Creates a PDF file using the FPDF library.
- **Customizable Design**: Adds a personalized message and an image background to the certificate.

## How to Use

1. Ensure you have the `fpdf` library installed. If not, install it using pip:

   ```bash
   pip install fpdf
   ```

2. Place the `shirtificate.png` image in the same directory as the script.

3. Run the script in your Python environment:

   ```bash
   python shirtificate.py
   ```

4. When prompted, enter your name:

   ```
   Name: John Doe
   ```

5. The script will generate a PDF certificate named `shirtificate.pdf` in the same directory.

### Example

```bash
Name: John Doe
```

This will create a `shirtificate.pdf` file with the content:

```
CS50 Shirtificate
John Doe took CS50
```

## License

This project is licensed under the MIT License.