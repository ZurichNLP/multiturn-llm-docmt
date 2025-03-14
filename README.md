# Source-primed Multi-turn Conversation Helps LLMs Translate Documents

This is the code to replicate the Source-primed Multi-turn Translation in the paper [Source-primed Multi-turn Conversation Helps Large Language Models
Translate Documents](https://arxiv.org/pdf/2503.10494). [[cite]](#citation)

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
'mturn_icl_context' means our source-primed multi-turn translation, 'mturn_icl' and 'mturn' is multi-turn without source-primed.

## 4. Evaluate the translation

If you need to evaluate through dBLEU, run the following command:

```bash
bash eval/eval.sh
```

If you need to evaluate through Comet, run the following command:

```bash
bash eval/eval_comet.sh
```


## Citation
Please consider citing us if you use our materials.
```
@misc{hu2025sourceprimedmultiturnconversationhelps,
      title={Source-primed Multi-turn Conversation Helps Large Language Models Translate Documents}, 
      author={Hanxu Hu and Jannis Vamvas and Rico Sennrich},
      year={2025},
      eprint={2503.10494},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2503.10494}, 
}
```
