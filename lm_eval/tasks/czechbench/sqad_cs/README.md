# SQAD Dataset

This dataset was obtained from [Hugging Face](https://huggingface.co/datasets/fewshot-goes-multilingual/cs_squad-3.0). It is a filtered version of the original dataset, released on [LINDAT](https://lindat.cz/repository/xmlui/handle/11234/1-3069).

### Dataset details

- Language: CS (Original)
- Task: Question Answering / Reading Comprehension
- Samples: 843 (Test set)
- Few-shot examples: 5 (From training set)

### Task description

The model is presented with a text passage and a related question. It is expected to produce a short answer in natural language, that is either a direct excerpt from the passage or a simple "yes" or "no" ("ano" or "ne") answer.

The [SQuAD metric](https://huggingface.co/spaces/evaluate-metric/squad) from Hugging Face was used for evaluation. The obtained exact match accuracy and ROUGE-1-like F1 score metrics are reported. To normalize the compared texts, the [Morphodita](https://ufal.mff.cuni.cz/morphodita) and [Derinet](https://ufal.mff.cuni.cz/derinet) morphological analysis tools are employed. There are three pairs of metrics reported in total, one for unchanged texts, one for lemmatized texts, and one for lemmas replaced with the roots of their word-formation relation trees.

## License

The dataset is licensed under [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).

## References

[1] Sabol et al., [Czech Question Answering with Extended SQAD v3.0 Benchmark Dataset](https://nlp.fi.muni.cz/raslan/2019/paper14-medved.pdf), 2019

[2] Straková et al., [Open-Source Tools for Morphology, Lemmatization, POS Tagging and Named Entity Recognition](https://aclanthology.org/P14-5003), ACL 2014

[3] Vidra et al., [DeriNet 2.0: Towards an All-in-One Word-Formation Resource](https://aclanthology.org/W19-8510), 2019
