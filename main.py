from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    dicionario = OrderedDict()
    for num in range(n):
        item = input().split()

        item_name = ' '.join(item[:-1])
        net_price = int(item[-1])

        dicionario[item_name] = dicionario.get(item_name, 0) + net_price

    for item, price in dicionario.items():
        print(f'{item} {price}')
