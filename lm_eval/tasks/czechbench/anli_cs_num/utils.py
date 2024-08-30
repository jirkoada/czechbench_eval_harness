# flake8: noqa
from sklearn.metrics import f1_score
import numpy as np
import string
import re

labels = {"0": 0, "1": 1, "2": 2}
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
    task = """Pro zadaný kontext a testované tvrzení rozhodni, zda kontext potvrzuje obsah tvrzení, popírá ho, nebo neobsahuje dostatečné informace. 
Pokud tvrzení potvrzuje, vrať číslo 2. Pokud jej vyvrací, vrať číslo 0. Pokud nelze rozhodnout, vrať číslo 1. Vždy odpovídej pouze touto jednou číslicí bez dalšího komentáře.
"""
    few_shot = """Zde je 5 ukázkových příkladů:
Kontext:
Zisk před úroky a zdaněním vyskočil na 4,55 miliardy eur (5,34 miliardy dolarů) z 1,90 miliardy o rok dříve, uvedl VW ve čtvrtečním prohlášení. „Jsem pevně přesvědčen, že naše finanční základna je dostatečná k tomu, abychom zvládli transformaci v automobilovém průmyslu a témata budoucnosti,“ uvedl ve svém prohlášení šéf financí Frank Witter. 
Tvrzení:
VW chce být součástí transformace v automobilovém průmyslu.
Klasifikace:
2

Kontext:
Nedávná studie nenalezla žádné důkazy sezónní afektivní poruchy na Islandu, kde se slunce v zimě dlouho neobjevuje.
Tvrzení:
Slunce se na Islandu v zimě dlouho objevuje.
Klasifikace:
0

Kontext:
Craig Conway, který byl propuštěn z funkce generálního ředitele společnosti PeopleSoft předtím, než společnost koupila společnost Oracle, byl minulý týden v Anglii.
Tvrzení:
Craig Conway byl propuštěn, protože chtěl minulý týden jet do Anglie
Klasifikace:
1

Kontext:
Ordonez Reyes obvinil Joseho Jesusa Penu, údajného šéfa bezpečnosti nikaragujského velvyslanectví v Tegucigalpě, ze zorganizování atentátu na velitele Manuela Antonia Rugamu 7. ledna.	
Tvrzení:
Jose zabil Ordoneze a Manuela
Klasifikace:
0

Kontext:
Více než 150 delfínů, mořských želv a zobáků velryb bylo vyplaveno na mrtvé pláže v Africe.	
Tvrzení:
Vláda varuje lidi, aby se drželi dál od mrtvých těl
Klasifikace:
1
"""

    request = f"""Vygeneruj klasifikaci pro následující příklad:
Kontext:
{doc["evidence"]}
Tvrzení:
{doc["claim"]}
Klasifikace:
"""

    return task + few_shot + request
