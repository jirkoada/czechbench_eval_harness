# Czech News Dataset

This dataset was obtained from [Hugging Face](https://huggingface.co/datasets/hynky/czech_news_dataset_v2).

Only 200 samples from each of the 5 selected categories (Zahraniční, Domácí, Sport, Kultura, Ekonomika) are used for evaluation.

### Dataset details

- Language: CS (Original)
- Task: News topic classification
- Samples: 1000 (Filtered test set)
- Few-shot examples: 5 (From training set)
- [Hugging Face link](https://huggingface.co/datasets/CIIRC-NLP/czech_news_simple-cs)

### Task description

The model is given the first paragraph of a news article and is asked to correctly determine its category. The choices available are:  
$~~~~$ 1\) Zahraniční  
$~~~~$ 2\) Domácí  
$~~~~$ 3\) Sport  
$~~~~$ 4\) Kultura  
$~~~~$ 5\) Ekonomika  

The reported metrics are classification accuracy (exact_match) and macro-averaged F1 score.

## Citation

```bibtex
@misc{kydlíček2023datasetstrongbaselinesclassification,
      title={A Dataset and Strong Baselines for Classification of Czech News Texts}, 
      author={Hynek Kydlíček and Jindřich Libovický},
      year={2023},
      eprint={2307.10666},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2307.10666}, 
}
```