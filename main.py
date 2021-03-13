import os
from tqdm import tqdm
from bruteforce import bruteforce_buy_actions
from optimized import optimized_buy_actions
import csv

TEXT_MENU = "Bienvenue sur le test d'achat d'actions\n\n\
1 : Méthode en brute force pour 20 actions\n\
2 : Méthode optimisé pour 20 actions\n\
3 : Méthode optimisé pour la liste compléte d'action\n\
4 : Edition fichier csv temps d'exectution en fonction\
 du nombre d'actions sur 40 actions en brut force\n\
5 : Edition fichier csv temps d'exectution en fonction\
du nombre d'actions sur 40 actions en optimisé\n\
6 : Quitter\n"

TEXT = "l'action: {}, acheté {} fois,\
pour un bénéfice de {} € au bout de 2 ans\n"


def result_bruteforce(actions_list):
    """Display bruteforce results"""
    result = bruteforce_buy_actions(actions_list)
    print("Resultat du brut force: \n\n")
    print("Temps total d'execution: ", result[1])
    print("\n\n")
    print("Nombre de résultats: " + str(len(result[0])))
    print("\n\n")
    print("Nombre d'itérations': " + str(result[2]))
    print("\n\n")
    print("Meilleur résultat: \n\n")
    for i in range(len(result[0][0]) - 2):
        share = result[0][0][i]
        print(TEXT.format(share[0], share[1], share[2]))
    print("\n\n")
    print("il reste {} €".format(result[0][0][-2]))
    print("\n\n")
    print("Le montant total des\
bénéfices est de {} €".format(result[0][0][-1]))


def result_optimized(actions_list):
    """Display optimized results"""
    result = optimized_buy_actions(actions_list)
    print("Résultat avec la méthode optimisé: \n\n")
    print("Temps total d'execution: ", result[-1])
    print("\n\n")
    print("Nombre d'itérations': " + str(result[-2]))
    print("\n\n")
    print("Meilleur résultat: \n\n")
    for i in range(len(result) - 4):
        share = result[i]
        print(TEXT.format(share[0], share[1], share[2]))
    print("\n\n")
    print("il reste {} €".format(result[-4]))
    print("\n\n")
    print("Le montant total des bénéfices est de {} €".format(result[-3]))


def action_list_csv_to_action_list(action_list_csv):
    """Add the information of a csv file to a list"""
    CASH = 500
    actions_list = []
    with open(action_list_csv, "r") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            if float(row['price']) > 0:
                max_nb_buy = int(CASH // float(row['price']))
                benefit_result = (
                                    float(row['price']) *
                                    float(row['profit'])
                                ) / 100
                max_benefit_result = round((benefit_result * max_nb_buy), 2)
                actions_list.append([row['name'],
                                    float(row['price']),
                                    float(row['profit']),
                                    benefit_result,
                                    max_benefit_result])
    return actions_list


def time_iterations_result_to_csv(actions_list,
                                  fonction_buy_action,
                                  file_name):
    """Adds the results (number of actions, iterations, time)
    of the two algorithms in a csv file"""
    with open(file_name, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['nb_actions', 'nb_iterations', 'time (secondes)'])
        actions_list_test = []
        for i in tqdm(range(len(actions_list))):
            actions_list_test.append(actions_list[i])
            if fonction_buy_action == bruteforce_buy_actions:
                result = bruteforce_buy_actions(actions_list_test)
                minutes = result[1].split(':')[0]
                secondes = result[1].split(':')[1]
                total_time = int(minutes) * 60 + int(secondes)
                writer.writerow([len(actions_list_test),
                                result[2],
                                total_time])
            else:
                result = optimized_buy_actions(actions_list_test)
                minutes = str(result[-1]).split(':')[0]
                secondes = str(result[-1]).split(':')[1]
                total_time = int(minutes) * 60 + int(secondes)
                writer.writerow([len(actions_list_test),
                                result[-2],
                                total_time])


def menu():
    """Engine menu"""
    select = ''
    while True:
        os.system("clear")
        print(TEXT_MENU)
        select = input("choix: \n\n")
        if select not in ('1', '2', '3', '4', '5', '6'):
            continue
        if select == '1':
            os.system("clear")
            action_list = action_list_csv_to_action_list("20_actions.csv")
            result_bruteforce(action_list)
            input("press any key...")
        if select == '2':
            os.system("clear")
            action_list = action_list_csv_to_action_list("20_actions.csv")
            result_optimized(action_list)
            input("press any key...")
        if select == '3':
            os.system("clear")
            action_list = action_list_csv_to_action_list("dataset2.csv")
            result_optimized(action_list)
            input("press any key...")
        if select == '4':
            action_list = action_list_csv_to_action_list("test_40_actions.csv")
            time_iterations_result_to_csv(action_list,
                                          bruteforce_buy_actions,
                                          "bruteforce_buy_actions.csv")
        if select == '5':
            action_list = action_list_csv_to_action_list("test_40_actions.csv")
            time_iterations_result_to_csv(action_list,
                                          optimized_buy_actions,
                                          "optimized_buy_actions.csv")
        if select == '6':
            break


if __name__ == "__main__":
    menu()
