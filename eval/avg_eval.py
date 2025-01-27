import json

def load_jsonl(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]

def avg_eval(file_path, metric):
    data = load_jsonl(file_path)
    group_by_setting = {"mturn": [], "mturn_icl": [], "seg": [], "seg_icl": []}
    for item in data:
        setting = item['setting']
        if setting not in group_by_setting:
            group_by_setting[setting] = []
        group_by_setting[setting].append(item[metric])
    res_avg = {}
    for setting in group_by_setting:
        print(setting, sum(group_by_setting[setting]) / len(group_by_setting[setting]))
        acc = sum(group_by_setting[setting]) / len(group_by_setting[setting])
        res_avg[setting] = acc

    return res_avg
print('dbleu_pred_all_TowerInstruct-7B-v0.2:')
avg_eval("result/dbleu_pred_all_TowerInstruct-7B-v0.2.jsonl", "bleu_score")
print('-'*100)
print('dbleu_pred_all_Meta-Llama-3.1-8B-Instruct:')
avg_eval("result/dbleu_pred_all_Meta-Llama-3.1-8B-Instruct.jsonl", "bleu_score")
print('-'*100)
print('dbleu_pred_all_gpt-4o-mini:')
avg_eval("result/dbleu_pred_all_gpt-4o-mini.jsonl", "bleu_score")
print('-'*100)
print('comet_res_Meta-Llama-3.1-8B-Instruct:')
avg_eval("result/comet_res_Meta-Llama-3.1-8B-Instruct.jsonl", "comet_score")
print('-'*100)
print('comet_res_gpt4omini:')
avg_eval("result/comet_res_gpt4omini.jsonl", "comet_score")
print('-'*100)
print('comet_res_TowerInstruct-7B-v0.2:')
avg_eval("result/comet_res_TowerInstruct-7B-v0.2.jsonl", "comet_score")
# avg_eval("res/dbleu_res_all_new.jsonl", "bleu_score")
