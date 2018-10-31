# QRcode
QRcode is a python library which generates qrcode images for the data of different types.

## Todos
> List of Tasks to be done

* [x] Data Analysis
* [ ] Data Encoding Modes
    - [x] Numeric
    - [x] Alphaneumeric
    - [x] Byte
    - [ ] Kanji
* [ ] Error Correction Part
 (Areas to understand)
    * Reed Solomon process
    * Polynomial Long Division
    * Galois Field Arithematic
* [ ] Structuring Final Message ( Interleaving  process)
* [ ] Placing Data in QR code
    - [ ] placing function patterns and data bits
    - [ ] add the finder patterns and separators
    - [ ] add alignment pattern
    - [ ] add timing pattern
    - [ ] add data bits to QR
    - [ ] add Dark modules and Reserved areas
* [ ] Apply Mask pattern to data and error correction bits
* [ ] Create Format and Version strings
:tada:

## Usage
 * ` cd ` to the root folder.
 * Currently to test we add the data in the `test.py`.Here:
 ```
 obj.create('<place your data here>')

> Eg. obj.create('Hello, World!')

```
* Run `python test.py`


## References
[QRcode Tutorial](https://thonky.com/qr-code-tutorial/) 