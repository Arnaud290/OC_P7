"""Program brute force"""
import csv
from time import time, strftime, gmtime

def buy_actions_optimized(action_list_csv):
    time_start = time()
    actions_list = []

    with open(action_list_csv, "r") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            if float(row['price']) > 0:
                benefit_result =  (float(row['price']) * float(row['profit']))/100
                actions_list.append([row['name'], float(row['price']), float(row['profit']), benefit_result])      
     
    actions_list.sort(key=lambda list: list[2], reverse=True)

    #Best list  
    result_list_best = []
    cash = 500
    benefit = 0
    for share in actions_list:
        nb_buy_share = 0
        while cash >= share[1]:
            cash -= share[1]
            nb_buy_share += 1
            benefit += share[3]
        if  nb_buy_share > 0:
            result_list_best.append(share[0] + ' X ' + str(nb_buy_share))
    result_list_best.append('REST: ' + str(round(cash, 2)))
    result_list_best.append('BENEFIT: ' + str(round(benefit, 2)))    

    actions_list.sort(key=lambda list: list[2])

    #Worst List
    result_list_worst = []
    cash = 500
    benefit = 0
    for share in actions_list:
        nb_buy_share = 0
        while cash >= share[1]:
            cash -= share[1]
            nb_buy_share += 1
            benefit += share[3]
        if  nb_buy_share > 0:
            result_list_worst.append(share[0] + ' X ' + str(nb_buy_share))
    result_list_worst.append('REST: ' + str(round(cash, 2)) + ' €')
    result_list_worst.append('BENEFIT: ' + str(round(benefit, 2)) + ' €')
    time_total = time() - time_start
    time_total = strftime('%H:%M:%S', gmtime(time_total))
    return([result_list_best, result_list_worst, time_total])

if __name__ == "__main__":

    result = buy_actions_optimized("dataset2.csv")
    print("Temps total d'execution: ", result[2], "seconde")
    print("\n\n Meilleur résultat: ", result[0])
    print("\n\n pire résultat: ", result[1])
