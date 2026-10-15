# Histology Collection

Creates separate PowerPoint presentations for stitched red, blue,
and overlay TIFF images.

Each slide contains one image and a title showing its four nearest
parent folders. Common misspellings of "stitched" are supported.

## Installation

```powershell
python -m pip install -r requirements.txt
```

## Usage

1. Edit HISTOLOGY in `make_and_fill_collected_stitched_folder.py`
   to point to your histology folder, then run:

   ```powershell
   python make_and_fill_collected_stitched_folder.py
   ```

2. Edit SOURCE in `stitched_to_powerpoint.py` to point to the
   resulting collected_stitched folder, then run:

   ```powershell
   python stitched_to_powerpoint.py
   ```