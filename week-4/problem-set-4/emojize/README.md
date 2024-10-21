# Emoji Input Converter

## Overview

This Python script allows users to input emoji aliases and converts them into actual emoji symbols using the `emoji` library. The user provides input with emoji aliases (e.g., `:smile:`), and the script outputs the corresponding emoji (e.g., 😄).

## Features

- **Convert Emoji Aliases to Emoji Symbols**: The script converts text aliases into emoji using the `emoji` library, which supports the "alias" syntax (e.g., `:heart:` becomes ❤️).
- **User-Friendly Input**: It takes user input, processes it, and immediately outputs the converted emoji.

## Requirements

- **Python 3.x**
- **emoji library** (install using `pip`)

### Installing the `emoji` Library

To use this script, you need to install the `emoji` library. You can do so by running the following command:

```bash
pip install emoji
```

## How to Use

1. Run the script.
2. When prompted, input text with emoji aliases (e.g., `:smile:`, `:heart:`, `:thumbs_up:`).
3. The script will convert the alias into the corresponding emoji and display the result.

### Example Usage

```bash
Input: :smile:
Output: 😄

Input: I :heart: Python!
Output: I ❤️ Python!
```

### Supported Aliases

The script uses the **alias syntax** provided by the `emoji` library. A complete list of supported emoji aliases can be found in the [Emoji Cheat Sheet](https://www.webfx.com/tools/emoji-cheat-sheet/).

## How It Works

- **Input**: The user enters text containing emoji aliases (e.g., `:smile:`).
- **Processing**: The `emoji.emojize()` function converts these aliases into the corresponding emoji characters.
- **Output**: The script prints the text with the emojis in place of the aliases.

## Code Explanation

```python
import emoji

# Prompts the user for input, converts emoji aliases to emojis, and prints the result
print(f"Output: {emoji.emojize(input('Input: '), language='alias')}")
```

- `emoji.emojize()`: This function converts the emoji alias (like `:smile:`) into the actual emoji (😄).
- `input('Input: ')`: Asks the user to enter a string with emoji aliases.
- `print()`: Outputs the converted text, showing the emojis in place of aliases.

## License

This project is licensed under the MIT License.