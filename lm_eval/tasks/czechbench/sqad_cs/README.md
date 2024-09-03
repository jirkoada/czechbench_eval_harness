# SQAD Dataset

This dataset was obtained from [Hugging Face](https://huggingface.co/datasets/Pehy/cs_sqad-3.0). It is a filtered version of the original dataset, released on [LINDAT](https://lindat.cz/repository/xmlui/handle/11234/1-3069).

### Dataset details

- Language: CS (Original)
- Task: Question Answering / Reading Comprehension
- Samples: 843 (Test set)
- Few-shot examples: 5 (From training set)
- [Hugging Face link](https://huggingface.co/datasets/Pehy/cs_sqad-3.0)

### Task description

The model is presented with a text passage and a related question. It is expected to produce a short answer in natural language, that is either a direct excerpt from the passage or a simple "yes" or "no" ("ano" or "ne") answer.

The [SQuAD metric](https://huggingface.co/spaces/evaluate-metric/squad) from Hugging Face is used for evaluation. The obtained exact match accuracy and ROUGE-1-like F1 score metrics are reported. 

## Citation

```bibtex
@misc{11234/1-3069,
    title = {sqad 3.0},
    author = {Medve{\v d}, Marek and Hor{\'a}k, Ale{\v s}},
    url = {http://hdl.handle.net/11234/1-3069},
    note = {{LINDAT}/{CLARIAH}-{CZ} digital library at the Institute of Formal and Applied Linguistics ({{\'U}FAL}), Faculty of Mathematics and Physics, Charles University},
    copyright = {{GNU} Library or "Lesser" General Public License 3.0 ({LGPL}-3.0)},
    year = {2019}
}
```
