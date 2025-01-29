import json
import os
import argparse
from tqdm import tqdm
from datasets import load_dataset
import openai  
from openai import OpenAI
from agent import GptAgent
import sacrebleu
from templates.de_examples import DE_EXAMPLES, EN_EXAMPLES, RU_EXAMPLES, ZH_EXAMPLES, HI_EXAMPLES, ES_EXAMPLES, CS_EXAMPLES, IS_EXAMPLES, JA_EXAMPLES, UK_EXAMPLES
import copy
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
from transformers import GemmaTokenizer, GemmaTokenizerFast
from templates.de_examples import EN_DE_EXAMPLES, EN_RU_EXAMPLES, EN_ZH_EXAMPLES, EN_HI_EXAMPLES, EN_ES_EXAMPLES, EN_CS_EXAMPLES, EN_IS_EXAMPLES, EN_JA_EXAMPLES, EN_UK_EXAMPLES, CS_UK_EXAMPLES, JA_ZH_EXAMPLES
def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def process_document(file_path, is_sentence=False, is_segment=False, n_paragraph=1):
    # Open the file and read the content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split the content based on the assumption that there's a blank line between documents
    documents = content.strip().split('\n\n')
    
    if is_segment:
        print('is segment')
        processed_documents = [doc.split('\n') for doc in documents]
        processed_documents_2 = []
        if is_sentence:
            for doc in processed_documents:
                split_doc = [para.split('.') for para in doc]
                final_doc = []
                if n_paragraph == 1:
                    for para in split_doc:
                        final_doc.extend(para)
                else:
                    for i in range(0, len(split_doc), n_paragraph):
                        final_doc.extend(split_doc[i:min(i+n_paragraph, len(split_doc))])
                final_doc = [sent for sent in final_doc if sent != ' ' and sent != '']
                processed_documents_2.append(final_doc)
                processed_documents = processed_documents_2
        if n_paragraph != 1:
            processed_documents_para = []
            for doc in processed_documents:
                new_doc = []
                for i in range(0, len(doc), n_paragraph):
                    new_para = ' '.join(doc[i:min(i+n_paragraph, len(doc))])[1:]
                    new_doc.append(new_para)
                processed_documents_para.append(new_doc)
            processed_documents = processed_documents_para
    else:
        processed_documents = [' '.join(doc.split('\n')) for doc in documents]
    
    return processed_documents

def process_concact_document(documents, n):
    # Open the file and read the content
    concatenated_docs = [' '.join(documents[i:i+n]) for i in range(0, len(documents), n)]
    
    return concatenated_docs

def process_list_document(file_path):
    # Open the file and read the content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split the content based on the assumption that there's a blank line between documents
    documents = content.strip().split('\n\n')
    
    # For each document, we'll join the lines (sentences) and return a list of processed documents
    processed_documents = [ doc.split('\n') for doc in documents]
    
    return processed_documents

def remove_triple_backlashes(trans_result):
    trans_result = trans_result.replace('```', '')
    return trans_result

