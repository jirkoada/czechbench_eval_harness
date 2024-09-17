# ANLI Dataset

### Dataset details

- Language: EN (Original)
- Task: Natural Language Inference
- Samples: 1200 (Test set)
- Few-shot examples: 5 (From training set)
- [Hugging Face link](https://huggingface.co/datasets/facebook/anli)

### Task description

The model is asked to determine the correct relation between a premise and a hypothesis. The premise can confirm the hypothesis, refute it, or there can be no clear relation.
This leads to a three-class classification problem.

The reported metrics are classification accuracy (exact_match) and macro-averaged F1 score.


## Citation

```bibtex
@InProceedings{nie2019adversarial,
    title={Adversarial NLI: A New Benchmark for Natural Language Understanding},
    author={Nie, Yixin
                and Williams, Adina
                and Dinan, Emily
                and Bansal, Mohit
                and Weston, Jason
                and Kiela, Douwe},
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    year = "2020",
    publisher = "Association for Computational Linguistics",
}
```

