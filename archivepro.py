import os
import zipfile
import argparse


def compress_files(file_paths, output_name):
    """Compress the given files into a zip archive."""
    try:
        with zipfile.ZipFile(output_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in file_paths:
                if os.path.exists(file):
                    zipf.write(file, os.path.basename(file))
                    print(f"Compressed: {file}")
                else:
                    print(f"File not found: {file}")
        print(f"Files successfully compressed into {output_name}")
    except Exception as e:
        print(f"An error occurred: {e}")


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="ArchivePro: Compress files to save space and improve load times.")
    parser.add_argument('files', metavar='F', type=str, nargs='+', help='Files to compress')
    parser.add_argument('-o', '--output', type=str, default='archive.zip', help='Output archive name (default: archive.zip)')
    return parser.parse_args()


def main():
    args = parse_arguments()
    compress_files(args.files, args.output)


if __name__ == "__main__":
    main()