def get_trans_prompt(p, lang_direction, is_icl=False, is_tower=False, is_og=False, shot_num=3):
    direct_mapping = {
        'de-en': ['German', 'English'],
        'en-de': ['English', 'German'],
        'zh-en': ['Chinese', 'English'],
        'en-zh': ['English', 'Chinese'],
        'zh-de': ['Chinese', 'German'],
        'de-zh': ['German', 'Chinese'],
        'fr-en': ['French', 'English'],
        'en-fr': ['English', 'French'],
        'en-es': ['English', 'Spanish'],
        'es-en': ['Spanish', 'English'],
        'en-ru': ['English', 'Russian'],
        'en-hi': ['English', 'Hindi'],
        'en-cs': ['English', 'Czech'],
        'en-is': ['English', 'Icelandic'],
        'en-ja': ['English', 'Japanese'],
        'en-uk': ['English', 'Ukrainian'],
        'cs-uk': ['Czech', 'Ukrainian'],
        'ja-zh': ['Japanese', 'Chinese'],
        'x-en': ['source', 'English'],
    }
    source_lang, target_lang = direct_mapping[lang_direction]
    user_tower_prompt = 'You need to translate the following {} text into {}. \n{}: {} \n{}:"'
    user_prompt = 'You need to translate the input {} sentence to {}. Input: {} Please directly reply with the translation, start with "Translation:"'
    messages = [{'role': 'system',
                 'content': 'You are a good translator.'
                 }]
    if is_og:
        user_prompt = 'Translate the following segment surrounded in triple backlashes into {}. Please directly reply with the translation,without any other text. The {} segment: \n```{}```\n'
        messages = [{'role': 'system',
                 'content': 'You are a good translator.'
                 }]

    if is_icl and not is_og:
        source_sentences = EN_EXAMPLES
        mapping_lang = {
            'en-de': DE_EXAMPLES,
            'zh-en': EN_EXAMPLES,
            'de-en': EN_EXAMPLES,
            'en-zh': ZH_EXAMPLES,
            'en-ru': RU_EXAMPLES,
            'ru-en': EN_EXAMPLES,
            'en-hi': HI_EXAMPLES,
            'en-es': ES_EXAMPLES,
            'en-cs': CS_EXAMPLES,
            'en-is': IS_EXAMPLES,
            'en-ja': JA_EXAMPLES,
            'en-uk': UK_EXAMPLES,
            'x-en': EN_EXAMPLES,
            'cs-uk': UK_EXAMPLES,
            'ja-zh': ZH_EXAMPLES,
        }
        if lang_direction == 'zh-en':
            source_sentences = ZH_EXAMPLES
        if lang_direction == 'cs-uk':
            source_sentences = CS_EXAMPLES
        if lang_direction == 'ja-zh':
            source_sentences = JA_EXAMPLES
        if lang_direction == 'x-en':
            source_sentences = X_EXAMPLES
        target_sentences = mapping_lang[lang_direction]
        for source_sentence, target_sentence in zip(source_sentences[:shot_num], target_sentences[:shot_num]):
            if is_tower:
                messages.append({'role': 'user',
                             'content': user_tower_prompt.format(source_lang, target_lang, source_lang, source_sentence, target_lang),
                             })
                messages.append({'role': 'assistant',
                             'content': target_sentence,
                             })
            else:
                messages.append({'role': 'user',
                             'content': user_prompt.format(source_lang, target_lang, source_sentence),
                         })
                messages.append({'role': 'assistant',
                             'content': 'Translation: ' + target_sentence,
                             })
    if is_tower:
        messages.append({'role': 'user',
                     'content': user_tower_prompt.format(source_lang, target_lang, source_lang, p, target_lang),
                 })
    if is_og and is_icl:
        mapping_lang = {
            'en-ru': EN_RU_EXAMPLES,
            'en-zh': EN_ZH_EXAMPLES,
            'en-hi': EN_HI_EXAMPLES,
            'en-es': EN_ES_EXAMPLES,
            'en-cs': EN_CS_EXAMPLES,
            'en-is': EN_IS_EXAMPLES,
            'en-ja': EN_JA_EXAMPLES,
            'en-uk': EN_UK_EXAMPLES,
            'en-de': EN_DE_EXAMPLES,
            'cs-uk': CS_UK_EXAMPLES,
            'ja-zh': JA_ZH_EXAMPLES,
        }
        pair_sentences = mapping_lang[lang_direction]
        for item in pair_sentences:
            messages.append({'role': 'user',
                             'content': user_prompt.format(target_lang, source_lang, item['source']),
                             })
            messages.append({'role': 'assistant',
                             'content': f"```{item['target']}```",
                             })
   
        messages.append({'role': 'user',
                     'content': user_prompt.format(target_lang, source_lang, p),
                     })
    else:
        messages.append({'role': 'user',
                     'content': user_prompt.format(target_lang, source_lang, p),
                     })
    print('messages', messages)
    print('-'*100)
    return messages

