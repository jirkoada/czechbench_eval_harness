# CTKFacts Dataset

This dataset was obtained from [Hugging Face](https://huggingface.co/datasets/ctu-aic/ctkfacts_nli).

### Dataset details

- Language: CS (Original)
- Task: Natural Language Inference
- Samples: 558 (Test set)
- Few-shot examples: 5 (From training set)
- [Hugging Face link](https://huggingface.co/datasets/ctu-aic/ctkfacts_nli)

### Task description

The model is asked to determine the correct relation between a premise and a hypothesis. The premise can confirm the hypothesis, refute it, or there can be no clear relation.
This leads to a three-class classification problem.

The reported metrics are classification accuracy (exact_match) and macro-averaged F1 score.

## Citation

```bibtex
@article{Ullrich_2023,
   title={CsFEVER and CTKFacts: acquiring Czech data for fact verification},
   volume={57},
   ISSN={1574-0218},
   url={http://dx.doi.org/10.1007/s10579-023-09654-3},
   DOI={10.1007/s10579-023-09654-3},
   number={4},
   journal={Language Resources and Evaluation},
   publisher={Springer Science and Business Media LLC},
   author={Ullrich, Herbert and Drchal, Jan and Rýpar, Martin and Vincourová, Hana and Moravec, Václav},
   year={2023},
   month=may, pages={1571–1605} 
}
```

