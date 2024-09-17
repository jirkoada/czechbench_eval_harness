# MMLU dataset

The professional_law and us_foreign_policy subtasks are excluded from the evaluation to match the czech version of this benchmark.

### Dataset details

- Language: EN (Original)
- Task: Knowledge-Based Question Answering
- Samples: 12508 (Test set)
- Few-shot examples: 5 (From the development set for each topic)
- [Hugging Face link](https://huggingface.co/datasets/cais/mmlu)

### Task description

MMLU consists of 57 separate subtasks, 55 of which are used here. Each subtask's examples are formatted as single-choice questions with 4 available answers. The model is asked to return a number from 1 to 4, corresponding to the chosen answer.

Accuracies for all 55 subtasks are reported, as well as an average accuracy over all test samples.

## Citation

```bibtex
    @article{hendryckstest2021,
      title={Measuring Massive Multitask Language Understanding},
      author={Dan Hendrycks and Collin Burns and Steven Basart and Andy Zou and Mantas Mazeika and Dawn Song and Jacob Steinhardt},
      journal={Proceedings of the International Conference on Learning Representations (ICLR)},
      year={2021}
    }

    @article{hendrycks2021ethics,
      title={Aligning AI With Shared Human Values},
      author={Dan Hendrycks and Collin Burns and Steven Basart and Andrew Critch and Jerry Li and Dawn Song and Jacob Steinhardt},
      journal={Proceedings of the International Conference on Learning Representations (ICLR)},
      year={2021}
    }
```