if __name__ == '__main__':
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Translate German texts to English using VLLM Agent.')
    parser.add_argument('--target_file', type=str, default='../wmt_devsets/wmt24_en.txt', help='File to load')
    parser.add_argument('--source_file', type=str, default='../wmt_devsets/wmt24_de.txt', help='File to load')
    parser.add_argument('--output_file', type=str, default='reverse-translations.json', help='File to save translations')
    parser.add_argument('--openai_api_key', type=str, default='', help='OpenAI API key')
    parser.add_argument('--model_name', type=str, default='gpt-4o-mini-2024-07-18', help='GPT model name')
    parser.add_argument('--data_num', type=int, default=10)
    parser.add_argument('--max_new_tokens', type=int, default=16384)
    parser.add_argument('--max_num_seqs', type=int, default=1)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--prefix_sentence', action='store_true')
    parser.add_argument('--prefix_sentence_num', type=int, default=1)
    parser.add_argument('--is_segment', action='store_true')
    parser.add_argument('--is_conversation', action='store_true')
    parser.add_argument('--by_sentence', action='store_true')
    parser.add_argument('--is_sentence', action='store_true')
    parser.add_argument('--n_paragraph', type=int, default=1)
    parser.add_argument('--is_icl', action='store_true')
    parser.add_argument('--lang_direction', type=str, default='de-en', help='Language direction to translate')
    parser.add_argument('--is_tower', action='store_true')
    parser.add_argument('--is_og', action='store_true')
    parser.add_argument('--shot_num', type=int, default=3)
    args = parser.parse_args()
    
    segmented_documents_source = process_document(args.source_file, args.is_sentence, args.is_segment or args.is_conversation, args.n_paragraph)
    segmented_documents_target = process_document(args.target_file, args.is_sentence, args.is_segment or args.is_conversation, args.n_paragraph)
    
    if args.data_num == -1:
        processed_documents_source = segmented_documents_source
        processed_documents_target = segmented_documents_target
    else:
        processed_documents_source = segmented_documents_source[:args.data_num]
        processed_documents_target = segmented_documents_target[:args.data_num]

    source_texts = processed_documents_source
    target_texts = processed_documents_target
    print('length of target texts', len(target_texts))
    references = target_texts

    trans_prompts = []
    if args.is_conversation:
        for doc in source_texts:
            trans_prompt = []
            for text in doc:
                text = get_trans_prompt(text, args.lang_direction, args.is_icl, args.is_tower, args.is_og, args.shot_num)
                trans_prompt.append(text)
            trans_prompts.append(trans_prompt)
    elif args.is_segment:
        for doc in source_texts:
            trans_prompt = []
            for text in doc:
                text = get_trans_prompt(text, args.lang_direction, args.is_icl, args.is_tower, args.is_og, args.shot_num)
                trans_prompt.append(text)
            trans_prompts.append(trans_prompt)
    else:
        for text in source_texts:
            text = get_trans_prompt(text, args.lang_direction, args.is_icl, args.is_tower, args.is_og, args.shot_num)
            trans_prompts.append(text)

    translator = GptAgent(args.model_name)

    translations = []
    translations_split = []
    if args.is_conversation:
        for trans_prompt in tqdm(trans_prompts):
            prev_prefix = []
            res_all = ' '
            translation_split = []
            for text in trans_prompt:
                if len(prev_prefix) == 0:
                    prev_prefix = text
                else:
                    prev_prefix.append(text[-1])
                output = translator.generate(prev_prefix)
                res = {'role': 'assistant', 'content': output}
                prev_prefix.append(res)
                if args.is_tower or args.is_og:
                    res['content'] = remove_triple_backlashes(res['content'])
                    res_all += res['content'] + ' '
                    translation_split.append(res['content'])
                else:
                    res_all += res['content'][len('Translation: '):] + ' '
                    translation_split.append(res['content'][len('Translation: '):])
            translations.append(res_all)
            translations_split.append(translation_split)
    elif args.is_segment:
        for trans_prompt in tqdm(trans_prompts):
            batch_translation = []
            translation_split = []
            for sentence in trans_prompt:
                trans_sentence = translator.generate(sentence)
                if args.is_tower or args.is_og:
                    trans_sentence = remove_triple_backlashes(trans_sentence)
                else:
                    trans_sentence = trans_sentence[len('Translation: '):]
                batch_translation.append(trans_sentence)
                translation_split.append(trans_sentence)
            translations.append(' '.join(batch_translation))
            translations_split.append(translation_split)
    else:
        for trans_prompt in tqdm(trans_prompts):
            trans_sentence = translator.generate(trans_prompt)
            if args.is_tower or args.is_og:
                trans_sentence = remove_triple_backlashes(trans_sentence)
            else:
                trans_sentence = trans_sentence[len('Translation: '):]
            translations.append(trans_sentence)

    # process reference
    references_split = copy.deepcopy(references)
    if args.is_segment or args.is_conversation:
        for i in range(len(references)):
            processed_references = ''
            for j in range(len(references[i])):
                processed_references += references[i][j] + ' '
            references[i] = processed_references

    if not args.is_conversation and not args.is_segment:
        with open(args.output_file[:-len('.json')] + '_gen.jsonl', 'w', encoding='utf-8') as f:
            for original, translation, reference in zip(source_texts, translations, references):
                json_line = json.dumps({
                    'original': original,
                    'translation': translation,
                    'reference': reference,
                }, ensure_ascii=False)
                f.write(json_line + '\n')
    else:
        with open(args.output_file[:-len('.json')] + '_gen.jsonl', 'w', encoding='utf-8') as f:
            for original, translation, reference, reference_split, translation_split in zip(source_texts, translations, references, references_split, translations_split):
                json_line = json.dumps({
                    'original': original,
                    'translation': translation,
                    'translation_split': translation_split,
                    'reference': reference,
                    'reference_split': reference_split,
                }, ensure_ascii=False)
                f.write(json_line + '\n')

    print(f"Translations saved to {args.output_file}")

