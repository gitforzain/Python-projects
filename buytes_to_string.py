hex_string = "7a 61 69 6e"
bytes_data = bytes.fromhex(hex_string)
decoded_string = bytes_data.decode('utf-8')
print("Decoded String:", decoded_string)
