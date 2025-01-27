# LANG_PAIRS="en-cs en-de en-es en-hi en-is en-ja en-ru en-uk en-zh cs-uk ja-zh"
LANG_PAIRS="en-ja"
SETTINGS="mturn"
MODEL_NAME="TowerInstruct-7B-v0.2"
for lang_pair in $LANG_PAIRS; do
    for setting in $SETTINGS; do
        python eval/eval.py --lang_pairs $lang_pair --model_name $MODEL_NAME --tgt_file wmt2024 --data_type jsonl --is_ours True --setting $setting --metric bleu
    done
done