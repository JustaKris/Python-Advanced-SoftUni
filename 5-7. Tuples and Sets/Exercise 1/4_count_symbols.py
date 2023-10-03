string = input()

symbols_dict = {}
for symbol in string:
    if symbol not in symbols_dict.keys():
        symbols_dict[symbol] = 1
    else:
        symbols_dict[symbol] += 1

for symbol, occurrences in sorted(symbols_dict.items()):
    print(f"{symbol}: {occurrences} time/s")
