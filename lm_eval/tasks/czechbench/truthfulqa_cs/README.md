# Czech TruthfulQA dataset

The original English dataset was obtained from [Hugging Face](https://huggingface.co/datasets/truthful_qa).

The translation was performed automatically using the [wmt21-dense-24-wide-en-x](https://huggingface.co/facebook/wmt21-dense-24-wide-en-x) model. For details, refer to the [dataset translation script](../dataset_translation.py). Only the single-choice (mc1) variant of the dataset is used, and the ordering of proposed answers is randomized.

### Dataset details

- Language: CS (Translated)
- Task: Knowledge-Based Question Answering
- Samples: 817 (Validation set)
- Few-shot examples: 5 (From validation set, excluded from evaluation)
- [Hugging Face link](https://huggingface.co/datasets/CIIRC-NLP/truthful_qa-cs)

### Task description

The model is given a question targeted at common misinformation and a variable-sized set of possible answers, only one of which is correct. It is expected to return the number corresponding to the chosen answer.

The reported accuracy metric (exact_match) represents the percentage of correctly selected answers.

## Citation

```bibtex
@masterthesis{jirkovsky-thesis,
    author = {Jirkovský, Adam},
    title = {Benchmarking Techniques for Evaluation of Large Language Models},
    school = {Czech Technical University in Prague, Faculty of Electrical Engineering},
    year = 2024,
    URL = {https://dspace.cvut.cz/handle/10467/115227}
}
```
