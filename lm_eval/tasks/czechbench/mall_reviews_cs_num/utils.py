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
Miska neuvěřitelně páchne plastem, nepomohlo ani umytí v myčce.
Odpověď:
-1

Text:
Vyborna pochoutka pro psy!
Odpověď:
1

Text:
Mohu jen doporučit. Pokud netrváte na zvýšené odolnosti (prach, voda), tak je svým poměrem cena/kapacita/kompaktnost výborný! Také rychlost čtení/zápis není špatná. Samozřejmě např. flashdisky od výborné značky OCZ rychlostí příp. odolností nedoženou, ale ... záleží na prioritách.
Odpověď:
0

Text:
Jsem spokojena, přes kabel krásný obraz i zvuk , doporučuji :-)
Odpověď:
1

Text:
Trošku se mi nezdá přidělání gumičkami, nevím, jak bude trvanlivé, ale to se po ani ne měsíci nedá hodnotit. Škoda, že se nedají "vyhodit" z menu funkce dostupné po dokoupení (frekvence šlapání, druhé kolo). Jinak spokojenost, jen si musí člověk zvyknout, že to trvá tak 2-5 vteřin, než tachometr zareaguje na pohyb.
Odpověď:
0

Vygeneruj klasifikaci pro následující příklad:
Text:
{doc['comment']}
Odpověď:
"""


def doc_to_target(doc) -> int:
    # because categories are indexed from 1
    return int(doc['rating_int']) + 1
