# see http://hyperstition.abstractdynamics.org/archives/003609.html
import string
from random import choice, getrandbits
from cStringIO import StringIO

class Isopsephia:
	def __init__(self, file_contents):
		self.gematria = dict(
			zip(
				(a for a in string.ascii_lowercase),
				(i for i in xrange(10,36))
			)
		)
		self.gematria.update(dict(((str(i),i) for i in xrange(0,10))))
		self.gematria[' ']=0
		self.mapping = self.map_content(file_contents)

	def numogram(self,phrase):
		letters = phrase.lower()
		return sum(self.gematria[l] for l in letters if l.isalnum())

	def reduce(self,phrase):
		return self.numogram(phrase) % 9 or 9

	def map_content(self,content):
		mapping = dict(([i,[]] for i in xrange(1,10)))
		io = StringIO(content)
		for line in io:
			# store words in lists attached to dictionary keys 1-9
			for word in line.split():
				reduction = self.reduce(word)
				if word not in mapping[reduction]:
					mapping[reduction].append(word)
		return mapping

	def generate_text(self):
		pie = str(getrandbits(45))
		pie = pie.replace("0","")
		sentence = ''
		for n in pie:
			sentence += choice(self.mapping[int(n)]) + " "
		return sentence
