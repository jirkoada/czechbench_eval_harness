from sklearn.metrics import f1_score
import numpy as np
import string
import re

labels = {"ne": 0, "nevím": 1, "ano": 2}
re_ignore = [" ", "\n", "Odpověď", ",", ";", "\.", "!", "\?", ":", "'", '"', "_", "-"]

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
    return f"""Pro zadaný kontext a testované tvrzení rozhodni, zda kontext potvrzuje obsah tvrzení, popírá ho, nebo neobsahuje dostatečné informace. 
Pokud tvrzení potvrzuje, vrať slovo Ano. Pokud jej vyvrací, vrať slovo Ne. Pokud nelze rozhodnout, vrať slovo Nevím. Vždy odpovídej pouze tímto jedním slovem bez dalšího komentáře.

Zde je 5 ukázkových příkladů:

Kontext:
Lidé na kolech čekají na křižovatce.
Tvrzení:
Právě teď se konají cyklistické závody.
Klasifikace:
Nevím

Kontext:
Děti jdou domů ze školy.
Tvrzení:
Děti jsou v knihovně.
Klasifikace:
Ne

Kontext:
Děti se usmívají a mávají na kameru.
Tvrzení:
Jsou tam děti.
Klasifikace:
Ano

Kontext:
Starší muž pije pomerančový džus v restauraci.
Tvrzení:
Muž pije džus.
Klasifikace:
Ano

Kontext:
Bílý kůň táhne vozík, zatímco muž stojí a sleduje.
Tvrzení:
Kůň tahá zboží.
Klasifikace:
Nevím

Vygeneruj klasifikaci pro následující příklad:
Kontext:
{doc['evidence']}
Tvrzení:
{doc['claim']}
Klasifikace:
"""

def doc_to_target(doc):
    return doc['label']
