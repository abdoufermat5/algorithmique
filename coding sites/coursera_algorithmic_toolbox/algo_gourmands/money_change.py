# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    n1 = money // 10
    r1 = money % 10
    n2 = r1 // 5
    r2 = r1 % 5
    n3 = r2
    return n3 + n2 + n1


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
