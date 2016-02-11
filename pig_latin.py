__author__ = 'ano'

class PigLatin:
	def __init__(self):
		self.choice = raw_input("Enter \n(1) to translate a single word \n(2) to translate a sentence \n(3) to translate word containing hyphens: ")

		if self.choice == '1':
			self.plainText = raw_input("\nEnter plaintext word : ")
			#print self.plaintext
			print self.translate_single_word(self.plainText)
		elif self.choice == '2':
			self.plainText = raw_input("\nEnter a sentence of plaintexts : ")
			#print self.plainText
			print self.translate_sentence(self.plainText)
		elif self.choice == '3':
			self.plainText = raw_input("\nEnter a sentence of plaintexts containing hyphens : ")
			#print self.plainText
			self.translate_sentence_with_hyphens(self.plainText)
		else:
			print "Wrong Choice!!!!"

	def translate_single_word(self , plainText):
		vowels = 'aeiou'
		vowelsup = vowels.upper()
		consonants = 'bcdfghjklmnpqrstvwxyz'
		consonantsup = consonants.upper()

		if len(plainText) > 0:
			if (plainText[0] in vowels or plainText[0] in vowelsup) and (plainText[len(plainText) - 1] in consonants or plainText[len(plainText) - 1] in consonantsup) and plainText[len(plainText) - 1] not in ['y' , 'Y']:
				#print plainText[0] , plainText[len(plainText) - 1]
				return plainText + 'ay'
			elif (plainText[0] in vowels or plainText[0] in vowelsup) and (plainText[len(plainText) - 1] in vowels or plainText[len(plainText) - 1] in vowelsup) and plainText[len(plainText) - 1] not in ['y' , 'Y']:
				#print plainText[0] , plainText[len(plainText) - 1]
				return plainText + 'yay'
			elif (plainText[0] in vowels or plainText[0] in vowelsup) and plainText[len(plainText) - 1] in ['y' , 'Y']:
				return plainText + 'nay'
			else:
				const_char = ""
				for char in plainText:
					if char in consonants or char in consonantsup:
						const_char += char.lower()
					else:
						break
				if plainText[0].isupper():
					return plainText[len(const_char):].capitalize() + const_char + 'ay'
				else:
					return plainText[len(const_char):] + const_char + 'ay'
		else:
			return "Nil"

	def translate_sentence(self , plainText):
		strli = plainText.split()
		#print strli
		newli = []
		for i in range(len(strli)):
			a = strli.pop()
			a = self.translate_single_word(a)
			newli.insert(i , a)
		newli.reverse()
		return ' '.join(newli)

	def translate_sentence_with_hyphens(self , plainText):
		strli = plainText.split('-')
		#print strli
		newli = []
		for i in range(len(strli)):
			a = strli.pop()
			a = self.translate_sentence(a)
			newli.insert(i , a)
		newli.reverse()
		print '-'.join(newli)

p = PigLatin()
