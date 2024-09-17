# flake8: noqa
from sklearn.metrics import f1_score
import numpy as np
import string
import re

labels = {"no": 0, "unclear": 1, "yes": 2}
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


def get_prompt(doc):
    task = """For the given premise and hypothesis, decide whether the premise supports, refutes, or does not provide enough information for the hypothesis.
If the premise supports the hypothesis, return the word Yes. If it refutes it, return the word No. If it neither supports nor refutes it, return the word Unclear. Always respond with a single word without any further commentary.
"""
    few_shot = """Here are 5 examples:
Premise:
Earnings before interest and tax jumped to 4.55 billion euros ($5.34 billion) from 1.90 billion a year earlier, VW said in a statement on Thursday. "I am firmly convinced that our financial footing is adequate to cope with the transformation in the automotive industry and topics of the future," finance chief Frank Witter said in the statement.
Hypothesis:
VW wants to be part of the transformation in the automotive industry.
Label:
Yes

Premise:
A recent study found no evidence of seasonal affective disorder in Iceland where the sun does not appear for a long time in the winter.
Hypothesis:
The sun appears often in iceland during the winter
Label:
No

Premise:
Craig Conway, who was fired as CEO of PeopleSoft before the company was acquired by Oracle, was in England last week.
Hypothesis:
Craig Conway was fired because he wanted to go to England last week
Label:
Unclear

Premise:
Ordonez Reyes accused Jose Jesus Pena, alleged chief of security for the Nicaraguan embassy in Tegucigalpa, of masterminding the January 7th assassination of contra-commander Manuel Antonio Rugama.
Hypothesis:
Jose killed Ordonez and Manuel
Label:
No

Premise:
More than 150 dolphins, marine turtles and beaked whales have been washed up dead on beaches in Africa.
Hypothesis:
The government is warning people to stay away from the dead bodies
Label:
Unclear
"""

    request = f"""Generate the label for the following example:
Premise:
{doc["premise"]}
Hypothesis:
{doc["hypothesis"]}
Label:
"""

    return task + few_shot + request
