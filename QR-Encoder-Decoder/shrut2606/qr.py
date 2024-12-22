from pyzbar.pyzbar import decode
from PIL import Image
import base64

def decode_qr(image_path, output_file, binary_format):
    """
    Decodes a QR code and saves the content to an output file.

    Args:
        image_path (str): Path to the QR code image.
        output_file (str): Name of the output file with extension.
        binary_format (bool): Whether the output should be written in binary format.
    """
    try:
        # Open the image file
        img = Image.open(image_path)
        # Decode the QR code
        qr_data = decode(img)
        if not qr_data:
            print("No QR code detected in the image.")
            return

        # Extract the data
        data = qr_data[0].data.decode('utf-8')

        # Check if data is base64 encoded
        try:
            decoded_data = base64.b64decode(data)
            re_encoded = base64.b64encode(decoded_data).decode('utf-8')
            is_base64 = data == re_encoded
        except Exception:
            is_base64 = False

        # If base64 encoded, decode it; otherwise, use as-is
        if is_base64:
            print("Detected base64 encoded data.")
            decoded_data = base64.b64decode(data)
        else:
            decoded_data = data.encode()

        # Write data to the output file
        mode = 'wb' if binary_format else 'w'
        with open(output_file, mode) as file:
            file.write(decoded_data if binary_format else decoded_data.decode())

        print(f"Data successfully written to {output_file}.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Take inputs from the user
    image_path = input("Enter the path to the QR code image: ")
    output_file = input("Enter the output file name with extension: ")
    binary_format = input("Is the data binary? (yes/no): ").strip().lower() == 'yes'

    # Decode the QR code
    decode_qr(image_path, output_file, binary_format)
     