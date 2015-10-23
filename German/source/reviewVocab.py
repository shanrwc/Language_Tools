#!/usr/bin/python
import sys
import random

print "Welcome to your German vocabulary review!"
rounds = raw_input("How many rounds would you like in this session?   ")
while (rounds.isdigit() == False):
    rounds = raw_input("I'm sorry, I can't use that number; enter another:   ")

rounds = int(rounds)

print "Great! "+str(rounds) + " it will be!" 

#Now load vocab files
vocab = []
f = open("data/vocab_foodAndeating.txt","r")
for line in f:
    pieces = line.split("\t\t")
    vocab.append([pieces[0],pieces[1].rstrip()])

#print vocab
print "\n\n\n\n"

#Print any necessary instructions
print "Please translate the following."
print "Include definite articles if shown."

correct = 0
wrong = 0
for i in xrange(rounds):
    words = list(random.choice(vocab))
 #   print words
    index = random.randrange(0,2)
#    print index
    test = words.pop(index)
    if (len(words) < 1):
        print "problem with list entry! "+ test
    answer = words[0]
    query = raw_input(test+":   ")
    if (str(query) == answer):
        print "Correct!"
        correct += 1
    else:
        print "Nope! The answer is "+answer
        wrong += 1


print "Your score: "
print str(correct) + " translations correct"
print str(wrong) + " translatations wrong"
print "Thank you, and good-bye!"
