# Czech News Dataset

This dataset was obtained from [Hugging Face](https://huggingface.co/datasets/hynky/czech_news_dataset_v2).

Only 200 samples from each of the 5 selected categories (Zahraniční, Domácí, Sport, Kultura, Ekonomika) are used for evaluation.

### Dataset details

- Language: CS (Original)
- Task: News topic classification
- Samples: 1000 (Filtered test set)
- Few-shot examples: 5 (From training set)

### Task description

The model is given the first paragraph of a news article and is asked to correctly determine its category. The choices available are:  
$~~~~$ 1\) Zahraniční  
$~~~~$ 2\) Domácí  
$~~~~$ 3\) Sport  
$~~~~$ 4\) Kultura  
$~~~~$ 5\) Ekonomika  
The model is expected to return the number corresponding to the chosen category.

The reported accuracy metric represents the percentage of correctly selected answers.

## License

The dataset is licensed under [Creative Commons Zero 1.0](https://creativecommons.org/publicdomain/zero/1.0/).

## References

[1] Kydlíček et al., [A Dataset and Strong Baselines for Classification of Czech News Texts](https://arxiv.org/abs/2307.10666), 2023
