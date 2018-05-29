import pandas as pd
import string
#from statistics import mean, stdev

df0 = pd.read_csv("the-office-lines - scripts.csv")
df = df0[df0.season <= 7]


main = ["Michael", "Jim", "Pam", "Dwight"]
characters = ["Michael", "Jim", "Pam", "Dwight", "Phyllis", "Stanley",
				"Angela", "Oscar", "Kevin", "Ryan", "Jan", "Toby", "Darryl", 
				"Creed", "Kelly", "Andy", "Karen", "Holly", "Roy", "Erin", 
				"Gabe", "David"]

def debracket(words):
	i = 0
	while i < len(words):
		if words[i] == "":
			del words[i]
			i -= 1
		elif words[i][0] == "[":
			while "]" not in words[i]:
				del words[i]
			del words[i]
		i += 1
	return words

def depunctuate(word):
	return word.translate(None, string.punctuation)

def normalize_word(word):
	foo = depunctuate(word).lower()
	return foo.replace(" ", "")

def normalize_text(text):
	nobracket = debracket(text)
	return map(normalize_word, text)

def getwords(name):
	char = df.speaker == name
	not_deleted = df.deleted == False

	char_df = df[char & not_deleted]
	#gets the data frame for this character

	char_lines = list(char_df.line_text)
	#gets the character's lines
	#print "This character has %d lines" % len(char_lines)

	char_text = " ".join(char_lines)
	#turns the list of lines into a single string

	char_words = char_text.replace("-", " ").split()
	#turns the string into a list of words
	#print "This character says %d words" % len(char_words)
	return normalize_text(char_words)

def word_count(name):
    return len(getwords(name))

def word_lengths(name):
    return map(len, getwords(name))

def add_entry(dictionary, key):
    if key in dictionary:
        dictionary[key] = dictionary[key] + 1
    else:
        dictionary[key] = 1

def getdict(name):
	d = {}
	words = getwords(name)

	for word in words:
		add_entry(d, word)

	#print "This character says %d distinct words" % len(d)
	return d

def getmax(dict, num):
	k = list(dict.keys())
	v = list(dict.values())

def mentions(name1, name2):
	d = getdict(name1)
	if name2.lower() in d:
		return d[name2.lower()]
	else:
		return 0

def get_scenes(name):
	char = df.speaker == name
	char_df = df[char]

	s = list(char_df.season)
	e = list(char_df.episode)
	sc = list(char_df.scene)

	scenes = []
	for i in range(len(s)):
		scenes.append([s[i], e[i], sc[i]])

	return scenes

def intersection(list1, list2):
	list3 = [value for value in list1 if value in list2]
	return list3

def scenes(name1, name2):
	scenes1 = get_scenes(name1)
	scenes2 = get_scenes(name2)

	shared = intersection(scenes1, scenes2)
	return shared

def analyze(name):
	print
	print "Character \t Scenes shared with %s \t Mentioned by %s \t Mentions %s" % (name, name, name)
	for char in characters:
		if char != name:
			print char + "\t\t %d \t\t\t\t %d \t\t\t %d" % (len(scenes(name, char)), mentions(name, char), mentions(char, name))
	print

name = 'A'
while name.lower() != 'q':
	print
	name = raw_input("Which character's data do you want to see? (Or enter Q to quit)  ")
	if name in characters:
		analyze(name)
	elif name.lower() != "q":
		print name.lower()
		print "Sorry, try again."

"""
print "Pam shares %d scenes with Jim and mentions his name %d times" \
		% (len(scenes("Pam", "Jim")), mentions("Pam", "Jim"))

longest = max(word_lengths("Michael"))
test = word_lengths("Michael").remove(1)
print test
#nextlongest = max(test)
#print nextlongest
for key in getdict("Michael"):
	if len(key) == longest:
		print key
"""

"""
mentions_dict = {}

for name1 in main:
	mentions_dict[name1] = {}
	for name2 in main:
		mentions_dict[name1][name2] = mentions(name1, name2)
"""

#print mentions_dict

#print "Michael mentions Jim's name %d times" % mentions("Michael", "Jim")


#analyze("Jim")
"""
michael = getwords("Michael")
test = []
for i in range(50):
	test.append(michael[i])

normal = normalize_text(test)
#print normal
print getdict(normal)
	
print mylist
print "now without brackets..."
print debracket(mylist)
"""

#test = getwords('Michael')
#test2 = debracket(test)
#print test2

print 'THE PROGRAM HAS ENDED'