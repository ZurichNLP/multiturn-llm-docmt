TARGET_LANGS="cs de es hi is ja ru uk zh"
MODEL_NAME_PATH=gpt-4o-mini
SETTINGS="mturn mturn_icl seg seg_icl single single_icl"
for setting in $SETTINGS; do
    for lang in $TARGET_LANGS; do
        bash scripts/run_trans_gpt_split.sh en $lang $setting wmt24_processed $MODEL_NAME_PATH
    done
    bash scripts/run_trans_gpt_split.sh cs uk $setting wmt24_processed $MODEL_NAME_PATH
    bash scripts/run_trans_gpt_split.sh ja zh $setting wmt24_processed $MODEL_NAME_PATH
done
