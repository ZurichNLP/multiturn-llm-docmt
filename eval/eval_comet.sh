LANG_PAIRS="en-cs en-de en-es en-hi en-is en-ja en-ru en-uk en-zh cs-uk ja-zh"
SETTINGS="mturn mturn_icl seg seg_icl"
for lang_pair in $LANG_PAIRS; do
    for setting in $SETTINGS; do
        python eval/eval.py --lang_pairs $lang_pair --model_name Meta-Llama-3.1-8B-Instruct --tgt_file wmt2024 --data_type jsonl --metric comet --is_ours True --setting $setting
    done
done