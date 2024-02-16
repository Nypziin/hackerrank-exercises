from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    dicionario = OrderedDict()
    for num in range(n):
        item = input().split()

        item_name = ' '.join(item[:-1])
        net_price = int(item[-1])

        if item_name in dicionario:
            dicionario[item_name] += net_price
        else:
            dicionario[item_name] = net_price

    for item, price in dicionario.items():
        print(f'{item} {price}')
