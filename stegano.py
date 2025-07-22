from PIL import Image

def _int_to_bin(rgb):
    return tuple(format(c, '08b') for c in rgb)

def _bin_to_int(rgb_bin):
    return tuple(int(b, 2) for b in rgb_bin)

def encode_image(input_path, output_path, message):
    img = Image.open(input_path)
    if img.mode != 'RGB':
        raise ValueError("Image must be in RGB format.")

    binary_msg = ''.join(format(ord(char), '08b') for char in message)
    binary_msg += '11111110'  # 8-bit EOF marker
    data_index = 0

    pixels = list(img.getdata())
    new_pixels = []

    for pixel in pixels:
        if data_index >= len(binary_msg):
            new_pixels.append(pixel)
            continue

        r_bin, g_bin, b_bin = _int_to_bin(pixel)

        if data_index < len(binary_msg):
            r_bin = r_bin[:-1] + binary_msg[data_index]
            data_index += 1
        if data_index < len(binary_msg):
            g_bin = g_bin[:-1] + binary_msg[data_index]
            data_index += 1
        if data_index < len(binary_msg):
            b_bin = b_bin[:-1] + binary_msg[data_index]
            data_index += 1

        new_pixel = _bin_to_int((r_bin, g_bin, b_bin))
        new_pixels.append(new_pixel)

    img.putdata(new_pixels)
    img.save(output_path)
    # Removed print()

def decode_image(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    binary_msg = ''

    for pixel in pixels:
        for color in pixel[:3]:
            binary_msg += format(color, '08b')[-1]

    # Read 8 bits at a time
    all_bytes = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]

    decoded = ''
    for byte in all_bytes:
        if byte == '11111110':  # EOF marker
            break
        decoded += chr(int(byte, 2))

    # Removed print()
    return decoded