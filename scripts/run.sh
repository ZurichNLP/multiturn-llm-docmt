MODEL_NAME_PATH=Qwen/Qwen2.5-7B-Instruct # MODEL_NAME_PATH=Meta-Llama/Meta-Llama-3.1-8B-Instruct
TARGET_LANGS="cs de es hi is ja ru uk zh"
SETTINGS="single single_icl seg seg_icl mturn mturn_icl mturn_context mturn_icl_context"
for setting in $SETTINGS; do
    for lang in $TARGET_LANGS; do
        bash scripts/run_trans_llama.sh en $lang $setting wmt24_processed $MODEL_NAME_PATH
    done
    bash scripts/run_trans_llama.sh cs uk $setting wmt24_processed $MODEL_NAME_PATH
    bash scripts/run_trans_llama.sh ja zh $setting wmt24_processed $MODEL_NAME_PATH 
done