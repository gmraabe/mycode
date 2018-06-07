#!/usr/bin/env python3
# narwhalrunner.py
# Micah Raabe

# Lab 76 - re.sub()

import re
androidsDream = "In the sumptuous and enormous hotel room Rick Deckard sat reading the typed carbon sheets on the two androids Roy and Irmgard Baty. In these two cases telescopic snapshots had been included, fuzzy 3-D color prints which he could barely make out. The woman, he decided, looks attractive. Roy Baty, however, is something different. Something worse. A pharmacist on Mars, he read. Or at least the android had made use of that cover. In actuality it had probably been a manual laborer, a field hand, with aspirations for something better. Do androids dream? Rick asked himself. Evidently; that's why they occasionally kill their employers and flee here. A better life, without servitude. Like Luba Luft; singing Don Giovanni and Le Nozze instead of toiling across the face of a barren rock-strewn field. On a fundamentally uninhabitable colony world."
meetsteven = re.sub(r'Roy', 'Steven', androidsDream)
noandroids = re.sub(r'android', 'narwhal', meetsteven)
print("Our new story featuring Steven Baty and his narwhal friends:\n", noandroids)

novowels = re.sub(r'[aeiou]+', '', androidsDream)    # remove any vowels and replace with an empty string
print("\nr nw stry ftrng Stvn Bty nd hs nrwhl frnds:\n", novowels)

exciting = re.sub(r'\.', '!!', androidsDream)
print("\nOur new exciting story featuring Steven Baty and his narwhal friends:\n", exciting)
