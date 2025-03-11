LANG_PAIRS="ja-zh"
# LANG_PAIRS="ja-zh cs-uk"
# LANG_PAIRS="zh-en"
SETTINGS="mturn_icl_context"
# MODEL_NAME="Qwen2.5-7B-Instruct"
MODEL_NAME="gpt-4o-mini"

for lang_pair in $LANG_PAIRS; do
    for setting in $SETTINGS; do
        python eval/eval.py --lang_pairs $lang_pair --model_name $MODEL_NAME --tgt_file wmt2024 --data_type jsonl --is_ours True --setting $setting --metric bleu
    done
done