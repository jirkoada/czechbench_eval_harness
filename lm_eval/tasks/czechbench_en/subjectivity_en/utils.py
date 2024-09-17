from sklearn.metrics import f1_score
import numpy as np
import string
import re

labels = {"0": 0, "1": 1}
re_ignore = [" ", "\n", "Answer", ",", ";", "\.", "!", "\?", ":", "'", '"', "_", "-"]

def macro_f1_score(items):
    unzipped_list = list(zip(*items))
    references = unzipped_list[0]
    predictions = unzipped_list[1]

    for s in re_ignore:
        predictions = np.array([re.sub(s, "", x) for x in predictions])
        references = np.array([re.sub(s, "", x) for x in references])

    predictions = np.char.lower(predictions)
    references = np.char.lower(references)

    repl_table = string.punctuation.maketrans("", "", string.punctuation)
    predictions = np.char.translate(predictions, table=repl_table)
    references = np.char.translate(references, table=repl_table)

    golds = [labels[g] for g in references]
    preds = [labels[p] if p in labels.keys() else -1 for p in predictions]
    fscore = f1_score(golds, preds, average="macro")
    return fscore


def doc_to_text(doc) -> str:
    return f"""For the given statement, determine whether the statement conveys a subjective opinion or objective facts. Respond with the number 0 for subjective opinion, or 1 for objective facts.
Always respond only with this single digit without any further commentary.

Here are 5 examples:

Text:
As excellent as the first, with an even more intricate plot and a perfect vision of the future.
Answer:
0

Text:
And so unfolds the story of four beautiful young women who seemingly have everything, including secrets that should not be discovered.
Answer:
1

Text:
Too much talk and too little action to my taste.	
Answer:
0

Text:
It documents the stories of four people from Novelda who are fighting to make their dreams come true, despite facing many obstacles.	
Answer:
1

Text:
And I have to admit that I did not fall asleep even once, although it is almost a two-hour borefest.	
Answer:
0
Classify the following example:
Text:
{doc['text']}
Answer:
"""


def doc_to_target(doc) -> int:
    return int(doc['label'])
