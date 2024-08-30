from sklearn.metrics import f1_score
import numpy as np
import string
import re

labels = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4}
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
    return f"""Pro zadaný text pocházející ze zpravodajského článku urči jeho kategorii z následujícího výběru:
1) Zahraniční
2) Domácí
3) Sport
4) Kultura
5) Ekonomika
Vždy vracej pouze číslo kategorie bez dalšího komentáře.

Zde je 5 ukázkových příkladů:

Text:
Ohňostroji, veselicemi a s jásotem přivítal svět příchod roku 2000. Jako poslední obyvatelé Země sledovali západ Slunce v roce 1999 obyvatelé tichomořského zámořského území USA, Americké Samoy. Slunce se naposledy v roce 1999 schovalo za duhovým horizontem v pátek 06:57 večer místního času (tj. v sobotu v 07:57 SEČ). Petardy a bengálské ohně usmrtily v Evropě šest lidí a desítky dalších zranily. Oslavy i přesto nepotvrdily chmurné představy policistů, kteří čekali daleko větší potíže a byli ve zvýšené pohotovosti ve všech evropských metropolích
Klasifikace:
1

Text:
V nesmírně vyrovnané tabulce fotbalové ligy má pátá Ostrava náskok jen sedmi bodů před posledním Žižkovem. Většinu týmů za Ostravou čeká tuhý boj o záchranu, a tak už se na něj připravují	
Klasifikace:
3

Text:
Strana, která by vznikla ze studentské výzvy "Děkujeme, odejděte!", by nyní mohla vyhrát případné parlamentní volby. Na její kandidaturu by přitom nejvíce doplatily Unie svobody a ODS. Účast nové strany by navíc zvýšila předpokládanou volební účast o šest procent na 85,7 procenta občanů. Vyplývá to z exkluzivního prosincového šetření agentury Sofres-Factum pro ČTK. "Studentskou" stranu by těsně před Vánocemi volilo 24,7 procenta občanů. Na druhém místě by skončila ODS, které by dalo hlas 14,4 procenta dotázaných
Klasifikace:
2

Text:
Tržby maloobchodních organizací vzrostly za celý loňský rok o 2,1 procenta, v samotném prosinci to bylo dokonce o 6,4 procenta. Letošní výhledy jsou podle ekonomů mírně horší, tržby maloobchodu nají podle jejich odhadů vzrůst přibližně o procento. Vliv bude mít nižší růst reálných mezd, které loni dosáhly vysokých 6 procent, na tržbách se podepíše se i vyšší nezaměstnanost	
Klasifikace:
5

Text:
Třináctého ledna odstartuje v pražské Městské knihovně další, již šestá část unikátní filmové přehlídky Projekt 100. Společná akce Asociací českých a slovenských filmových klubů a Městských divadel v Uherském Hradišti se zrodila před čtyřmi lety při příležitosti stého výročí vzniku kinematografie, nyní se s šestou desítkou filmů dostává již do své druhé poloviny
Klasifikace:
4

Vygeneruj klasifikaci pro následující příklad:
Text:
{doc['brief']}
Klasifikace:
"""


def doc_to_target(doc) -> int:
    # because categories are indexed from 1
    return int(doc['category']) - 1
