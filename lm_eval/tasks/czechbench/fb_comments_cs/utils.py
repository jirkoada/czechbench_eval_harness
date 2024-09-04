from sklearn.metrics import f1_score
import numpy as np
import string
import re

labels = {"-1": 0, "0": 1, "1": 2}
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


def doc_to_text(doc) -> str:
    return f"""Urči sentiment zadaného textu. Odpověz číslem 1 pro pozitivní sentiment, 0 pro neutrální sentiment, nebo -1 pro negativní sentiment.
Vždy odpovídej pouze tímto jedním číslem bez dalšího komentáře.

Zde je 5 ukázkových příkladů:

Text:
Rek bych ze mekac trosku nezachapal tvoji otazku :D
Odpověď:
0

Text:
Moc krásná fotečka :-)
Odpověď:
1

Text:
Já mám iPhone a nejde to!
Odpověď:
-1

Text:
parada, konecne si je zase jeden z velkych hracu vedom nastupujici budoucnosti. Diky
Odpověď:
1

Text:
jasně, že Vyskoká u Miskovic Kutná Hora :) hned kousíček je zřícenina Kláštera Belveder :)
Odpověď:
0

Vygeneruj klasifikaci pro následující příklad:
Text:
{doc['comment']}
Odpověď:
"""


def doc_to_target(doc) -> int:
    # because categories are indexed from 1
    return int(doc['sentiment_int']) + 1
