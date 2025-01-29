#!/usr/bin/env bash
SRC_LANG=$1
TGT_LANG=$2
SETTING=$3
DATA_PATH=$4
MODEL_NAME_PATH=$5
MODEL_NAME=$(basename $MODEL_NAME_PATH)
mkdir -p outputs/${MODEL_NAME}
NUM=-1  # -1 means all data
export OPENAI_API_KEY=${OPENAI_API_KEY}

if [ "$SETTING" == "mturn_icl" ]; then
  python3 translate_gpt.py \
    --source_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${SRC_LANG}.txt \
    --target_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${TGT_LANG}.txt \
    --model_name $MODEL_NAME_PATH \
    --output_file outputs/${MODEL_NAME}/wmt2024_${SRC_LANG}-${TGT_LANG}_mturn_icl.jsonl \
    --is_icl \
    --is_og \
    --max_new_tokens 512 \
    --is_conversation \
    --lang_direction "${SRC_LANG}-${TGT_LANG}" \
    --data_num "${NUM}"
elif [ "$SETTING" == "seg_icl" ]; then
  python3 translate_gpt.py \
    --source_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${SRC_LANG}.txt \
    --target_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${TGT_LANG}.txt \
    --model_name $MODEL_NAME_PATH \
    --output_file outputs/${MODEL_NAME}/wmt2024_${SRC_LANG}-${TGT_LANG}_seg_icl.jsonl \
    --is_segment \
    --is_icl \
    --is_og \
    --max_new_tokens 512 \
    --lang_direction "${SRC_LANG}-${TGT_LANG}" \
    --data_num "${NUM}"
elif [ "$SETTING" == "mturn" ]; then
  python3 translate_gpt.py \
    --source_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${SRC_LANG}.txt \
    --target_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${TGT_LANG}.txt \
    --model_name $MODEL_NAME_PATH \
    --output_file outputs/${MODEL_NAME}/wmt2024_${SRC_LANG}-${TGT_LANG}_mturn.jsonl \
    --is_conversation \
    --is_og \
    --max_new_tokens 512 \
    --lang_direction "${SRC_LANG}-${TGT_LANG}" \
    --data_num "${NUM}"
elif [ "$SETTING" == "seg" ]; then
  python3 translate_gpt.py \
    --source_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${SRC_LANG}.txt \
    --target_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${TGT_LANG}.txt \
    --model_name $MODEL_NAME_PATH \
    --output_file outputs/${MODEL_NAME}/wmt2024_${SRC_LANG}-${TGT_LANG}_seg.jsonl \
    --is_segment \
    --is_og \
    --max_new_tokens 512 \
    --lang_direction "${SRC_LANG}-${TGT_LANG}" \
    --data_num "${NUM}"
elif [ "$SETTING" == "single" ]; then
  python3 translate_gpt.py \
    --source_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${SRC_LANG}.txt \
    --target_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${TGT_LANG}.txt \
    --model_name $MODEL_NAME_PATH \
    --output_file outputs/${MODEL_NAME}/wmt2024_${SRC_LANG}-${TGT_LANG}_single.jsonl \
    --is_og \
    --lang_direction "${SRC_LANG}-${TGT_LANG}" \
    --data_num "${NUM}"
elif [ "$SETTING" == "single_icl" ]; then
  python3 translate_gpt.py \
    --source_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${SRC_LANG}.txt \
    --target_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${TGT_LANG}.txt \
    --model_name $MODEL_NAME_PATH \
    --output_file outputs/${MODEL_NAME}/wmt2024_${SRC_LANG}-${TGT_LANG}_single_icl.jsonl \
    --is_icl \
    --is_og \
    --lang_direction "${SRC_LANG}-${TGT_LANG}" \
    --data_num "${NUM}"
fi

