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

### Task description

The model is presented with a question and a selection of (typically 4) possible answers. It needs to return a letter (A, B, C, ...) corresponding to the correct answer.

The reported accuracy metric represents the percentage of correctly selected answers.

## License

The dataset is licensed under [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## References

[1] Clark et al., [Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge](https://arxiv.org/abs/1803.05457), 2018
