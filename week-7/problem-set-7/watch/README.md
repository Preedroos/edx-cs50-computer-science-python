# YouTube Link Extractor

## Overview

This Python script extracts the YouTube video ID from an HTML `<iframe>` tag that embeds a YouTube video. It converts the extracted ID into a standard YouTube URL format.

## Features

- **User Input**: Prompts the user to input an HTML string.
- **Pattern Matching**: Utilizes regular expressions to search for a YouTube embed URL within the provided HTML.
- **Output**: Returns the corresponding YouTube link if a valid embed URL is found.

## How to Use

1. Run the script in your Python environment:

   ```bash
   python script.py
   ```

2. When prompted, enter an HTML string containing a YouTube iframe, for example:

   ```html
   <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>
   ```

3. The script will print the extracted YouTube link:

### Example

```bash
HTML: <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>
https://youtu.be/dQw4w9WgXcQ
```

```bash
HTML: <iframe src="https://www.example.com/embed/dQw4w9WgXcQ"></iframe>
```

Output:

```bash
None
```

## License

This project is licensed under the MIT License.