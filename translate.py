import json
import os
import argparse
from datasets import load_dataset
from agent import VllmAgent  # Assuming the VllmAgent is in a file named agent.py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
import sacrebleu
import copy
from transformers import GemmaTokenizer, GemmaTokenizerFast
from templates.de_examples import DE_EXAMPLES, EN_EXAMPLES, RU_EXAMPLES, ZH_EXAMPLES, HI_EXAMPLES, ES_EXAMPLES, CS_EXAMPLES, IS_EXAMPLES, JA_EXAMPLES, UK_EXAMPLES, X_EXAMPLES
from templates.de_examples import EN_DE_EXAMPLES, EN_RU_EXAMPLES, EN_ZH_EXAMPLES, EN_HI_EXAMPLES, EN_ES_EXAMPLES, EN_CS_EXAMPLES, EN_IS_EXAMPLES, EN_JA_EXAMPLES, EN_UK_EXAMPLES, CS_UK_EXAMPLES, JA_ZH_EXAMPLES
from tqdm import tqdm
# def segment_document(processed_documents):
#     return [doc.split('\n') for doc in processed_documents]
def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def process_document(file_path, is_sentence=False, is_segment=False, n_paragraph=1):
    # Open the file and read the content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split the content based on the assumption that there's a blank line between documents
    documents = content.strip().split('\n\n')
    
    # For each document, we'll join the lines (sentences) and return a list of processed documents
    if is_segment:
        print('is segment')
        # split by '\n' or '.':
        processed_documents = [doc.split('\n') for doc in documents]
        processed_documents_2 = []
        if is_sentence:
            for doc in processed_documents:
                #print('len(doc)', len(doc))
                split_doc = [para.split('.') for para in doc]
                final_doc = []
                if n_paragraph == 1:
                    for para in split_doc:
                        final_doc.extend(para)
                else:
                    for i in range(0, len(split_doc), n_paragraph):
                        final_doc.extend(split_doc[i:min(i+n_paragraph, len(split_doc))])
                # delete empty elements in final_doc
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

                    #new_doc.append(doc[i:min(i+n_paragraph, len(doc))])
                processed_documents_para.append(new_doc)
            processed_documents = processed_documents_para
        print('len(processed_documents_2)', len(processed_documents_2))
        print('len(processed_documents)', len(processed_documents))
        print('len(processed_documents[0])', len(processed_documents[0]))
    else:
        processed_documents = [' '.join(doc.split('\n')) for doc in documents]
        #print('processed_documents[0]', processed_documents[0])
    
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

# a parse function for the translation result to remove triple backlashes:
def remove_triple_backlashes(trans_result):
    # remove triple backlashes:
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
        # if lang_direction == 'x-en':
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
    elif is_tower:
        messages.append({'role': 'user',
                     'content': user_tower_prompt.format(source_lang, target_lang, source_lang, p, target_lang),
                 })
    elif is_og and is_icl:
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

