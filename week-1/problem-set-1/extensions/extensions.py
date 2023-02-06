def main():
    # prompts the user for a file name
    file_name = input("File name: ")

    # checks if the file hasn't an extension
    if not "." in file_name:
        print("application/octet-stream")
        return 1

    # splits the file name from its extension(s)
    splitted_list = file_name.split(".")

    # catches the last extension
    extension = splitted_list[len(splitted_list) - 1]

    # turns the extension to lower case and removes additional spaces
    extension = extension.lower().strip()

    # perses the extension to MIME type
    mime = extension_to_mime(extension)

    # outputs the MIME type
    print(mime)


def extension_to_mime(extension: str):
    APPLICATION = ["zip", "pdf"]
    IMAGE = ["gif", "jpg", "jpeg", "png"]

    if extension in IMAGE:
        if extension == "jpg":
            return "image/jpeg"

        return f"image/{extension}"

    if extension == "txt":
        return "text/plain"

    if extension in APPLICATION:
        return f"application/{extension}"

    return "application/octet-stream"


main()
