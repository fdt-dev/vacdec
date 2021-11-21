#!/usr/bin/env python3

from __future__ import print_function

import sys
import zlib
import pprint

from PIL import Image
import pyzbar.pyzbar
import base45
import cbor2


def vacdecode(data):
    cert = data[0].data.decode()
    b45data = cert.replace("HC1:", "")
    zlibdata = base45.b45decode(b45data)
    cbordata = zlib.decompress(zlibdata)
    decoded = cbor2.loads(cbordata)
    return cbor2.loads(decoded.value[2])


def pprint_vacdec(json_result):
    #pprint.pprint(json_result)
    print(ppformat_vacdec(json_result))


def print_vacdec(json_result):
    print(json_result)


def ppformat_vacdec(json_result):
    return pprint.pformat(json_result)


def decode_image(filename):
    return pyzbar.pyzbar.decode(Image.open(filename))

    
if __name__ == "__main__":
    data = decode_image(sys.argv[1])
    json = vacdecode(data)
    pprint_vacdec(json)
