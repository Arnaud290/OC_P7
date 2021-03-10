"""Program brute force"""
import csv
from time import time, strftime, gmtime


def brutforce_buy_actions(action_list_csv):
    time_start = time()
    actions_list = []
    total_result = []
    with open(action_list_csv, "r") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            benefit_result = (float(row['price']) * float(row['profit']))/100
            actions_list.append([row['name'], float(row['price']), float(row['profit']), benefit_result])
    k = len(actions_list) - 1
    action_list_2 = actions_list
    action_list_2.sort(key=lambda list: list[3], reverse=True)
    for i in range(k):
        for j in range(0, k - i - 1):
            for share in actions_list:
                cash = 500
                benefit = 0
                nb_actions = 0
                while share[1] <= cash:
                    cash -= share[1]
                    nb_actions += 1
                    benefit += share[3] 
                    result_1 = share[0] + ' X ' + str(nb_actions)  
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
                            if nb_action2 > 0:
                                t_result.append(share_2[0] + ' X ' + str(nb_action2))  
                    t_result.append('REST:' + str(cash_rest) + ' €') 
                    t_result.append(round(benefit + benefit_2, 2))
                    if t_result not in total_result:
                        total_result.append(t_result)
            if action_list_2[j][3] > action_list_2[j+1][3] :
                action_list_2[j], action_list_2[j+1] = action_list_2[j+1], action_list_2[j]
    total_result.sort(key=lambda x: x[-1], reverse=True)
    time_total = time() - time_start
    time_total = strftime('%H:%M:%S', gmtime(time_total))
    return([total_result, time_total])

if __name__ == "__main__":
  
    result = brutforce_buy_actions("dataset2.csv")

    print("Temps total d'execution: ", result[1])
    print("\n\n")
    print("Nombre de résultats: " + str(len(result[0])))
    print("\n\n")
    print("Meilleur résultat: ", result[0][0])
    print("\n\n")
    print("Pire résultat: ", result[0][-1])
   