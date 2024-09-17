# TruthfulQA dataset

The original English dataset was obtained from [Hugging Face](https://huggingface.co/datasets/truthful_qa).

Only the single-choice (mc1) variant of the dataset was kept, and the ordering of proposed answers was randomized.

### Dataset details

- Language: CS (Translated)
- Task: Knowledge-Based Question Answering
- Samples: 817 (Validation set)
- Few-shot examples: 5 (From validation set, excluded from evaluation)
- [Hugging Face link](https://huggingface.co/datasets/CIIRC-NLP/truthful_qa-shuffled)

### Task description

The model is given a question targeted at common misinformation and a variable-sized set of possible answers, only one of which is correct. It is expected to return the number corresponding to the chosen answer.

The reported accuracy metric (exact_match) represents the percentage of correctly selected answers.

## Citation

```bibtex
@misc{lin2021truthfulqa,
    title={TruthfulQA: Measuring How Models Mimic Human Falsehoods},
    author={Stephanie Lin and Jacob Hilton and Owain Evans},
    year={2021},
    eprint={2109.07958},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}

```
