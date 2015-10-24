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
    pieces = line.split("---")
    if len(pieces) < 2: 
        print "problem with "
        print pieces
    vocab.append([pieces[0],pieces[1].rstrip()])

print vocab
print "\n\n\n\n"

#Print any necessary instructions
print "Please translate the following."
print "Include definite articles if shown."
print "To indicate an umlaut (if you don't have those keys),"
print "follow the letter needing the umlaut with a ':'"

print "\n\n\n\n"

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
    if "a:" in query:
        query = query.replace("a:","\xc3\xa4")
    if "u:" in query:
        query = query.replace("u:","\xc3\xbc")
    if "o:" in query:
        query = query.replace("o:","\xc3\xb6")
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
