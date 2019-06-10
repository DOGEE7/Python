b = [[0] * 9 for i in range(9)]
for i in range(9):
    for n in range(9):
        b[i][n] = input("验证数独有效性，请输入一个数独，空格用*表示"+'\n')
print(b)

