import base64
import random
import struct
import zlib

if __name__ == '__main__':

    length = 256

    print "Creating {} doubles".format(length)

    random.seed(13)
    values = [random.uniform(-1, 1) for x in xrange(length)]

    print "Total bytes:               {}".format(length * 8)

    packed = struct.pack('<' + ('d' * length), *values)

    print "===================================================================="

    print "Total bytes (packed):      {}".format(len(packed))

    b64 = base64.b64encode(packed)

    print "Total bytes (base64):      {}".format(len(b64))

    print "===================================================================="

    compressed = zlib.compress(packed, 9)

    print "Total bytes (compressed):  {}".format(len(compressed))

    b64 = base64.b64encode(compressed)

    print "Total bytes (base64):      {}".format(len(b64))