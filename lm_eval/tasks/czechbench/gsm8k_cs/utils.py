def get_prompt(doc):

    task = """Vyřeš zadanou matematickou úlohu. Popiš svůj postup a následně uveď výsledek jako jedno číslo následující za výrazem '####'."""

    few_shot = """Zde je 5 ukázkových zodpovězených příkladů:
Úloha:
Weng vydělává 12 dolarů na hodinu za hlídání dětí. Včera dělala 50 minut chůvu. Kolik vydělala?
Odpověď:
Weng vydělává 12/60 = 0,2 dolaru za minutu. Pracovala 50 minut a vydělala 0,2 x 50 = 10 dolarů. #### 10

Úloha:
Betty šetří peníze na novou peněženku, která stojí 100 dolarů. Betty má jen polovinu peněz, které potřebuje. Její rodiče se rozhodli dát jí na tento účel 15 dolarů a její prarodiče dvakrát tolik než její rodiče. Kolik peněz ještě Betty potře
buje, aby si mohla koupit peněženku?
Odpověď:
Na začátku má Betty jen 100/2 = 50 dolarů. Prarodiče Betty jí dali 15 * 2 = 30 dolarů. To znamená, že Betty potřebuje 100 - 50 - 30 - 15 = 5 dolarů navíc. #### 5

Úloha:
Hlubinné monstrum se vynoří z vody jednou za sto let, aby hodovalo na lodi a ukojilo svůj hlad. Za více než tři sta let pohltila 847 lidí. Lodě byly v průběhu času stavěny větší, takže každá nová loď má dvakrát více lidí než poslední loď. Ko
lik lidí bylo na lodi, kterou monstrum snědlo v prvních sto letech?
Odpověď:
Nechť S je počet lidí na lodi prvních sto let. Druhá stoletá loď jich měla dvakrát tolik než ta první, čili 2S lidí. Třetí stoletá loď jich měla dvakrát tolik než druhá, takže 2 * 2S = 4S lidí. Všechny lodě měly S + 2S + 4S = 7S = 847 lidí.
Takže loď, kterou monstrum snědlo v prvních sto letech měla S = 847 / 7 = 121 lidí. #### 121

Úloha:
James píše dvakrát týdně třístránkový dopis dvěma různým přátelům. Kolik stránek napíše za rok?
Odpověď:
Každému příteli napíše 3 * 2 = 6 stránek týdně. Takže každý týden napíše 6 * 2 = 12 stran. To znamená, že za rok napíše 12 * 52 = 624 stran #### 624

Úloha:
James vytváří mediální impérium. Vytvoří film za 2000 dolarů. Výroba každého DVD stála 6 dolarů. Prodává ho za 2,5 násobek. Prodává 500 filmů denně, pět dní v týdnu. Kolik vydělá za 20 týdnů?
Odpověď:
Prodal každé DVD za 6*2,5=15 dolarů, takže vydělal 15-6=9 dolarů. Takže každý den vydělá 9*500=4500 dolarů. Takže vydělá 4500*5=$22,500 týdně. Vydělá 22,500*20=$450,000 celkem. Potom po odečtení nákladů na vytvoření filmu má zisk 450,000-200
0=$448,000 #### 448000
"""

    request = f"""Vyřeš následující úlohu:
Úloha:
{doc["question"]}
Odpověď:
"""

    return task + few_shot + request
