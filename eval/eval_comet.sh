# LANG_PAIRS="en-cs en-de en-es en-hi en-is en-ja en-ru en-uk en-zh cs-uk ja-zh"
LANG_PAIRS="en-de en-zh"
SETTINGS="seg seg_icl"
for lang_pair in $LANG_PAIRS; do
    for setting in $SETTINGS; do
        python eval/eval.py --lang_pairs $lang_pair --model_name gpt-4o-mini --tgt_file wmt2024 --data_type jsonl --metric comet --is_ours True --setting $setting
    done
done