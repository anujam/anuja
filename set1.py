import sys
my_sentence = "the name of my dog is tommy"
my_sentence = my_sentence.lower()
my_set1 = set(my_sentence)
print my_set1
print len(my_set1)
my_set2="ilovemypapa"
my_set2 = set(my_set2)
print my_set2
print len(my_set2)
inter = my_set1.intersection(my_set2)
print inter
print len(inter)
uni = my_set1.union(my_set2)
print uni
print len(uni)
