white_square = '\u25A0'
black_square = '\u25A1'

print(white_square)
print(black_square)

for row in range(0,8):
    for col in range(8):
        if (row + col) % 2 == 0:
            print(white_square,end=' ')
        else:
            print(black_square,end=' ')
    print() 