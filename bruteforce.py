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
            actions_list.append(("share_" + str(i), int(row['cost_per_share']), int(row['benefit']), benefit_result))
            i += 1
    actions_list.sort(key=lambda tup: tup[3], reverse=True)

def test_buy_actions():
    for i in range(len(actions_list)):
        results = []
        cash = 500
        benefit = 0
        nb_actions = 0
        while actions_list[i][1] <= cash:
            cash -= actions_list[i][1]
            nb_actions += 1
            benefit += actions_list[i][3]  
        if nb_actions > 0:
            results.append(actions_list[i][0] + ' X ' + str(nb_actions)) 
        for share in actions_list:
            nb_actions = 0
            if share != actions_list[i]:
                while share[1] <= cash:
                    cash -= share[1]
                    nb_actions += 1
                    benefit += share[3]
                if nb_actions > 0:
                    results.append(share[0] + ' X ' + str(nb_actions))
        results.append('REST: ' + str(cash))
        results.append(round(benefit,2))
        total_result.append(results)
        results = []
    total_result.sort(key=lambda x: x[-1], reverse=True)

if __name__ == "__main__":
    get_actions("20_actions.csv")
    for action in actions_list:
        print(action)
    print("\n \n")
    test_buy_actions()

    for result in total_result:
        print(result)
