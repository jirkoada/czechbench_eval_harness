# Czech MMLU dataset

The original English dataset was obtained from [Hugging Face](https://huggingface.co/datasets/cais/mmlu).

The translation was performed automatically using the [wmt21-dense-24-wide-en-x](https://huggingface.co/facebook/wmt21-dense-24-wide-en-x) model. For details, refer to the [dataset translation script](../dataset_translation.py).

The professional_law and us_foreign_policy subtasks are excluded from the evaluation, due to large inference expenses and low relevance to the Czech cultural setting.

### Dataset details

- Language: CS (Translated)
- Task: Knowledge-Based Question Answering
- Samples: 12508 (Test set)
- Few-shot examples: 5 (From the development set for each topic)
- [Hugging Face link](https://huggingface.co/datasets/CIIRC-NLP/mmlu-cs)

### Task description

MMLU consists of 57 separate subtasks, 55 of which are used here. Each subtask's examples are formatted as single-choice questions with 4 available answers. The model is asked to return a number from 1 to 4, corresponding to the chosen answer.

Accuracies for all 55 subtasks are reported, as well as an average accuracy over all test samples.

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
