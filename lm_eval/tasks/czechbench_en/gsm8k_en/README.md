# GSM8K dataset

### Dataset details

- Language: EN (Original)
- Task: Mathematical inference
- Samples: 1319 (Test set)
- Few-shot examples: 5 (From training set)
- [Hugging Face link](https://huggingface.co/datasets/openai/gsm8k)

### Task description

The model is presented with a math word problem. It is asked to describe its solution step by step, and then mark the final numerical answer with a preceding '####' token.

The main evaluation accuracy metric (exact_match) represents the percentage of final numerical answers exactly matching the references.

## Citation

```bibtex
@article{cobbe2021gsm8k,
  title={Training Verifiers to Solve Math Word Problems},
  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
  journal={arXiv preprint arXiv:2110.14168},
  year={2021}
}
```
