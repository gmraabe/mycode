#!/usr/bin/env python3
# towel01.py
# Micah Raabe

# Lab 77 - re.compile()

import re
hitchhiker = "The only person for whom the house was in any way special was Arthur Dent, and that was only because it happened to be the one he lived in. He had lived in it for about three years, ever since he had moved out of London because it made him nervous and irritable. He was about thirty as well, dark haired and never quite at ease with himself. The thing that used to worry him most was the fact that people always used to ask him what he was looking so worried about. He worked in local radio which he always used to tell his friends was a lot more interesting than they probably thought. It was, too - most of his friends worked in advertising."
mycomp = re.compile(r'\w+er\w+') # compiling mycomp as a reg ex
hikerexample = mycomp.findall(hitchhiker)
print("The results of our hikerexample:", hikerexample)
stringexample = mycomp.findall("This expression looks for places where a combination of the letters er exist and are also surrounded by atleast one case insenstive alphanumeric.")
print("The results of our stringexample:", stringexample)
print("\nCompiling Regular Expression Objects is very efficent.\n")
