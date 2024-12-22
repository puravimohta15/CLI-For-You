import os
import sys
import base64
import logging
import argparse
from typing import Union
from pathlib import Path
from PIL import Image
from pyzbar.pyzbar import decode as decode_qr

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

def is_base64(data: bytes) -> bool:
    try:
        return data == base64.b64encode(base64.b64decode(data, validate=True))
    except Exception:
        return False

def bin_to_bytes(bin_str: str) -> bytes:
    bin_str = ''.join(bin_str.split())
    if not all(c in '01' for c in bin_str):
        raise ValueError("Invalid binary string")
    return bytes(int(bin_str[i:i+8], 2) for i in range(0, len(bin_str), 8))

def decode_qr_code(img_path: Union[str, Path]) -> bytes:
    try:
        img = Image.open(img_path)
        qr = decode_qr(img)
        if not qr:
            raise ValueError("No QR code found")
        return qr[0].data
    except Exception as e:
        raise ValueError(f"Error loading image: {e}")

def process_data(data: bytes, bin_mode: bool) -> bytes:
    try:
        txt = data.decode('ascii')
        if all(c in '01 \n' for c in txt):
            return bin_to_bytes(txt)
    except UnicodeDecodeError:
        pass

    if is_base64(data):
        try:
            decoded = base64.b64decode(data)
            txt = decoded.decode('ascii')
            return bin_to_bytes(txt) if all(c in '01 \n' for c in txt) else decoded
        except (UnicodeDecodeError, ValueError):
            pass
    return data

def write_output(data: bytes, out_path: Union[str, Path], bin_mode: bool) -> None:
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    mode, write_data = ('wb', data) if bin_mode else ('w', data.decode('utf-8'))
    try:
        with open(out_path, mode) as f:
            f.write(write_data)
        log.info(f"Output written to {out_path}")
    except Exception as e:
        raise IOError(f"Error writing file: {e}")

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="QR Code Decoder")
    p.add_argument('-i', '--input', required=True, help="Input image path")
    p.add_argument('-o', '--output', required=True, help="Output file path")
    p.add_argument('-b', '--binary', action='store_true', help="Binary output mode")
    p.add_argument('-v', '--verbose', action='store_true', help="Verbose logging")
    return p.parse_args()

def main() -> int:
    """Main function."""
    args = parse_args()
    if args.verbose:
        log.setLevel(logging.DEBUG)

    try:
        qr_data = decode_qr_code(args.input)
        processed = process_data(qr_data, args.binary)
        write_output(processed, args.output, args.binary)
        return 0
    except Exception as e:
        log.error(f"Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
