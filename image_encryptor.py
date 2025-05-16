from PIL import Image
import sys

def encrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            # Simple operation: invert RGB values
            pixels[i, j] = (255 - r, 255 - g, 255 - b)

    img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path):
    # Since our operation is reversible, we use the same logic
    encrypt_image(input_path, output_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 image_encryptor.py [encrypt|decrypt] input_image output_image")
        sys.exit(1)

    mode, input_image, output_image = sys.argv[1], sys.argv[2], sys.argv[3]
    
    if mode == "encrypt":
        encrypt_image(input_image, output_image)
    elif mode == "decrypt":
        decrypt_image(input_image, output_image)
    else:
        print("Invalid mode. Use 'encrypt' or 'decrypt'.")
