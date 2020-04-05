import json
import random

from gtts import gTTS

# Language in which you want to convert
language = 'pl'


def resolve_phrase(phrase_dict, subject):
    phrase_template = phrase_dict['phrase']
    if isinstance(phrase_dict[subject['number']], dict):
        phrase_parts = phrase_dict[subject['number']][subject['gender']]
    else:
        phrase_parts = phrase_dict[subject['number']]

    if isinstance(phrase_parts, list):
        phrase = phrase_template.format(*phrase_parts)
    else:
        phrase = phrase_template.format(phrase_parts)
    return phrase


if __name__ == '__main__':
    with open('sebot-2k18/phrases.json', 'r') as f:
        phrases = json.load(f)

    openings = phrases['openings']
    subjects = phrases['subjects']
    actions = phrases['actions']

    parts_to_resolve = [
        phrases['fillers'],
        phrases['actions'],
        phrases['reasons'],
        phrases['endings']
    ]

    opening = random.choice(openings)
    subject = random.choice(subjects)
    seba = opening + subject['phrase']

    for part in parts_to_resolve:
        phrase = random.choice(part)
        if isinstance(phrase, dict):
            phrase = resolve_phrase(phrase, subject)
        seba += phrase

    sebacjusz = gTTS(text=seba, lang=language, slow=False)
    print(seba)
    sebacjusz.save("sebix.mp3")




