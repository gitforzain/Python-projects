def binery_to_string(Message):
    bul = Message.split(' ')
    built_in = [chr(int (b , 2))for b in bul]
    built_in2 = '' .join(built_in)
    return built_in2
binery_message = "01110011 01110100 01110010 01101001 01101110 01100111 00100000 01110100 01101111 00100000 01100010 01101001 01101110 01100101 01110010 01111001 00100000 01101101 01100001 01101011 01100101 01110010"
out = binery_to_string(binery_message)
print(out)
