# 🧠 PRODIGY_CS_02 — Pixel Manipulation for Image Encryption

This is Task 2 of the Cybersecurity track from Prodigy Infotech.

    🔐 A simple yet insightful image encryption tool using pixel-level transformations — built for Cybersecurity Task 2 of the Prodigy InfoTech Internship.

# 📌 Overview

This project demonstrates a beginner-friendly approach to image encryption and decryption using basic pixel manipulation techniques. The goal is to showcase how simple operations at the RGB pixel level can be used to obfuscate image content in a reversible manner.
🖼️ Features

    🔄 Image encryption via pixel color inversion

    🔁 Symmetric decryption using the same transformation

    📷 Compatible with standard image formats (JPEG, PNG)

    🧠 Educational value in understanding low-level image processing

    ⚙️ Lightweight and built with Python and Pillow

# 🔧 How It Works

The script reads each pixel from the input image and inverts its RGB values using the formula:

(R, G, B) → (255 - R, 255 - G, 255 - B)

This transformation is fully reversible, so the same function can be applied again to decrypt the image.

🚀 Usage

# 1. Install dependencies
pip install pillow

#  2. Run the script
python3 image_encryptor.py encrypt input.jpg encrypted.jpg
python3 image_encryptor.py decrypt encrypted.jpg decrypted.jpg

# 📂 File Structure

PRODIGY_CS_02/
├── image_encryptor.py     # Main encryption/decryption script
├── input.jpg              # Sample input image
├── encrypted.jpg          # Encrypted output
├── decrypted.jpg          # Result after decryption
├── README.md              # Project documentation

# 🎯 Learning Outcomes

    Understand how pixel data is stored and manipulated

    Learn basic image processing with Python

    Practice building symmetrical encryption logic

    Improve GitHub collaboration and documentation skills

# 🛡️ Disclaimer

This project is meant for educational purposes only and should not be used in production environments. It does not offer cryptographic security.
