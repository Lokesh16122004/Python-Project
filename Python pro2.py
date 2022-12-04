

import random
when = ["A few years ago" , "Last night" , "A long time ago" , "On 20th Jan"]
who = ["a rabbit" , "an elephant" , "a mouse" , "a turtle" , "a cat"]
name = ["Yash","Monty" , "Jojo" , "Pampi"]
residence = ["India" , "Germany" , "England" , "Venice"]
went = ["cinema" , "university" , "seminar" , "school" , "function"]
happened = ["made a lot of friends" , "Eats a burger" , "found a secret key" , "participated in dance"]

randomwhen = random.choice(when)
randomwho = random.choice(who)
randomname = random.choice(name)
randomresidence = random.choice(residence)
randomwent = random.choice(went)
randomhappened = random.choice(happened)

story = randomwhen + " , " + randomwho + " called " + randomname + " that lived in " + randomresidence + " went to a " + randomwent + " and " + randomhappened + "."

print(story)
