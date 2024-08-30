import datasets

def get_prompt(doc):
    task = """Vyřeš zadanou úlohu výběrem jedné z 5 nabídnutých možností.
Zvolenou odpověď neopakuj. Odpovídej vždy pouze písmenem odpovídajícím zvolené odpovědi bez dalšího komentáře.
"""

    few_shot = """Zde je 5 ukázkových příkladů:
Úloha:
Bedřich je o 1 rok a 1 den starší než Anežka. Narodil se 1. ledna 2002. Kdy se narodila Anežka?	
Možnosti:
A) 2. ledna 2003
B) 2. ledna 2001
C) 31. prosince 2000
D) 31. prosince 2002
E) 31. prosince 2003
Odpověď:
A

Úloha:
Anička a Bětka mají dohromady 10 bonbonů. Bětka jich má o 2 více než Anička. Kolik bonbonů má Bětka?
Možnosti:
A) 8
B) 6
C) 4
D) 2
E) 1
Odpověď:
B

Úloha:
V rovnici KAN - GAR = OO představují různá písmena různé číslice, stejná písmena stejné číslice. Najdětě největší možnou hodnotu čísla KAN.
Možnosti:
A) 987
B) 876
C) 865
D) 864
E) 785
Odpověď:
D

Úloha:
Kája, Eliška a Lucka slaví narozeniny ve stejný den. Jako každý rok dostaly společný dort, na kterém je napsán součet jejich věků. Letos je to 44. Které číslo tam bude napsáno příště, až to bude opět dvojmístné číslo zapsané týmiž číslicemi?
Možnosti:
A) 55
B) 66
C) 77
D) 88
E) 99
Odpověď:
C

Úloha:
Eva, Lucie a Magda spolu hrály turnaj v piškvorkách. Každé partie se účastnily právě dvě z těchto dívek, žádná neskončila remízou. Po každé partii nastoupila vítězka předchozí partie a dívka, která ji nehrála. Eva hrála celkem 10krát, Lucka 15krát a Magda 17krát. Kdo všechno mohl vyhrát druhou partii?
Možnosti:
A) Eva
B) Lucie
C) Magda
D) Eva nebo Magda
E) Lucie nebo Magda
Odpověď:
E
"""

    request = f"""Vyřeš následující úlohu:
Úloha:
{doc["question"]}
Možnosti:
A) {doc["A"]}
B) {doc["B"]}
C) {doc["C"]}
D) {doc["D"]}
E) {doc["E"]}
Odpověď:
"""

    return task + few_shot + request

def doc_to_target(doc):
    answer_letter = doc["correct_answer"]

    return answer_letter

def process_docs(dataset: datasets.Dataset):
    example_idcs = [1, 6, 4, 16, 20]
    dataset = dataset.select(
        (
            i for i in range(len(dataset))
            if i not in set(example_idcs)
        )
    )
    return dataset