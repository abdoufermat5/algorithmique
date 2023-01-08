import random

from algo_fermat_utils.helpers import measure_performance


def coupon_collector(n):
    coupons = set()  # set to store collected coupons
    num_coupons = 0  # number of coupons collected
    while len(coupons) < n:
        coupons.add(random.randint(1, n))  # randomly draw a coupon
        num_coupons += 1
    return num_coupons


@measure_performance
def main(n, range_n):
    # run the simulation 1000 times and compute the average number of coupons collected
    total_coupons = 0
    for i in range(range_n):
        total_coupons += coupon_collector(n)
    print("average number of coupons needed: ",total_coupons / range_n)  # approximate average number of coupons
    # needed to complete the set


if __name__ == '__main__':
    main(10, 1000)
