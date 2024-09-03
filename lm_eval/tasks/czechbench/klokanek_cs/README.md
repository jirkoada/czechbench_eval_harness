# Klokánek dataset

This dataset was obtained from [Hugging Face](https://huggingface.co/datasets/hynky/klokan-qa).

### Dataset details

- Language: CS (Original)
- Task: Logical/Mathematical Inference
- Samples: 813 (Training set)
- Few-shot examples: 5 (From training set, excluded from evaluation)
- [Hugging Face link](https://huggingface.co/datasets/hynky/klokan-qa).

### Task description

The model is given a challenging word problem and a set of 5 possible answers marked with letters from A to E. It is asked to only return the letter corresponding to the chosen answer.

The reported accuracy metric (exact match) represents the percentage of correctly selected answers.

## Citation

```bibtex
@misc{klokanek-dataset,
  author = {Hynek Kydlíček, David Nocar et al.},
  title = {Klokánek dataset},
  year = {2023},
  publisher = {Hynek Kydlíček},
  doi       = { 10.57967/hf/1608 },
  url = {https://matematickyklokan.net/}
  howpublished = "\url{https://huggingface.co/datasets/hynky/klokan-qa}"
}
```
