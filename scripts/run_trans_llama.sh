#!/usr/bin/env bash

# MODEL_NAME_PATH=Meta-Llama/Meta-Llama-3.1-8B-Instruct
# MODEL_NAME=Meta-Llama-3.1-8B-Instruct
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
export TORCH_USE_CUDA_DSA=1
SRC_LANG=$1
TGT_LANG=$2
SETTING=$3
DATA_PATH=$4
MODEL_NAME_PATH=$5
MODEL_NAME=$(basename $MODEL_NAME_PATH)
mkdir -p outputs/${MODEL_NAME}
NUM=-1  # -1 means all data
DEVICES=0,1,2,3
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
export CUDA_LAUNCH_BLOCKING=1

if [ "$SETTING" == "mturn_icl" ]; then
  NCCL_DEBUG=INFOCUDA_VISIBLE_DEVICES="${DEVICES}" python3 translate.py \
    --source_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${SRC_LANG}.txt \
    --target_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${TGT_LANG}.txt \
    --model_name $MODEL_NAME_PATH \
    --output_file outputs/${MODEL_NAME}/wmt2024_${SRC_LANG}-${TGT_LANG}_mturn_icl.jsonl \
    --is_icl \
    --is_og \
    --is_conversation \
    --max_new_tokens 512 \
    --gpu_memory_utilization 0.9 \
    --lang_direction "${SRC_LANG}-${TGT_LANG}" \
    --data_num "${NUM}"
elif [ "$SETTING" == "seg_icl" ]; then
  NCCL_DEBUG=INFO CUDA_VISIBLE_DEVICES="${DEVICES}" python3 translate.py \
    --source_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${SRC_LANG}.txt \
    --target_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${TGT_LANG}.txt \
    --model_name $MODEL_NAME_PATH \
    --output_file outputs/${MODEL_NAME}/wmt2024_${SRC_LANG}-${TGT_LANG}_seg_icl.jsonl \
    --is_segment \
    --is_icl \
    --is_og \
    --max_new_tokens 512 \
    --gpu_memory_utilization 0.9 \
    --lang_direction "${SRC_LANG}-${TGT_LANG}" \
    --data_num "${NUM}"
elif [ "$SETTING" == "mturn" ]; then
  NCCL_DEBUG=INFO CUDA_VISIBLE_DEVICES="${DEVICES}" python3 translate.py \
    --source_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${SRC_LANG}.txt \
    --target_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${TGT_LANG}.txt \
    --model_name $MODEL_NAME_PATH \
    --output_file outputs/${MODEL_NAME}/wmt2024_${SRC_LANG}-${TGT_LANG}_mturn.jsonl \
    --is_conversation \
    --is_og \
    --max_new_tokens 512 \
    --gpu_memory_utilization 0.9 \
    --lang_direction "${SRC_LANG}-${TGT_LANG}" \
    --data_num "${NUM}"
elif [ "$SETTING" == "seg" ]; then
  NCCL_DEBUG=INFO CUDA_VISIBLE_DEVICES="${DEVICES}" python3 translate.py \
    --source_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${SRC_LANG}.txt \
    --target_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${TGT_LANG}.txt \
    --model_name $MODEL_NAME_PATH \
    --output_file outputs/${MODEL_NAME}/wmt2024_${SRC_LANG}-${TGT_LANG}_seg.jsonl \
    --is_segment \
    --is_og \
    --max_new_tokens 512 \
    --gpu_memory_utilization 0.95 \
    --lang_direction "${SRC_LANG}-${TGT_LANG}" \
    --data_num "${NUM}"
elif [ "$SETTING" == "single" ]; then
  NCCL_DEBUG=INFO CUDA_VISIBLE_DEVICES="${DEVICES}" python3 translate.py \
    --source_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${SRC_LANG}.txt \
    --target_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${TGT_LANG}.txt \
    --model_name $MODEL_NAME_PATH \
    --output_file outputs/${MODEL_NAME}/wmt2024_${SRC_LANG}-${TGT_LANG}_single.jsonl \
    --is_og \
    --gpu_memory_utilization 0.95 \
    --lang_direction "${SRC_LANG}-${TGT_LANG}" \
    --data_num "${NUM}"
elif [ "$SETTING" == "single_icl" ]; then
  NCCL_DEBUG=INFO CUDA_VISIBLE_DEVICES="${DEVICES}" python3 translate.py \
    --source_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${SRC_LANG}.txt \
    --target_file ${DATA_PATH}/wmt24_${SRC_LANG}-${TGT_LANG}.${TGT_LANG}.txt \
    --model_name $MODEL_NAME_PATH \
    --output_file outputs/${MODEL_NAME}/wmt2024_${SRC_LANG}-${TGT_LANG}_single_icl.jsonl \
    --is_icl \
    --is_og \
    --gpu_memory_utilization 0.95 \
    --lang_direction "${SRC_LANG}-${TGT_LANG}" \
    --data_num "${NUM}"
fi


# CUDA_VISIBLE_DEVICES=${DEVICES} python3 translate.py \
#   --source_file ../wmt_devsets/wmt24_en_${LANG}.txt \
#   --target_file ../wmt_devsets/wmt24_${LANG}.txt \
#   --model_name $MODEL_NAME_PATH \
#   --output_file outputs1/${MODEL_NAME}/wmt2024_en_${LANG}_conv_${NUM}.jsonl \
#   --is_conversation \
#   --gpu_memory_utilization 0.9 \
#   --lang_direction en-${LANG} \
#   --data_num ${NUM} \

# CUDA_VISIBLE_DEVICES=${DEVICES} python3 translate.py \
#   --source_file ../wmt_devsets/wmt24_en_${LANG}.txt \
#   --target_file ../wmt_devsets/wmt_seg/wmt24_${LANG}.txt \
#   --model_name $MODEL_NAME_PATH \
#   --output_file outputs1/${MODEL_NAME}/wmt2024_en_${LANG}_${NUM}.jsonl \
#   --lang_direction en-${LANG} \
#   --data_num ${NUM} \

# CUDA_VISIBLE_DEVICES=${DEVICES} python3 translate.py \
#   --source_file ../wmt_devsets/wmt24_en_${LANG}.txt \
#   --target_file ../wmt_devsets/wmt24_${LANG}.txt \
#   --model_name $MODEL_NAME_PATH \
#   --output_file outputs1/${MODEL_NAME}/wmt2024_en_${LANG}_all_icl_1shot.jsonl \
#   --is_icl \
#   --lang_direction en-${LANG} \
#   --data_num ${NUM} \

# CUDA_VISIBLE_DEVICES=${DEVICES} python3 translate.py \
#   --source_file ../wmt_devsets/wmt24_en_${LANG}.txt \
#   --target_file ../wmt_devsets/wmt24_${LANG}.txt \
#   --model_name $MODEL_NAME_PATH \
#   --output_file outputs1/${MODEL_NAME}/wmt2024_en_${LANG}_seg_icl_1shot.jsonl \
#   --is_segment \
#   --is_icl \
#   --lang_direction en-${LANG} \
#   --data_num ${NUM} \

# CUDA_VISIBLE_DEVICES=${DEVICES} python3 translate.py \
#   --source_file ../wmt_devsets/wmt24_en_${LANG}.txt \
#   --target_file ../wmt_devsets/wmt24_${LANG}.txt \
#   --model_name $MODEL_NAME_PATH \
#   --output_file outputs1/${MODEL_NAME}/wmt2024_en_${LANG}_seg_${NUM}.jsonl \
#   --is_segment \
#   --lang_direction en-${LANG} \
#   --data_num ${NUM} \
