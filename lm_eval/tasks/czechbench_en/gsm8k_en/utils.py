import re

def get_prompt(doc):

    task = """Solve the given mathematical problem. Explain your thought process and then state the final answer as a single number following the '####' expression."""

    few_shot = """Here are 5 example problems with answers:
Problem:
Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?
Answer:
Weng earns 12/60 = $0.2 per minute. Working 50 minutes, she earned 0.2 x 50 = $10. #### 10

Problem:
Betty is saving money for a new wallet which costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?
Answer:
In the beginning, Betty has only 100 / 2 = $50. Betty's grandparents gave her 15 * 2 = $30. This means, Betty needs 100 - 50 - 30 - 15 = $5 more. #### 5

Problem:
A deep-sea monster rises from the waters once every hundred years to feast on a ship and sate its hunger. Over three hundred years, it has consumed 847 people. Ships have been built larger over time, so each new ship has twice as many people as the last ship. How many people were on the ship the monster ate in the first hundred years?
Answer:
Let S be the number of people on the first hundred years’ ship. The second hundred years’ ship had twice as many as the first, so it had 2S people. The third hundred years’ ship had twice as many as the second, so it had 2 * 2S = 4S people. All the ships had S + 2S + 4S = 7S = 847 people. Thus, the ship that the monster ate in the first hundred years had S = 847 / 7 = 121 people on it. #### 121

Problem:
James writes a 3-page letter to 2 different friends twice a week. How many pages does he write a year?
Answer:
He writes each friend 3*2=6 pages a week. So he writes 6*2=12 pages every week. That means he writes 12*52=624 pages a year #### 624

Problem:
James creates a media empire. He creates a movie for $2000. Each DVD cost $6 to make. He sells it for 2.5 times that much. He sells 500 movies a day for 5 days a week. How much profit does he make in 20 weeks?
Answer:
He sold each DVD for 6*2.5=$15. So he makes a profit of 15-6=$9. So each day he makes a profit of 9*500=$4500. So he makes 4500*5=$22,500 a week. He makes 22,500*20=$450,000 in total. Then after the cost of creating the movie he has a profit of 450,000-2000=$448,000 #### 448000
"""

    request = f"""Solve the following problem:
Problem:
{doc["question"]}
Answer:
"""

    return task + few_shot + request


def get_target(doc):
    answer = doc["answer"]
    target = re.search(r"#### ?(-?[0-9.,]+)", answer).group(1)
    return target
