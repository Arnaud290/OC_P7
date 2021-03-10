"""Program brute force"""
import csv
from time import time, strftime, gmtime
import os

def brutforce_buy_actions(action_list_csv):
    CASH = 500
    iteration = 0
    time_start = time()
    actions_list = []
    total_result = []
    with open(action_list_csv, "r") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            if float(row['price']) > 0:
                max_nb_buy = int(CASH // float(row['price']))
                benefit_result = (float(row['price']) * float(row['profit'])) / 100
                max_benefit_result = round((benefit_result * max_nb_buy), 2)
                actions_list.append([row['name'],
                                    float(row['price']),
                                    float(row['profit']),
                                    benefit_result,
                                    max_benefit_result
                                    ])
    k = len(actions_list) - 1
    action_list_2 = actions_list
    action_list_2.sort(key=lambda list: list[4], reverse=True)
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
                    result_1 = (share[0], nb_actions, round((nb_actions * share[3]), 2))  
                    cash_rest = cash
                    benefit_2 = 0
                    t_result = [result_1]
                    for share_2 in action_list_2:
                        nb_action2 = 0
                        if share_2 != share:
                            while share_2[1] <=  cash_rest:
                                cash_rest -= share_2[1]
                                nb_action2 += 1
                                benefit_2 += share_2[3]
                                iteration += 1
                            if nb_action2 > 0:
                                t_result.append((share_2[0],
                                                nb_action2,
                                                round((nb_action2 * share_2[3]), 2)))  
                    t_result.append(cash_rest) 
                    t_result.append(round(benefit + benefit_2, 2))
                    if t_result not in total_result:
                        total_result.append(t_result)
            if action_list_2[j][3] > action_list_2[j+1][3] :
                action_list_2[j], action_list_2[j+1] = action_list_2[j+1], action_list_2[j]
    total_result.sort(key=lambda x: x[-1], reverse=True)
    time_total = time() - time_start
    time_total = strftime('%H:%M:%S', gmtime(time_total))
    return([total_result, time_total, iteration])

if __name__ == "__main__":
    os.system('clear')
    result = brutforce_buy_actions("dataset2.csv")
    print("Temps total d'execution: ", result[1])
    print("\n\n")
    print("Nombre de résultats: " + str(len(result[0])))
    print("\n\n")
    print("Nombre d'itérations': " + str(result[2]))
    print("\n\n")
    print("Meilleur résultat: \n\n")
    TEXT = "l'action: {}, acheté {} fois, pour un bénéfice de {} € au bout de 2 ans\n"
    for i in range(len(result[0][0]) - 2):
        share = result[0][0][i]
        print(TEXT.format(share[0], share[1], share[2]))  
    print("\n\n")
    print("il reste {} €".format(result[0][0][-2]))
    print("\n\n")
    print("Le montant total des bénéfices est de {} €".format(result[0][0][-1]))