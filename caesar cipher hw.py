ori_text = raw_input ("Enter message: ")

ord ('x')

text_to_num = map (ord, ori_text)

def addfour (y): return y + 4

num_plus_four = map (addfour, text_to_num)

chr ()

ciphered_text = map (chr, num_plus_four)

print ori_text
print text_to_num
print num_plus_four
print ciphered_text
