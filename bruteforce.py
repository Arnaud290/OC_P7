"""Program brute force"""
import csv

actions_list = []
total_result = []

def get_actions(csv_file):
    with open(csv_file, "r") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        i = 1
        for row in reader:
            benefit_result = (int(row['cost_per_share']) * int(row['benefit']))/100
            actions_list.append(["share_" + str(i), int(row['cost_per_share']), int(row['benefit']), benefit_result])
            i += 1
    actions_list.sort(key=lambda list: list[3], reverse=True)

def test_buy_actions():
    k = len(actions_list) - 1
    action_list_2 = actions_list
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
                    t_result.append(cash_rest) 
                    t_result.append(round(benefit + benefit_2, 2))
                    if t_result not in total_result:
                        total_result.append(t_result)
            if action_list_2[j][3] > action_list_2[j+1][3] :
                action_list_2[j], action_list_2[j+1] = action_list_2[j+1], action_list_2[j]

if __name__ == "__main__":
    get_actions("20_actions.csv")
    print("\n\nListe des actions : \n")
    for action in actions_list:
        print(action)
    print("\n \n")

    test_buy_actions()
    print('Nombre total de resultats: ',len(total_result))
    total_result.sort(key=lambda x: x[-1], reverse=True)

    print('\n\nLa meilleur combinaison est :\n')
    for i in range(len(total_result[0]) - 2):
        print("l'action : ", total_result[0][i], "fois")
    print("il reste: ", total_result[0][-2], "€")
    print("le benefice sera de :", total_result[0][-1]," € au bout de 2 ans\n\n")
    print('La moins bonne combinaison est :\n')
    for i in range(len(total_result[-1]) - 2):
        print("l'action : ", total_result[-1][i], "fois")
    print("il reste: ", total_result[-1][-2], "€")
    print("le benefice sera de :", total_result[-1][-1],"€ au bout de 2 ans")
