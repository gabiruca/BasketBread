def leerTransacciones():
    file = open("BasketBread.csv","r").readlines()[1:]
    return [';'.join(line.strip().split(",")) for line in file]


print(leerTransacciones())

