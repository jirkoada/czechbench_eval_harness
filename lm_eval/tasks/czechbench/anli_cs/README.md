# Czech ANLI Dataset

This dataset was obtained from [Hugging Face](https://huggingface.co/datasets/ctu-aic/anli_cs).

### Dataset details

- Language: CS (Translated)
- Task: Natural Language Inference
- Samples: 1200 (Test set)
- Few-shot examples: 5 (From training set)
- [Hugging Face link](https://huggingface.co/datasets/ctu-aic/anli_cs)

### Task description

The model is asked to determine the correct relation between a premise and a hypothesis. The premise can confirm the hypothesis, refute it, or there can be no clear relation.
This leads to a three-class classification problem.

The reported metrics are classification accuracy (exact_match) and macro-averaged F1 score.


## Citation

```bibtex
@masterthesis{ullrich-thesis,
    author = {Ullrich, Herbert},
    title = {Dataset for Automated Fact Checking in Czech Language},
    school = {Czech Technical University in Prague, Faculty of Electrical Engineering},
    year = 2021,
    URL = {https://dspace.cvut.cz/handle/10467/95430}
}
```

