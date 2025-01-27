import json
import argparse
import re
import nltk
from blonde import BLONDE
nltk.download('punkt')

def load_jsonl(file_path):
    with open(file_path, "r") as f:
        return [json.loads(line) for line in f]

def parse_input(data):
    for item in data:
        translation = item['translation']
        ref = item['reference']
        sentences = re.split(r'(?<=[.!?]) (?=[A-Z])', translation)
        item['translation'] = sentences
        sentences = re.split(r'(?<=[.!?]) (?=[A-Z])', ref)
        item['reference'] = sentences

        # item['translation'] = translation
        # item['reference'] = ref
    return data

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", default="gpt-4o-mini", type=str)
    parser.add_argument("--langs", default=["ru", "uk", "ja", "is"], type=list)
    parser.add_argument("--input_path", default="outputs/Meta-Llama-3.1-8B-Instruct/wmt2023_en_zh_en_mturn_icl._gen.jsonl", type=str)
    parser.add_argument("--output_path", default="results/Meta-Llama-3.1-8b-Instruct-blonde.jsonl", type=str)

    return parser.parse_args()

def main():
    args = parse_args()
    data = load_jsonl(args.input_path)
    # data = data[-10:]
    data = parse_input(data)
    langs = ['zh']
    settings = ['seg', 'seg_icl', 'mturn', 'mturn_icl']
    last_lang = 'zh'
    last_setting = 'mturn_icl'
    res_all = []
    for lang in langs:
    
        input_path = args.input_path.replace(last_lang, lang)
        for setting in settings:
            print('last_setting', last_setting)
            print('setting', setting)
            input_path = input_path.replace(last_setting, setting)
            data = load_jsonl(input_path)
            data = parse_input(data)
            last_setting = setting
            blonde = BLONDE()
            translations = []
            references = []
            for item in data:
                # print(item['translation_split'])
                # print(item['reference_split'])
                translations.append(item['translation_split'])
                references.append(item['reference_split'])
                #print(translations[0])
                #print(references[0])
            score = blonde.corpus_score(translations, [references])
            str_score = str(score)
            print(input_path, str_score)
            res_all.append({'input_path': input_path, 'score': str_score})
        last_lang = lang

if __name__ == "__main__":
    main()