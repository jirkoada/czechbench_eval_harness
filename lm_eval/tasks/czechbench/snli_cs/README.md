# Czech SNLI Dataset

This dataset was obtained from [Hugging Face](https://huggingface.co/datasets/ctu-aic/snli_cs).

### Dataset details

- Language: CS (Translated)
- Task: Natural Language Inference
- Samples: 10000 (Test set)
- Few-shot examples: 5 (From training set)

### Task description

Natural language inference is a 3-class classification problem. Each example consists of a premise text passage and a hypothesis. The premise can either support the hypothesis, refute it, or not provide enough information for either case. The model is given a premise-hypothesis pair and asked to correctly determine their relation. It replies with a number from 0 to 2 assigned to one of the classes.

The reported metrics are classification accuracy and macro-averaged F1 score.

## License

The dataset is licensed under [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## References

[1] Ullrich, [Dataset for Automated Fact Checking in Czech
Language](https://dspace.cvut.cz/bitstream/handle/10467/95430/F3-DP-2021-Ullrich-Herbert-Thesis___Ullrich.pdf?sequence=-1&isAllowed=y), 2021

[2] Bowman et al., [A large annotated corpus for learning natural language inference](https://arxiv.org/abs/1508.05326v1), 2015

