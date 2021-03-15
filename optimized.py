"""Program brute force"""
from time import time, strftime, gmtime


def optimized_buy_actions(actions_list):
    """big O notation linear time O(n)"""
    time_start = time()
    result_list_best = []
    CASH = 500
    iteration = 0
    actions_list.sort(key=lambda list: list[4], reverse=True)
    cash = CASH
    benefit = 0
    for share in actions_list:
        nb_buy_share = 0
        iteration += 1
        while cash >= share[1]:
            cash -= share[1]
            nb_buy_share += 1
            benefit += round(share[3], 2)
            iteration += 1
        if nb_buy_share > 0:
            result_list_best.append((share[0],
                                     nb_buy_share,
                                     round((share[3] * nb_buy_share),
                                     2)))
    result_list_best.append(round(cash, 2))
    result_list_best.append(round(benefit, 2))
    result_list_best.append(iteration)
    time_total = time() - time_start
    time_total = strftime('%M:%S', gmtime(time_total))
    result_list_best.append(time_total)
    return result_list_best
