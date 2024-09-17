from sklearn.metrics import f1_score
import numpy as np
import string
import re

labels = {"no": 0, "unknown": 1, "yes": 2}
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
    return f"""For the given premise and hypothesis, decide whether the premise supports, refutes, or does not provide enough information for the hypothesis.
If the premise supports the hypothesis, return the word Yes. If it refutes it, return the word No. If it neither supports nor refutes it, return the word Unclear. Always respond with a single word without any further commentary.

Here are 5 examples:

Premise:
Prague 14. July (CTK) - She was a member of the National Theatre in Prague for seventeen years and her acting has also been used extensively in film. Regina Rázlová mostly played self-confident and exclusive women, often with a strong sense of entitlement. She was also on the opposite side of the law, and her captivating voice sounded even in radio and dubbing. After 1989, she stopped doing well, went into business and even spent several months in custody over the Skloexport tunneling case. Added to this were health problems. But in the spirit of the heroines she portrayed on stage, even in the movie, she was able to overcome everything bad. Today Rázlová, who will celebrate her 70th birthday o 16. July, is once again a sought-after actress and celebrity.
Hypothesis:
Regina Rázlová is a singer.
Label:
No

Premise:
Washington, Aug. 20. (ČTK) - Leading Democratic Congressman Barney Frank unexpectedly spoke out this week in favour of abolishing the nationalised mortgage agencies Fannie Mae and Freddie Mac, which significantly contributed to the emergence and deepening of the severe financial crisis in the USA from 2008-09. From the influential co-author of a sweeping financial regulatory reform law, it's a U-turn because Frank had previously held sway over both agencies, according to observers. 
Hypothesis:
Congressman Frank wants to abolish two agencies.
Label:
Yes

Premise:
The sale of live dolphins is governed by the Agreement on International Trade in Endangered Species, which prohibits similar transactions if they could harm the animals. The Solomon Islands, about 1,800 kilometers northeast of Australia, did not sign the agreement. The territory is currently in the throes of a political crisis and ethnic violence, which prompted Australian troops to be sent there this week. Environmentalists accuse Mexican businessmen of exploiting the crisis in the Solomon Islands.
Hypothesis:
Australia has rejected an agreement on international trade in endangered species relating to, for example, the sale of live dolphins.
Label:
Unknown

Premise:
BRNO/BUČOVICE (Vyškovsko) 1. June (CTK) - Fifty years of restoring tapestries at the Moravian Tapestry Manufactory in Valašské Meziříčí na Vsetínsku will be illustrated from today by an exhibition at Bučovice Castle in Vyškovsko. It will last until the end of August, Bučovice castellan Pavel Ecler told ČTK today. Among other things, the manufactory brought six historical tapestries from the depositories of the state chateau Náměšť nad Oslavou and the Silesian Museum in Opava to the Bučovice castle.
Hypothesis:
There is no exhibition on the restoration of tapestries at Bučovice Castle.
Label:
No

Premise:
Last year, 1.1 million illegal immigrants from Mexico were apprehended on the 3200-kilometre US southern border, more than half of them along 600 kilometres in Arizona's border desert. The Department of Homeland Security is preparing to increase the number of border patrol agents by another 500 people in the spring, when the immigration wave reaches its peak, and will temporarily transfer 27 aircraft there.
Hypothesis:
The migration wave from Mexico to the US peaks in April.
Label:
Unknown

Generate the label for the following example:
Premise:
{doc['evidence']}
Hypothesis:
{doc['claim']}
Label:
"""


def doc_to_target(doc) -> int:
    return doc['label']

