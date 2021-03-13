"""Program brute force"""
from time import time, strftime, gmtime


def bruteforce_buy_actions(actions_list):
    """ Big O notation polynomial time O(n^4)"""
    CASH = 500
    iteration = 0
    time_start = time()
    total_result = []
    k = len(actions_list) - 1
    action_l_2 = actions_list
    action_l_2.sort(key=lambda list: list[4], reverse=True)
    for i in range(k):
        for j in range(0, k - i - 1):
            for share in actions_list:
                cash = CASH
                benefit = 0
                nb_actions = 0
                while share[1] <= cash:
                    cash -= share[1]
                    nb_actions += 1
                    benefit += share[3]
                    result_1 = (share[0],
                                nb_actions,
                                round((nb_actions * share[3]), 2))
                    cash_rest = cash
                    benefit_2 = 0
                    t_result = [result_1]
                    for share_2 in action_l_2:
                        nb_action2 = 0
                        if share_2 != share:
                            while share_2[1] <= cash_rest:
                                cash_rest -= share_2[1]
                                nb_action2 += 1
                                benefit_2 += share_2[3]
                                iteration += 1
                            if nb_action2 > 0:
                                t_result.append((share_2[0],
                                                 nb_action2,
                                                 round((nb_action2 *
                                                        share_2[3]), 2)))
                    t_result.append(cash_rest)
                    t_result.append(round(benefit + benefit_2, 2))
                    if t_result not in total_result:
                        total_result.append(t_result)
            if action_l_2[j][3] > action_l_2[j+1][3]:
                action_l_2[j], action_l_2[j+1] = action_l_2[j+1], action_l_2[j]
    total_result.sort(key=lambda x: x[-1], reverse=True)
    time_total = time() - time_start
    time_total = strftime('%M:%S', gmtime(time_total))
    return([total_result, time_total, iteration])
