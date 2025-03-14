TARGET_LANGS="cs de es hi is ja ru uk zh"
MODEL_NAME_PATH=gpt-4o-mini
SETTINGS="single single_icl seg seg_icl mturn mturn_icl mturn_contextmturn_icl_context"
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY_HERE"
for setting in $SETTINGS; do
    for lang in $TARGET_LANGS; do
        bash scripts/run_trans_gpt_split.sh en $lang $setting wmt24_processed $MODEL_NAME_PATH
    done
    bash scripts/run_trans_gpt_split.sh cs uk $setting wmt24_processed $MODEL_NAME_PATH
    bash scripts/run_trans_gpt_split.sh ja zh $setting wmt24_processed $MODEL_NAME_PATH
done
