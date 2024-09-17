# CTKFacts EN Dataset

The original dataset was obtained from [Hugging Face](https://huggingface.co/datasets/ctu-aic/ctkfacts_nli).

### Dataset details

- Language: EN (Translated)
- Task: Natural Language Inference
- Samples: 558 (Test set)
- Few-shot examples: 5 (From training set)
- [Hugging Face link](https://huggingface.co/datasets/CIIRC-NLP/ctkfacts_nli-en)

### Task description

The model is asked to determine the correct relation between a premise and a hypothesis. The premise can confirm the hypothesis, refute it, or there can be no clear relation.
This leads to a three-class classification problem.

The reported metrics are classification accuracy (exact_match) and macro-averaged F1 score.

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

