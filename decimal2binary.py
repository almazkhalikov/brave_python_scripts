def decimal2binary(x):
    decimal = x
    binary = [0] * x

    i = 0
    while (x > 0):
        binary[i] = x % 2
        x = int(x / 2)
        i += 1

    finale = []
    for j in range(i - 1, -1, -1):
        result = binary[j]
        finale.append(result)

    binary_result = ''.join(map(str, finale))

    print(f"DECIMAL: {decimal}\nBINARY: {binary_result}")


decimal2binary(255)
