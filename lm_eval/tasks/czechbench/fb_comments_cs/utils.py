from sklearn.metrics import f1_score
import numpy as np
import string
import re

labels = {"pozitivní": 0, "neutrální": 1, "negativní": 2}
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
    return f"""Urči sentiment zadaného textu výběrem jedné z těchto možností: 
1) pozitivní
2) negativní
3) neutrální
Vždy odpovídej pouze jedním slovem bez dalšího komentáře.

Zde je 5 ukázkových příkladů:

Text:
Rek bych ze mekac trosku nezachapal tvoji otazku :D
Odpověď:
neutrální

Text:
Moc krásná fotečka :-)
Odpověď:
pozitivní

Text:
Já mám iPhone a nejde to!
Odpověď:
negativní

Text:
parada, konecne si je zase jeden z velkych hracu vedom nastupujici budoucnosti. Diky
Odpověď:
pozitivní

Text:
jasně, že Vyskoká u Miskovic Kutná Hora :) hned kousíček je zřícenina Kláštera Belveder :)
Odpověď:
neutrální

Vygeneruj klasifikaci pro následující příklad:
Text:
{doc['comment']}
Odpověď:
"""
