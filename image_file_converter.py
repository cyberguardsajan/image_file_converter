from PIL import Image

def main():
    # User input
    input_path = input("Enter the file name of the image (with extension): ")
    output_format = input("Change format to (e.g., JPEG, PNG, BMP): ").upper()
    output_name = input("Enter file name for the converted image")
    output_path = output_name+"."+output_format.lower()

    # Validate output format
    valid_formats = ['JPEG', 'PNG', 'BMP', 'GIF']
    if output_format not in valid_formats:
        print(f"Invalid format. Please choose from: {', '.join(valid_formats)}")
        return

    # Perform conversion
    convert_image(input_path, output_path, output_format)


def convert_image(input_path, output_path, output_format):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format=output_format)
        print(f"Image successfully converted to {output_format} format and saved at {output_path}.")
        print(output_path)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
