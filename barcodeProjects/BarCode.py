# First install python barcode module

from barcode import EAN13
from barcode.writer import ImageWriter

# Write programs that ask the user how many barcodes they need to generate.

num_of_barcodes = int(input("How many Barcodes you need? "))

numbers = range(num_of_barcodes)

for i in numbers:
    id = input("Give 12-Digit numbers for your barcode id: ")
    my_code = EAN13(id, writer=ImageWriter)
    name = input("Give the name to save barcode: ")
    my_code.save(name)


