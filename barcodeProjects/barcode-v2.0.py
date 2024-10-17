from io import BytesIO

from barcode import EAN13
from barcode.writer import ImageWriter

with open("somefile.png", "wb") as f:
        EAN13("123123123115", writer=ImageWriter()).write(f)