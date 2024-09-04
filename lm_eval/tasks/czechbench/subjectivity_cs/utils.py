from sklearn.metrics import f1_score
import numpy as np
import string
import re

labels = {"0": 0, "1": 1}
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
    return f"""Urči zda zadaný výrok vyjadřuje subjektivní názor, nebo objektivní skutečnost. Odpověz číslem 0 pro subjektivní názor, nebo 1 pro objektivní skutečnost.
Vždy odpovídej pouze tímto jedním číslem bez dalšího komentáře.

Zde je 5 ukázkových příkladů:

Text:
Stejně vynikající jako jednička s ještě spletitějším dějem a s dokonalou vizí budoucnosti.	
Odpověď:
0

Text:
A tak se odvíjí příběhy 4 krásných slečen, které mají zdánlivě vše i svá tajemství, jenž by neměla být objevena.	
Odpověď:
1

Text:
Na muj vkus az moc "kecaci" a malo akce.	
Odpověď:
0

Text:
Dokument zachycuje příběhy čtyř lidí z Noveldy, kteří bojují za splnění svých snů přesto, že se setkávají se spoustou obtíží.	
Odpověď:
1

Text:
A musím se přiznat, že sem ani jednou neusnul, ačkoli je to bezmála dvouhodinová nuda jako prase.	
Odpověď:
0
Vygeneruj klasifikaci pro následující příklad:
Text:
{doc['text']}
Odpověď:
"""


def doc_to_target(doc) -> int:
    return int(doc['label'])
