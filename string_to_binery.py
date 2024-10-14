def string_to_binery(Message):
    built_in_fun = ' ' .join(format (ord (chr), '08b')for chr in Message)
    return built_in_fun
message = "string to binery maker"
out = string_to_binery(message)
print(out)