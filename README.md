# MTurn_MT

## 1. Installation:

```bash
bash scripts/start_vllm.sh
```

## 2. Prepare data

We get and parse the data from the WMT24 dataset (https://www2.statmt.org/wmt24/translation-task.html), you can also directly use our parsed data in `wmt24_processed`.

## 3. Run translation

If you need to use gpt models to translate the data, you should first set your OPENAI_API_KEY:

```bash
export OPENAI_API_KEY=your_api_key
```

Then you can run the following command to translate the data:

```bash
bash scripts/run_gpt.sh
```

If you don't need to use gpt models, you can run the following command to translate the data:

```bash
bash scripts/run.sh
```

## 4. Evaluate the translation

If you need to evaluate through dBLEU, run the following command:

```bash
bash eval/eval.sh
```

If you need to evaluate through Comet, run the following command:

```bash
bash eval/eval_comet.sh
```
