# ARC dataset

### Dataset details

- Language: EN (Original)
- Task: Knowledge-Based Question Answering
- Subsets:
    - Challenge: 1172 test samles
    - Easy: 2376 test samles
- Few-shot examples: 5 (From ARC Challenge validation set)
- [Hugging Face link](https://huggingface.co/datasets/allenai/ai2_arc)

### Task description

The model is presented with a question and a selection of (typically 4) possible answers. It needs to return a letter (A, B, C, ...) corresponding to the correct answer.

The reported accuracy metric (exact_match) represents the percentage of correctly selected answers.

## Citation

```bibtex
@article{allenai:arc,
      author    = {Peter Clark  and Isaac Cowhey and Oren Etzioni and Tushar Khot and
                    Ashish Sabharwal and Carissa Schoenick and Oyvind Tafjord},
      title     = {Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge},
      journal   = {arXiv:1803.05457v1},
      year      = {2018},
}
```
