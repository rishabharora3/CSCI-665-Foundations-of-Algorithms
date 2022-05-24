import random


def computer_top_income(income_list):
    topsum = 0
    count = 0
    topindex = int(len(income_list) * 0.99)
    topindex_val = k_select_algo(income_list, topindex)
    for income in income_list:
        if income > topindex_val:
            topsum = topsum + income
            count += 1
    # edge case calculated in case kth value is repeated in list
    diff = (len(income_list) - topindex)
    if count < diff:
        topsum = topsum + (diff * topindex_val)
    return topsum


def k_select_algo(income_list, k):
    pivot = random.randint(0, len(income_list) - 1)
    pivot_element = income_list[pivot]
    l = []
    e = []
    g = []
    for index in range(len(income_list)):
        if income_list[index] < pivot_element:
            l.append(income_list[index])
        elif income_list[index] == pivot_element:
            e.append(income_list[index])
        elif income_list[index] > pivot_element:
            g.append(income_list[index])
    if k - 1 < len(l):
        return k_select_algo(l, k)
    if len(l) <= k - 1 < (len(l) + len(e)):
        return pivot_element
    else:
        return k_select_algo(g, k - len(l) - len(e))


def find_sum_top(income_list, k):
    pivot_element = random.choice(income_list)
    x, y, z = [], [], []
    top_sum = 0
    for index in range(len(income_list)):
        if income_list[index] < pivot_element:
            x.append(income_list[index])
        elif income_list[index] == pivot_element:
            y.append(income_list[index])
            top_sum = top_sum + income_list[index]
        elif income_list[index] > pivot_element:
            z.append(income_list[index])
            top_sum = top_sum + income_list[index]
    if k < len(x):
        return find_sum_top(income_list, k)
    elif k > len(x) + len(y):
        return find_sum_top(z, k - len(x) - len(y))
    else:
        return round(top_sum, 2)


def comparison(income_list, k, count):
    pivot_element = random.choice(income_list)
    l, e, g = [], [], []
    sum1, sum2, sum3 = 0, 0, 0
    for index in range(len(income_list)):
        if income_list[index] < pivot_element:
            l.append(income_list[index])
            sum1 = sum1 + income_list[index]
        elif income_list[index] == pivot_element:
            e.append(income_list[index])
            sum2 = sum2 + income_list[index]
        elif income_list[index] > pivot_element:
            g.append(income_list[index])
            sum3 = sum3 + income_list[index]
    if sum1 > k:
        return comparison(l, k, count)
    elif sum1 < k <= sum1 + sum2:
        return count + len(l) + len(e) - 1
    elif sum1 + sum2 < k:
        return comparison(g, k - sum1 - sum2, count + len(l) + len(e))


def main():
    n = int(input())
    arr = [float(input()) for _ in range(n)]
    bottom_income_sum = comparison(arr, computer_top_income(arr), 0)
    print(int(bottom_income_sum * (100 / n)))


if __name__ == '__main__':
    main()
