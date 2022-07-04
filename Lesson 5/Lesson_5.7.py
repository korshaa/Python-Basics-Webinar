import json
with open('text_7.txt', 'r', encoding='utf-8') as my_f:
    all_firm = [i for i in my_f.read().split()]
    profit_list = [int(all_firm[i]) - int(all_firm[i + 1]) for i in range(2, len(all_firm), 4)]
    firm_list = [all_firm[i] for i in range(0, len(all_firm), 4)]
    dict_firms = {k: y for k, y in zip(firm_list, profit_list)}
    dict_profit = {'average_profit': sum([i for i in profit_list if i > 0]) / len([i for i in profit_list if i > 0])}
    final_list = [dict_firms, dict_profit]


with open('text_7_j.txt', 'w', encoding='utf-8') as my_j:
    json.dump(final_list, my_j, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
