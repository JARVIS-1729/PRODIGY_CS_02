Task 02: Pixel-Manipulation Image Encryptor

A Command Line Interface (CLI) tool designed to encrypt and decrypt images at the byte level. Initially vulnerable to the "ECB Flaw" (where visual patterns remain intact), the architecture was upgraded to a Stream Cipher.

Concept: Pseudo-Random Number Generators (PRNG), Seeded Cryptography, and XOR (^) operations.

Features:

Flattens 2D image matrices into 1D bytearrays for high-speed processing.

Uses the user's password as a cryptographic seed to generate unique XOR keys for every individual pixel, completely obliterating visual patterns into pure static.

Tech Stack: Python, Pillow (PIL), argparse, os
