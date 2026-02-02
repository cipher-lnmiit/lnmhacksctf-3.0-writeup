import zxing
import sys

def decode_qr(image_path):
    reader = zxing.BarCodeReader()
    barcode = reader.decode(image_path)
    
    if barcode:
        print(f"Decoded Flag: {barcode.parsed}")
    else:
        print("Error: Could not decode. Is the header/tail still broken?")

if __name__ == "__main__":
    # This allows you to run: python check_image.py fixed_image.png
    if len(sys.argv) > 1:
        decode_qr(sys.argv[1])
    else:
        print("Please provide the path to the fixed image.")