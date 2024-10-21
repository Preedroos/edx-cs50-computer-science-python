# Text Formatter with PyFiglet

## Overview

This Python script allows users to transform input text into stylish ASCII art using the `pyfiglet` library. The user can either select a specific font from the available options or let the program choose a random font to display the text.

## Features

- **Customizable Fonts**: Users can specify a font using the `-f` or `--font` flag followed by the font name.
- **Random Font Selection**: If no font is specified, a random font is selected from the list of available fonts.
- **Error Handling**: The script provides feedback for invalid font names or incorrect usage.
- **ASCII Art Output**: The script generates and prints text in ASCII art style using the `pyfiglet` library.

## Requirements

- **Python 3.x**
- **pyfiglet library** (install using `pip`)

### Installing the `pyfiglet` Library

To use this script, you need to install the `pyfiglet` library. You can do so by running the following command:

```bash
pip install pyfiglet
```

## How to Use

### Basic Usage (Random Font)

Run the script without any arguments, and it will display the input text using a random font:

```bash
python script.py
```

You will be prompted to enter text, and the output will be displayed using a randomly selected font.

Example:

```
Input: Hello World
Output (random font):
 _   _      _ _         __        __         _     _ _ 
| | | | ___| | | ___    \ \      / /__  _ __| | __| | |
| |_| |/ _ \ | |/ _ \    \ \ /\ / / _ \| '__| |/ _` | |
|  _  |  __/ | | (_) |    \ V  V / (_) | |  | | (_| |_|
|_| |_|\___|_|_|\___( )    \_/\_/ \___/|_|  |_|\__,_(_)
                 |__/                                  
```

### Specifying a Font

To specify a font, use the `-f` or `--font` flag followed by the font name:

```bash
python script.py -f <fontname>
```

Example:

```bash
python script.py -f slant
```

You will be prompted to enter text, and the output will be displayed using the specified font.

Example:

```
Input: Hello
Output (slant font):
    __    __     _ __       
   / /_  / /_   (_) /____   
  / __ \/ __ \ / / __/ _ \  
 / / / / / / // / /_/  __/  
/_/ /_/_/ /_//_/\__/\___/   
                            
```

### Invalid Usage

If you provide incorrect arguments, the script will exit with a message like:

- If you pass more than 2 arguments or only 1 argument:
  ```
  Invalid usage
  ```

- If you provide an invalid font name:
  ```
  Invalid font
  ```

## Command-Line Arguments

- **No arguments**: The script will choose a random font for the input text.
- **`-f` or `--font`**: This flag allows the user to specify a font for the text.

### Example with a Specific Font

```bash
python script.py --font banner
```

Example output:

```
Input: Test
Output (banner font):
######                 #     #                
#     # ######  ####   ##   ##  ####   ###### 
#     # #      #       # # # # #       #      
######  #####   ####   #  #  #  ####   #####  
#   #   #           #  #     #      #  #      
#    #  #      #    #  #     # #    #  #      
#     # ######  ####   #     #  ####   ###### 
```

## Code Explanation

```python
from pyfiglet import Figlet
import random
import sys
```
- **Imports**: The script imports `pyfiglet.Figlet` for text-to-ASCII conversion, `random` to pick a random font, and `sys` to handle command-line arguments.

```python
def main(args):
    fonts = Figlet().getFonts()
    if len(args) > 2 or len(args) == 1:
        sys.exit("Invalid usage")
```
- **Argument validation**: If the user provides more than 2 arguments or only 1, the program exits with an "Invalid usage" message.

```python
    if len(args) == 2:
        if not args[0] == "-f" and not args[0] == "--font":
            sys.exit("Invalid usage")
        if not args[1] in fonts:
            sys.exit("Invalid font")
```
- **Font validation**: If the `-f` or `--font` flag is used, the program checks if the font name provided is valid.

```python
    text = input("Input: ")
    if len(args) == 0:
        figlet = Figlet(font=random.choice(fonts))
    else:
        figlet = Figlet(font=args[1])
    print(figlet.renderText(text))
```
- **Main logic**: If no font is provided, the script selects a random font. Otherwise, it uses the specified font to render the text.

## License

This project is licensed under the MIT License.