if __name__ == '__main__':

    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    second_lowest = sorted(set([i[1] for i in records]))[1]
    result_list = sorted(list(i[0] for i in records if i[1] == second_lowest))

    for name in result_list:
        print(name)
