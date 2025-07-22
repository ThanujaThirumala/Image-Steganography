import argparse
from stegano import encode_image, decode_image

def main():
    parser = argparse.ArgumentParser(description="Image Steganography Tool")
    subparsers = parser.add_subparsers(dest='command')

    # Encode command
    encode_parser = subparsers.add_parser('encode')
    encode_parser.add_argument('input_image', help='Path to the input image')
    encode_parser.add_argument('output_image', help='Path to save the encoded image')
    encode_parser.add_argument('message', help='Message to hide')

    # Decode command
    decode_parser = subparsers.add_parser('decode')
    decode_parser.add_argument('input_image', help='Path to the encoded image')

    args = parser.parse_args()

    if args.command == 'encode':
        encode_image(args.input_image, args.output_image, args.message)
        print(f"[+] Message encoded and saved to {args.output_image}")
    elif args.command == 'decode':
        message = decode_image(args.input_image)
        print(f"[+] Hidden Message: {message}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()