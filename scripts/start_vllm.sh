pip3 install accelerate deepspeed peft bitsandbytes tokenizers evaluate

pip install packaging
pip install ninja

pip install wandb

cd ..
git clone https://github.com/vllm-project/vllm.git
cd vllm
pip install -e .

pip uninstall flash-attn -y

pip3 install -U flash-attn --no-cache-dir

pip uninstall antlr4-python3-runtime -y

pip install antlr4-python3-runtime==4.11

pip install -U openai

pip install cohere

pip install rouge bert_score

# # Get CUDA version using nvcc
# CUDA_VERSION=$(nvcc -V | grep "release" | awk '{print $5}' | cut -d',' -f1 | tr -d '.')
# pip install flashinfer -i https://flashinfer.ai/whl/cu${CUDA_VERSION}/torch2.4/

export HF_HOME=/mnt/data/.cache/huggingface
export HF_TRANSFORMERS_CACHE=/mnt/data/.cache/transformers
export HF_DATASETS_CACHE=/mnt/data/.cache/datasets

git config --global credential.helper store
pip install sacrebleu
pip install mecab-python3
pip install sacrebleu[ja]
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
cd ../
git clone https://github.com/EleanorJiang/BlonDe
cd BlonDe
pip install .

