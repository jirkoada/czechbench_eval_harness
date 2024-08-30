# CTKFacts Dataset

This dataset was obtained from [Hugging Face](https://huggingface.co/datasets/ctu-aic/ctkfacts_nli).

### Dataset details

- Language: CS (Original)
- Task: Natural Language Inference
- Samples: 558 (Test set)
- Few-shot examples: 5 (From training set)

### Task description

Natural language inference is a 3-class classification problem. Each example consists of a premise text passage and a hypothesis. The premise can either support the hypothesis, refute it, or not provide enough information for either case. The model is given a premise-hypothesis pair and asked to correctly determine their relation. It replies with a number from 0 to 2 assigned to one of the classes.

The reported metrics are classification accuracy and macro-averaged F1 score.

## License

The dataset has no license specified by its authors.

## References

[1] Ullrich et al., [CsFEVER and CTKFacts: Acquiring Czech data for fact verification](https://arxiv.org/abs/2201.11115), 2022
