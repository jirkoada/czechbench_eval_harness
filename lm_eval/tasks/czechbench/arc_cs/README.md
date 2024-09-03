# Czech ARC dataset

The original English dataset was obtained from [Hugging Face](https://huggingface.co/datasets/allenai/ai2_arc).

The translation was performed automatically using the [wmt21-dense-24-wide-en-x](https://huggingface.co/facebook/wmt21-dense-24-wide-en-x) model. For details, refer to the [dataset translation script](../dataset_translation.py).

### Dataset details

- Language: CS (Translated)
- Task: Knowledge-Based Question Answering
- Subsets:
    - Challenge: 1172 test samles
    - Easy: 2376 test samles
- Few-shot examples: 5 (From ARC Challenge validation set)
- [Hugging Face link](https://huggingface.co/datasets/CIIRC-NLP/arc-cs)

### Task description

The model is presented with a question and a selection of (typically 4) possible answers. It needs to return a letter (A, B, C, ...) corresponding to the correct answer.

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
