LANG_PAIRS="ja-zh"
SETTINGS="mturn_icl_context"
# MODEL_NAME="Qwen2.5-7B-Instruct"
MODEL_NAME="gpt-4o-mini"
for lang_pair in $LANG_PAIRS; do
    for setting in $SETTINGS; do
        python eval/eval.py --lang_pairs $lang_pair --model_name $MODEL_NAME --tgt_file wmt2024 --data_type jsonl --metric comet --is_ours True --setting $setting
    done
done

# MODEL_NAME="Meta-Llama-3.1-8B-Instruct"
# for lang_pair in $LANG_PAIRS; do
#     for setting in $SETTINGS; do
#         python eval/eval.py --lang_pairs $lang_pair --model_name $MODEL_NAME --tgt_file wmt2024 --data_type jsonl --metric comet --is_ours True --setting $setting
#     done
# done