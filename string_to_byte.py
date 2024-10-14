# a = "zain"
# e = a.encode('utf-8')
# out = ' '.join(format(i, '02x') for i in e)
# print(out)

string = "zain"
bytes_string = string.encode('utf-8')
hex_string = ' '.join(format(byte, '02x') for byte in bytes_string)
print(hex_string)
