import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Catches the youtube src attribute of an iframe tag
    youtube_url_pattern = r'src="http[s]?://(www\.)?youtube(\.com)?/embed/([a-zA-Z0-9_-]+)"'

    # Returns the youtube video ID
    match = re.search(youtube_url_pattern, s)

    if match:
        video_id = match.group(3)
        return f"https://youtu.be/{video_id}"
    else:
        return None


if __name__ == "__main__":
    main()
