import datasets

def get_prompt(doc):
    task = """Answer the following question by selecting one of the proposed options. Answer based on the provided context.
Do not repeat the chosen answer. Always respond only with the number corresponding to the selected answer without further comment.
"""

    few_shot = """Here are 5 examples:
Context:
Make sure your hand is as relaxed as possible while still hitting all the notes correctly - also try not to make much extraneous motion with your fingers. This way, you will tire yourself out as little as possible. Remember there's no need to hit the keys with a lot of force for extra volume like on the piano. On the accordion, to get extra volume, you use the bellows with more pressure or speed.
Question:
According to the passage, what would not be considered an accurate tip for successfully playing the accordion?
Options:
1) For additional volume, increase the force with which you hit the keys
2) Keep unnecessary movement to a minimum in order to preserve your stamina
3) Be mindful of hitting the notes while maintaining a relaxed hand
4) Increase the speed with which you operate the bellows to achieve extra volume
Answer:
1

Context:
One of the most common problems when trying to convert a movie to DVD format is the overscan. Most televisions are made in a way to please the general public. For that reason, everything you see on the TV had the borders cut, top, bottom and sides. This is made to ensure that the image covers the whole screen. That is called overscan. Unfortunately, when you make a DVD, it's borders will most likely be cut too, and if the video had subtitles too close to the bottom, they won't be fully shown.
Question:
According to the passage, which of the following problems might one encounter when converting a movie to DVD format?	
Options:
1) An image that doesn’t fill the entire screen
2) Partially cut subtitles
3) An image that fills the entire screen
4) Cut borders
Answer:
2

Context:
"After its adoption by Congress on July 4, a handwritten draft signed by the President of Congress John Hancock and the Secretary Charles Thomson was then sent a few blocks away to the printing shop of John Dunlap. Through the night between 150 and 200 copies were made, now known as ""Dunlap broadsides"". The first public reading of the document was by John Nixon in the yard of Independence Hall on July 8. One was sent to George Washington on July 6, who had it read to his troops in New York on July 9. A copy reached London on August 10. The 25 Dunlap broadsides still known to exist are the oldest surviving copies of the document. The original handwritten copy has not survived."
Question:
Whose signature appeared on the handwritten draft?
Options:
1) John Dunlap
2) George Washington
3) John Nixon
4) Charles Thomson
Answer:
4

Context:
The American plan relied on launching coordinated attacks from three different directions. General John Cadwalder would launch a diversionary attack against the British garrison at Bordentown, in order to block off any reinforcements. General James Ewing would take 700 militia across the river at Trenton Ferry, seize the bridge over the Assunpink Creek and prevent any enemy troops from escaping. The main assault force of 2,400 men would cross the river nine miles north of Trenton, and then split into two groups, one under Greene and one under Sullivan, in order to launch a pre-dawn attack.
Question:
Where was there a British garrison located?
Options:
1) Assunpink Creek
2) Trenton
3) Bordentown
4) Princeton
Answer:
3

Context:
The Colonists, seeing this activity, had also called for reinforcements. Troops reinforcing the forward positions included the 1st and 3rd New Hampshire regiments of 200 men, under Colonels John Stark and James Reed (both later became generals). Stark's men took positions along the fence on the north end of the Colonist's position. When low tide opened a gap along the Mystic River along the northeast of the peninsula, they quickly extended the fence with a short stone wall to the north ending at the water's edge on a small beach. Gridley or Stark placed a stake about 100 feet (30 m) in front of the fence and ordered that no one fire until the regulars passed it.
Question:
According to the passage, when did Stark’s men extend their fence?
Options:
1) While the Colonists called for reinforcements
2) After the regulars passed the stake
3) During low tide
4) While troops assumed forward positions
Answer:
3
"""

    request = f"""Answer the following question:
Context:
{doc["flores_passage"]}
Question:
{doc["question"]}
Options:
1) {doc["mc_answer1"]}
2) {doc["mc_answer2"]}
3) {doc["mc_answer3"]}
4) {doc["mc_answer4"]}
Answer:
"""

    return task + few_shot + request

def doc_to_target(doc):
    a_idx = doc["correct_answer_num"]

    return a_idx

def process_docs(dataset: datasets.Dataset):
    example_idcs = [0, 3, 5, 4, 8]
    dataset = dataset.select(
        (
            i for i in range(len(dataset)) 
            if i not in set(example_idcs)
        )
    )
    return dataset
