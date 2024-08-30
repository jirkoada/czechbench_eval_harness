# AGREE dataset

The dataset was obtained from its official [site](https://nlp.fi.muni.cz/~xbaisa/agree/).

The data were transformed to accommodate a missing word selection task. 
Sentences containing more than one marked verb were discarded. 
In the remaining sentences, the marked verb was completely replaced with the "____" token. 
All five possible verb variants formed the list of available choices. The index of the correct choice was stored as the label.

Preblamatic examples were identified by gradually selecting examples wrongly answered by Claude 3 Haiku, Claude 3 Sonet and GPT-4 Turbo. These 115 examples were then manually checked and 46 of them were identified as ambiguous and removed from the dataset. This led to a final number of 627 evaluation samples.

### Dataset details

- Language: CS (Original)
- Task: Language proficiency: subject-verb agreement
- Samples: 627 (Test set)
- Few-shot examples: 5 (From validation set)

### Task description

The model is asked to select one of five possible forms of a verb that has been masked out in the reference sentence. All the proposed verb forms are in past tense and differ only in their ending (-la, -lo, -li, -ly, -l), which needs to correctly match the sentence subject.

The reported accuracy metric represents the percentage of correctly completed sentences.

## License

The dataset is licensed under [Creative Commons BY-NC 2.0](https://creativecommons.org/licenses/by-nc/2.0/).

## References

[1] Baisa, [Byte Level Language Models](https://is.muni.cz/th/139654/fi_d/), 2016
