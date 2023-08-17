text = open('ch7.bin','rb').read()

i = -100
while i < 100:
    print(''.join([chr(ord(c) - i) for c in text]))
    i += 1

# Flag = Yolaihu
