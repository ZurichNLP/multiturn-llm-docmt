from comet import download_model, load_from_checkpoint
import json
import argparse
# from comet import CometScorer
def load_jsonl(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [json.loads(line) for line in file]

def eval_comet(src_file, tgt_file, ref_file, is_kiwi=True, is_ours_model=False):
    if is_kiwi:
        model_path = download_model("Unbabel/wmt22-cometkiwi-da")
    else:
        model_path = download_model("Unbabel/wmt22-comet-da")
    model = load_from_checkpoint(model_path)
    src_file = open(src_file, 'r', encoding='utf-8')
    tgt_file = open(tgt_file, 'r', encoding='utf-8')
    ref_file = open(ref_file, 'r', encoding='utf-8')
    src_lines = src_file.readlines()
    tgt_lines = tgt_file.readlines()
    ref_lines = ref_file.readlines()
    src_lines = [line.strip() for line in src_lines]
    tgt_lines = [line.strip() for line in tgt_lines]
    ref_lines = [line.strip() for line in ref_lines]
    if not is_ours_model:
        src_lines = src_lines[1:]
        tgt_lines = tgt_lines[1:]
        ref_lines = ref_lines[1:]
    else:
        src_lines = src_lines[1:]
        ref_lines = ref_lines[1:]
    print(len(src_lines))
    print(len(tgt_lines))
    if not is_kiwi:
        data = [{"src": src, "mt": mt, "ref": ref} for src, mt, ref in zip(src_lines, tgt_lines, ref_lines)]
    else:
        data = [{"src": src, "mt": mt} for src, mt in zip(src_lines, tgt_lines)]
    scores = model.predict(data, gpus=1)
    avg_score = sum(scores['scores']) / len(scores['scores'])
    print(f"Average COMET Score: {avg_score:.4f}")
    return scores

def eval_comet_ours(src_file, tgt_file, ref_file, is_kiwi=True, is_ours_model=False):
    if is_kiwi:
        model_path = download_model("Unbabel/wmt22-cometkiwi-da")
    else:
        model_path = download_model("Unbabel/wmt22-comet-da")
    model = load_from_checkpoint(model_path)
    src_lines = load_jsonl(src_file)
    tgt_lines = load_jsonl(tgt_file)
    ref_lines = load_jsonl(ref_file)
    src_res = []
    tgt_res = []
    ref_res = []
    for item in src_lines:
        # print(item)
        for sent in item['original']:
            src_res.append(sent)
    for item in tgt_lines:
        for sent in item['translation_split']:
            tgt_res.append(sent)
    for item in ref_lines:
        for sent in item['reference_split']:
            ref_res.append(sent)
    print(len(src_res))
    print(len(tgt_res))
    print(len(ref_res))
    if not is_kiwi:
        data = [{"src": src, "mt": mt, "ref": ref} for src, mt, ref in zip(src_res, tgt_res, ref_res)]
    else:
        data = [{"src": src, "mt": mt} for src, mt in zip(src_res, tgt_res)]
    scores = model.predict(data, gpus=1)
    avg_score = sum(scores['scores']) / len(scores['scores'])
    print(f"Average COMET Score: {avg_score:.4f}")
    return scores
    
def parse_docs(doc_file):
    doc_data = open(doc_file, 'r', encoding='utf-8')
    doc_lines = doc_data.readlines()
    doc_lines = [line.strip() for line in doc_lines]
    return doc_lines

def compute_doc_bleu_score(doc_file, ref_file, tgt_file):
    ref_data = open(ref_file, 'r', encoding='utf-8')
    tgt_data = open(tgt_file, 'r', encoding='utf-8')
    ref_lines = ref_data.readlines()
    tgt_lines = tgt_data.readlines()
    ref_lines = [line.strip() for line in ref_lines]
    tgt_lines = [line.strip() for line in tgt_lines]
    ref_lines = ref_lines[1:]
    tgt_lines = tgt_lines[1:]
    docs = parse_docs(doc_file)
    docs = docs[1:]
    tgt_doc = ''
    ref_doc = ''
    tgt_doc_list = []
    ref_doc_list = []
    for i, (tgt, ref, doc) in enumerate(zip(tgt_lines, ref_lines, docs)):
        if doc == docs[i-1]:
            # if previous paragraph is the same as current paragraph, then we need to add the previous paragraph to the list
            tgt_doc += tgt
            ref_doc += ref
        else:
            tgt_doc_list.append(tgt_doc)
            ref_doc_list.append(ref_doc)
            tgt_doc = ''
            ref_doc = ''
    print(len(tgt_doc_list))
    print(len(ref_doc_list))
    from sacrebleu import corpus_bleu
    if 'ja-zh' in ref_file:
        print('ja-zh')
        score = corpus_bleu(tgt_doc_list, [ref_doc_list], tokenize='zh')
        return score.score
    elif 'en-ja' in ref_file:
        score = corpus_bleu(tgt_doc_list, [ref_doc_list], tokenize='ja-mecab')
        return score.score
    elif 'en-zh' in ref_file:
        score = corpus_bleu(tgt_doc_list, [ref_doc_list], tokenize='zh')
        return score.score
    else:
        score = corpus_bleu(tgt_doc_list, [ref_doc_list])
        return score.score
        
def eval_bleu(ref_file, tgt_file, data_type='txt', setting='all'):
    if data_type == 'txt':
        ref_data = open(ref_file, 'r', encoding='utf-8')
        tgt_data = open(tgt_file, 'r', encoding='utf-8')
        ref_lines = ref_data.readlines()
        tgt_lines = tgt_data.readlines()
    if data_type == 'jsonl':
        ref_lines = load_jsonl(ref_file)
        tgt_lines = load_jsonl(tgt_file)
        ref_lines = [line['reference'] for line in ref_lines]
        tgt_lines = [line['translation'] for line in tgt_lines]
    ref_lines = [line.strip() for line in ref_lines]
    tgt_lines = [line.strip() for line in tgt_lines]
    # ref_lines = ref_lines[1:]
    print(len(ref_lines))
    print(len(tgt_lines))
    from sacrebleu import corpus_bleu
    print(ref_file)
    if 'ja-zh' in ref_file:
        # print('ja-zh')
        score = corpus_bleu(tgt_lines, [ref_lines], tokenize='zh')
        return score.score
    elif 'en-ja' in ref_file:
        score = corpus_bleu(tgt_lines, [ref_lines], tokenize='ja-mecab')
        return score.score
    elif 'en-zh' in ref_file:
        score = corpus_bleu(tgt_lines, [ref_lines], tokenize='zh')
        return score.score
    else:
        score = corpus_bleu(tgt_lines, [ref_lines])
        return score.score

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang_pairs', nargs='+', help='List of items')
    parser.add_argument('--model_name', nargs='+', help='List of items')
    parser.add_argument('--tgt_file', type=str, help='List of items')
    parser.add_argument('--data_type', type=str, help='List of items')
    parser.add_argument('--is_ours', type=bool, help='List of items')
    parser.add_argument('--metric', type=str, help='List of items')
    parser.add_argument('--setting', type=str, help='List of items')
    args = parser.parse_args()
    print(args.lang_pairs)
    print(args.model_name)
    lang_pairs = args.lang_pairs
    model_name = args.model_name
    model_list = ["GPT-4", "Claude-3.5", "Unbabel-Tower70B", "Llama3-70B", "CommandR-plus", "Gemini-1.5-Pro", "Aya23", "Mistral-Large"]
    for model in model_name:
        for lang_pair in lang_pairs:
            commet_res_all = []
            bleu_res_all = []
            if model not in model_list:
                is_ours_model = True
            else:
                is_ours_model = False
            if args.data_type == 'txt':
                src_file = 'txt/sources/'+str(lang_pair)+'.txt'
                # tgt_file = 'txt/system-outputs/'+lang_pair+'/'+model+'.txt'
                ref_file = 'txt/references/'+str(lang_pair)+'.refA.txt'
            elif args.data_type == 'jsonl':
                #lang_pair = lang_pair.replace('-', '_')
                res_file_name = 'outputs/'+model+'/'+args.tgt_file+ '_'+lang_pair+ '_'+args.setting+'._gen.jsonl'
                # tgt_file = 'jsonl/system-outputs/'+lang_pair+'/'+model+'.jsonl'
                # ref_file = 'outputs/'+args.model_name+'/'+args.tgt_file+'.refA.jsonl'
            if is_ours_model:
                tgt_file = args.tgt_file
            else:
                tgt_file = 'txt/system-outputs/'+lang_pair+'/'+model+'.txt'
            
            print('is_ours_model', is_ours_model)
            if args.metric == 'bleu':   
                if args.data_type == 'txt':
                    doc_file = 'txt/documents/'+str(lang_pair)+'.docs'
                    score = compute_doc_bleu_score(doc_file, ref_file, tgt_file)
                elif args.data_type == 'jsonl':
                    score = eval_bleu(res_file_name, res_file_name, data_type='jsonl', setting=args.setting)
                bleu_res = {'lang_pair': lang_pair, 'model': model, 'bleu_score': score, 'setting': args.setting}
                bleu_res_all.append(bleu_res)
                print(bleu_res)
                with open('result/dbleu_pred_all_{}.jsonl'.format(model.split('/')[0]), 'a') as f:
                    for item in bleu_res_all:
                        f.write(json.dumps(item) + '\n')
            elif args.metric == 'comet':
                if is_ours_model:
                    comet_scores = eval_comet_ours(res_file_name, res_file_name, res_file_name, is_kiwi=False, is_ours_model=is_ours_model)
                else:
                    comet_scores = eval_comet(src_file, tgt_file, ref_file, is_kiwi=False, is_ours_model=is_ours_model)
                score = comet_scores['system_score']
                commet_res = {'lang_pair': lang_pair, 'model': model, 'comet_score': score, 'setting': args.setting}
                commet_res_all.append(commet_res)
                with open('result/comet_res_{}.jsonl'.format(model.split('/')[0]), 'a') as f:
                    for item in commet_res_all:
                        f.write(json.dumps(item) + '\n')
            # print(commet_res)
            # print(commet_res_kiwi)
            # with open('commet_res_all.jsonl', 'a') as f:
            #     for item in commet_res_all:
            #         f.write(json.dumps(item) + '\n')
            
            
    # with open('commet_res_all.jsonl', 'a') as f:
    #     for item in commet_res_all:
    #         f.write(json.dumps(item) + '\n')
    # with open('bleu_res_all.jsonl', 'a') as f:
    #     for item in bleu_res_all:
    #         f.write(json.dumps(item) + '\n')

if __name__ == '__main__':
    main()