def save_jsonl(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        for i, doc in enumerate(data):
            item = {'doc id': str(i), 'translation_split': doc}
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')
def save_as_txt(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(item + '\n')

if __name__ == '__main__':
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Translate German texts to English using VLLM Agent.')
    parser.add_argument('--target_file', type=str, default='../par3/par3_dataset_test/candide_fr/src_txts/candide_src.txt', help='File to load')
    parser.add_argument('--source_file', type=str, default='../par3/par3_dataset_test/candide_fr/trans_txts/candide_gt.txt', help='File to load')
    parser.add_argument('--output_file', type=str, default='reverse-translations.json', help='File to save translations')
    parser.add_argument('--model_name', type=str, default='Meta-Llama/Meta-Llama-3.1-8B-Instruct', help='Translation model name') #'THUDM/LongWriter-llama3.1-8b'
    parser.add_argument('--gpu_memory_utilization', type=float, default=0.95, help='GPU memory utilization for VLLM Agent')
    parser.add_argument('--max_model_len', type=int, default=16384, help='Maximum model length')
    parser.add_argument('--batch_size', type=int, default=8, help='Batch size for translation')
    parser.add_argument('--is_dp', action='store_true')
    parser.add_argument('--temperature', type=float, default=0.0)
    parser.add_argument('--top_p', type=float, default=0.9)
    parser.add_argument('--data_num', type=int, default=10)
    parser.add_argument('--max_new_tokens', type=int, default=2048)
    parser.add_argument('--max_num_seqs', type=int, default=1)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--n_paragraph', type=int, default=1)
    parser.add_argument('--is_segment', action='store_true')
    parser.add_argument('--is_conversation', action='store_true')
    parser.add_argument('--is_sentence', action='store_true')
    parser.add_argument('--one_by_one', action='store_true', help='input one by one')
    parser.add_argument('--is_icl', action='store_true')
    parser.add_argument('--is_tower', action='store_true')
    parser.add_argument('--is_og', action='store_true')
    parser.add_argument('--is_save_txt', action='store_true')
    parser.add_argument('--lang_direction', type=str, default='de-en', help='Language direction to translate')
    parser.add_argument('--shot_num', type=int, default=3)
    args = parser.parse_args()
    segmented_documents_source = process_document(args.source_file, args.is_sentence, args.is_segment or args.is_conversation, args.n_paragraph)
    segmented_documents_target = process_document(args.target_file, args.is_sentence, args.is_segment or args.is_conversation, args.n_paragraph)
    #print('segmented_documents_de', segmented_documents_de)
    # if data_num is -1, use all data
    if args.data_num == -1:
        processed_documents_source = segmented_documents_source
        processed_documents_target = segmented_documents_target
    else:
        processed_documents_source = segmented_documents_source[:args.data_num]
        processed_documents_target = segmented_documents_target[:args.data_num]
    #german_texts = [example['src'] for example in de_en_dataset]
    #print('processed_documents_de', processed_documents_de)
    source_texts = processed_documents_source
    target_texts = processed_documents_target
    print('length of target texts', len(target_texts))
    references = target_texts
    # Initialize the VLLM Agent, and set the generation kwargs
    vllm_kwargs = {
        "gpu_memory_utilization": args.gpu_memory_utilization,
        "max_model_len": args.max_model_len,
    }
    generation_kwargs = {
        "temperature": args.temperature,
        "top_p": args.top_p,
        "max_tokens": args.max_new_tokens,
        "seed": args.seed,
    }
    if args.is_dp:
        vllm_kwargs["data_parallel_size"] = torch.cuda.device_count()
    else:
        vllm_kwargs['tensor_parallel_size'] = torch.cuda.device_count()
    if "llama-3.1" in args.model_name.lower():
        generation_kwargs["stop_token_ids"] = [128001, 128008, 128009] # <|end_of_text|>, <|eom_id|>, <|eot_id|>
    elif "llama" in args.model_name.lower():
        generation_kwargs["stop_token_ids"] = [128001, 128009]
    

    # Perform translation in batches
    translations = []
    trans_prompts = []
    if args.is_conversation:
        for doc in source_texts:
            trans_prompt = []
            for text in doc:
                text = get_trans_prompt(text, args.lang_direction, args.is_icl, args.is_tower, args.is_og, args.shot_num)
                trans_prompt.append(text)
            trans_prompts.append(trans_prompt)
    # print('len(trans_prompts)', len(trans_prompts))
    
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    ref_token_counts = []
    # Initialize the VLLM Agent with the specified translation model
    translator = VllmAgent(model_name=args.model_name, model_kwargs=vllm_kwargs, generation_kwargs=generation_kwargs)

    if args.is_segment:
        for doc in source_texts:
            trans_prompt = []
            for text in doc:
                text = get_trans_prompt(text, args.lang_direction, args.is_icl, args.is_tower, args.is_og, args.shot_num)
                #trans_prompt.append(text)
                if isinstance(tokenizer, GemmaTokenizer) or isinstance(tokenizer, GemmaTokenizerFast):
                    if text[0]['role'] == 'system':
                        system_prompt = text.pop(0)['content']
                        text[0]['content'] = system_prompt + "\n" + text[0]['content']
                if 'LongWriter' in args.model_name:
                    text[0]['content'] = text[0]['content'] + '\n' + text[1]['content']
                    #print(text[0]['content'])
                    text = f"[INST]{text[0]['content']}[/INST]"
                else:
                    text = tokenizer.apply_chat_template(text, add_generation_prompt=True, tokenize=False)
                trans_prompt.append(text)
            trans_prompts.append(trans_prompt)
    elif not args.is_segment and not args.is_conversation:
        for text in source_texts:
            text = get_trans_prompt(text, args.lang_direction, args.is_icl, args.is_tower, args.is_og, args.shot_num)
            # trans_prompts.append(text)
            if isinstance(tokenizer, GemmaTokenizer) or isinstance(tokenizer, GemmaTokenizerFast):
                if text[0]['role'] == 'system':
                    system_prompt = text.pop(0)['content']
                    text[0]['content'] = system_prompt + "\n" + text[0]['content']
            if 'LongWriter' in args.model_name:
                text[0]['content'] = text[0]['content'] + '\n' + text[1]['content']
                #print(text[0]['content'])
                text = f"[INST]{text[0]['content']}[/INST]"
            else:
                text = tokenizer.apply_chat_template(text, add_generation_prompt=True, tokenize=False)
            trans_prompts.append(text)
    # Prepare prompts for translation
    # Generate translations
    translations = []
    res_all_list = []
    translations_split = []
    if args.is_conversation:
        for trans_prompt in tqdm(trans_prompts):
            prev_prefix = []
            res_all = ' '
            translation_split = []
            for text in trans_prompt:
                #prev_prefix.append(text[-1])
                # translation_split = []
                if len(prev_prefix) == 0:
                    prev_prefix = text
                    text = tokenizer.apply_chat_template(prev_prefix, add_generation_prompt=True, tokenize=False)
                else:
                    # avoid OOM errors when cases are too long, hyperparameter is heuristic
                    if len(prev_prefix) > 50:
                        prev_prefix = [prev_prefix[0]] + prev_prefix[-6:]
                    prev_prefix.append(text[-1])
                    text = tokenizer.apply_chat_template(prev_prefix, add_generation_prompt=True, tokenize=False)
                #print(text)
                output = translator.generate([text])[0][0]
                #print(output[0])
                res = {'role': 'assistant', 'content': output}
                #print(output[0][0])
                prev_prefix.append(res)
                if args.is_tower or args.is_og:
                    res['content'] = remove_triple_backlashes(res['content'])
                    res_all += res['content'] + ' '
                    translation_split.append(res['content'])
                else:
                    res_all += res['content'][len('Translation: '):] + ' '
                    translation_split.append(res['content'][len('Translation: '):])
                del output, text
            translations.append(res_all)
            translations_split.append(translation_split)
    elif args.is_segment:
        batch_translation = []
        # input all paragraphs as a list or input one by one, there is no algorithm level difference but input whole is faster due to vllm.
        if args.one_by_one:
            for trans_prompt in tqdm(trans_prompts):
                batch_translation = []
                for sentence in trans_prompt:
                    trans_sentence = translator.generate([sentence])
                    #print(trans_sentence[0][0])
                    batch_translation.append([trans_sentence[0][0]])
                translations.append(batch_translation)
        else:
            for trans_prompt in trans_prompts:
                batch_translation = translator.generate(trans_prompt)
                translations.append(batch_translation)
    else:
        batch_translations = []
        if args.one_by_one:
            for doc in trans_prompts:
                trans_sentence = translator.generate([doc])
                trans_sentence = trans_sentence[0][0]
                trans_sentence = remove_triple_backlashes(trans_sentence)
                batch_translations.append(trans_sentence)
        else:
            batch_translations = translator.generate(trans_prompts)
            for i in range(len(batch_translations)):
                if args.is_tower or args.is_og:
                    batch_translations[i] = batch_translations[i][0]
                    batch_translations[i] = remove_triple_backlashes(batch_translations[i])
                else:
                    batch_translations[i] = batch_translations[i][0][len('Translation: '):]
        translations.extend(batch_translations)

    # process the translations and references
    
    if args.is_segment:
        translations_split = []
        for i in range(len(translations)):
            translation_split = []
            processed_translations = ''
            for j in range(len(translations[i])):
                if args.is_tower or args.is_og:
                    translations[i][j] = translations[i][j][0]
                    translations[i][j] = remove_triple_backlashes(translations[i][j])
                else:
                    translations[i][j] = translations[i][j][0][len('Translation: '):]
                processed_translations += translations[i][j] + ' '
                translation_split.append(translations[i][j])
            translations[i] = processed_translations
            translations_split.append(translation_split)
        #print('translations', translations)
    references_split = copy.deepcopy(references)
    #print('references_split', references_split)
    if args.is_segment or args.is_conversation:
        for i in range(len(references)):
            processed_references = ''
            for j in range(len(references[i])):
                processed_references += references[i][j] + ' '
            references[i] = processed_references
    
    translated_token_counts = []
    ref_token_counts = []
    batch_encodings = tokenizer(translations, return_attention_mask=False, return_token_type_ids=False)
    batch_token_counts = [len(enc) for enc in batch_encodings['input_ids']]
    translated_token_counts.extend(batch_token_counts)
    batch_encodings = tokenizer(references, return_attention_mask=False, return_token_type_ids=False)
    batch_token_counts = [len(enc) for enc in batch_encodings['input_ids']]
    ref_token_counts.extend(batch_token_counts)
    # save_as_txt(args.output_file[:-len('.json')] + '', translations_split)
    if not args.is_conversation and not args.is_segment:
        with open(args.output_file[:-len('.json')] + '_gen.jsonl', 'w', encoding='utf-8') as f:
            for original, translation, ref_token_count, translated_token_count, reference in zip(source_texts, translations, ref_token_counts, translated_token_counts, references):
                json_line = json.dumps({
                    'original': original,
                    'translation': translation,
                    'reference': reference,
                    'ref_token': ref_token_count,
                    'translated_token': translated_token_count,
                    'token ratio': translated_token_count / ref_token_count,
                }, ensure_ascii=False)
                f.write(json_line + '\n')
    else:
        with open(args.output_file[:-len('.json')] + '_gen.jsonl', 'w', encoding='utf-8') as f:
            for original, translation, ref_token_count, translated_token_count, reference, reference_split, translation_split in zip(source_texts, translations, ref_token_counts, translated_token_counts, references, references_split,translations_split):
                json_line = json.dumps({
                    'original': original,
                    'translation': translation,
                    'translation_split': translation_split,
                    'reference': reference,
                    'reference_split': reference_split,
                    'ref_token': ref_token_count,
                    'translated_token': translated_token_count,
                    'token ratio': translated_token_count / ref_token_count,
                }, ensure_ascii=False)
                f.write(json_line + '\n')
    print(f"Translations saved to {args.output_file}")

