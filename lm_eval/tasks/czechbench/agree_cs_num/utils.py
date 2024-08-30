# flake8: noqa

def get_prompt(doc):
    task = """V zadané větě je jedno slovo nahrazeno výrazem '____'. Z nabídnutých možností vyber slovo, po jehož doplnění bude zadaná věta gramaticky správná.
Zvolenou odpověď neopakuj. Odpovídej vždy pouze číslicí odpovídající zvolené odpovědi bez dašího komentáře.
"""

    few_shot = """Zde je 5 ukázkových příkladů:
Věta:
Moje zamyšlení, jak jste si ____, je hlavně o mrhání.
Možnosti:
1) všimla
2) všimlo
3) všimli
4) všimly
5) všiml
Odpověď:
3

Věta:
Jeho kapacita ____ až 36 tisíc diváků.
Možnosti:
1) byla
2) bylo
3) byli
4) byly
5) byl
Odpověď:
1

Věta:
V sobotu ____ 36. ročník Karlovarského filmového festivalu.
Možnosti:
1) skončila
2) skončilo
3) skončili
4) skončily
5) skončil
Odpověď:
5

Věta:
Hodně zvláštní ____ i japonské sladkosti podávané na závěr.
Možnosti:
1) byla
2) bylo
3) byli
4) byly
5) byl
Odpověď:
4

Věta:
Pro vozy se ____ několik typů karosérií lišících se uspořádáním interiéru a vybavením.
Možnosti:
1) vyráběla
2) vyrábělo
3) vyráběli
4) vyráběly
5) vyráběl
Odpověď:
2
"""

    request = f"""Doplň správně chybějící slovo do této věty:
Věta:
{doc["sentence"]}
Možnosti:
1) {doc["choices"][0]}
2) {doc["choices"][1]}
3) {doc["choices"][2]}
4) {doc["choices"][3]}
5) {doc["choices"][4]}
Odpověď:
"""

    return task + few_shot + request


def doc_to_target(doc):
    return str(doc["answer_idx"] + 1)
