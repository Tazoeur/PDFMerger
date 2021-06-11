# PDF Merger

Simple script to generate a PDF from a folder containing images.

## Usage

```
PDF Merger

Usage:
    merge <image-folder> <file-name>

Arguments:
    <image-folder>      The folder containing the images you want to merge as a PDF.
    <file-name>         The name you want for your PDF file.

Options:
    -h --help           Show this screen.
```

## Installation

I recommend using a python virtual environment.

```bash
git clone git@github.com:Tazoeur/PDFMerger.git /opt/scripts/pdfmerger
cd /opt/scripts/pdfmerger
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

You can add the bash script to your bash aliases

```bash
echo "alias pdfmerge=\"/opt/scripts/pdfmerger/pdfmerger.sh\"" >> ~/.bashrc
```

