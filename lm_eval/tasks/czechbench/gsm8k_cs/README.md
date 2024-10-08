# Czech GSM8K dataset

The original English dataset was obtained from [Hugging Face](https://huggingface.co/datasets/gsm8k).

The translation was performed automatically using the [wmt21-dense-24-wide-en-x](https://huggingface.co/facebook/wmt21-dense-24-wide-en-x) model. For details, refer to the [dataset translation script](../dataset_translation.py).

The original dataset structure has been slightly altered by splitting the answer field into the 'thoughts' field, containing the translation of the thought process stripped of the calculation commands enclosed in '<<>>', and the 'answer' field, containing the final numerical answer as an integer.

### Dataset details

- Language: CS (Translated)
- Task: Mathematical inference
- Samples: 1319 (Test set)
- Few-shot examples: 5 (From training set)
- [Hugging Face link](https://huggingface.co/datasets/CIIRC-NLP/gsm8k-cs)

### Task description

The model is presented with a math word problem. It is asked to describe its solution step by step, and then mark the final numerical answer with a preceding '####' token.

The main evaluation accuracy metric (exact_match) represents the percentage of final numerical answers exactly matching the references.

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
