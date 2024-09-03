# Belebele (CS) dataset

The dataset was obtained from [Hugging Face](https://huggingface.co/datasets/facebook/belebele).

### Dataset details

- Language: CS (Human translation)
- Task: Question Answering / Reading Comprehension
- Samples: 900 (Test set)
- Few-shot examples: 5 (From test set, excluded from evaluation)
- [Hugging Face link](https://huggingface.co/datasets/facebook/belebele)

### Task description

The model is presented with a source passage, a question related to that passage and a selection of 4 possible answers. It needs to return a number (1 to 4) corresponding to the correct answer.

The reported accuracy metric (exact_match) represents the percentage of correctly selected answers.


## Citation

```bibtex
@inproceedings{bandarkar-etal-2024-belebele,
    title = "The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants",
    author = "Bandarkar, Lucas  and
      Liang, Davis  and
      Muller, Benjamin  and
      Artetxe, Mikel  and
      Shukla, Satya Narayan  and
      Husa, Donald  and
      Goyal, Naman  and
      Krishnan, Abhinandan  and
      Zettlemoyer, Luke  and
      Khabsa, Madian",
    booktitle = "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand and virtual meeting",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.acl-long.44",
    pages = "749--775",
}
```
