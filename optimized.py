"""Program brute force"""
import os
import csv
from time import time, strftime, gmtime

def optimized_buy_actions(action_list_csv):
    time_start = time()
    actions_list = []
    result_list_best = []
    CASH = 500
    iteration = 0
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
    actions_list.sort(key=lambda list: list[4], reverse=True)
    cash = CASH
    benefit = 0
    for share in actions_list:
        nb_buy_share = 0
        while cash >= share[1]:
            cash -= share[1]
            nb_buy_share += 1
            benefit += share[3]
            iteration += 1
        if  nb_buy_share > 0:
            result_list_best.append((share[0], nb_buy_share, round((share[3] * nb_buy_share), 2)))
    result_list_best.append(round(cash, 2))
    result_list_best.append(round(benefit, 2)) 
    result_list_best.append(iteration)    
    time_total = time() - time_start
    time_total = strftime('%H:%M:%S', gmtime(time_total))
    result_list_best.append(time_total)
    return result_list_best
    
if __name__ == "__main__":
    os.system('clear')
    result = optimized_buy_actions("dataset2.csv")
    print("Temps total d'execution: ", result[-1])
    print("\n\n")
    print("Nombre d'itérations': " + str(result[-2]))
    print("\n\n")
    print("Meilleur résultat: \n\n")
    TEXT = "l'action: {}, acheté {} fois, pour un bénéfice de {} € au bout de 2 ans\n"
    for i in range(len(result) - 4):
        share = result[i]
        print(TEXT.format(share[0], share[1], share[2]))  
    print("\n\n")
    print("il reste {} €".format(result[-4]))
    print("\n\n")
    print("Le montant total des bénéfices est de {} €".format(result[-3]))