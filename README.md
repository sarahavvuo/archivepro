# ArchivePro

ArchivePro is a Python utility designed to help users efficiently archive and compress files on Windows systems to save space and improve load times.

## Features

- Compress multiple files into a single archive.
- Easy-to-use command-line interface.
- Default output name with an option to specify a custom archive name.

## Requirements

- Python 3.x

## Installation

Clone this repository or download the `archivepro.py` file directly to your local machine.

## Usage

Open a terminal and navigate to the directory containing `archivepro.py`. Use the following command to compress files:

```bash
python archivepro.py <file1> <file2> ... -o <output_archive_name>
```

### Arguments

- `file1`, `file2`, ...: The list of files you want to compress.
- `-o`, `--output`: (Optional) Specify the name of the output archive file. If not provided, the default is `archive.zip`.

### Example

To compress `document.txt` and `image.png` into an archive named `my_archive.zip`, use:

```bash
python archivepro.py document.txt image.png -o my_archive.zip
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## Author

Created by [Your Name]

## Disclaimer

This utility is provided as-is without any guarantees or warranties. Use at your own risk.