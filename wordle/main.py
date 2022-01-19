import random 
from termcolor import colored


class Wordle:
	def __init__(self):
		self.word_list = self.load_word_list()
		self.dict_list = self.load_dict_list()
		self.word = random.choice(self.word_list).lower()
		self.history = []
		self.is_winner = False

	def load_word_list(self):
		with open("topwords.txt", "r") as file:
				allText = file.read()
				word_list = list(map(str, allText.split()))
		return word_list


	def load_dict_list(self):
		with open("dictionary.txt", "r") as file:
			allText = file.read()
			dict_list = list(map(str, allText.split()))
		dict_list = [word.lower() for word in dict_list]
		return dict_list

	def is_valid(self, word):
		return word in self.word_list

	def check(self, word):
		winner = 0
		checked_word = ""

		if word in self.dict_list:
			for i, letter in enumerate(word):
				if letter in self.word:
					if word[i] == self.word[i]:
						winner += 1
						checked_word += colored(letter, "green")		
					else: 
						checked_word += colored(letter, "yellow")	
				else:
					checked_word += letter
			
		else:
			checked_word += colored("not a valid word, try again", "red")
		if winner == len(self.word):
			self.winner(checked_word)
		else:
			return checked_word
	
	def winner(self, checked_word):
		self.is_winner = True 
		self.display_history()
		print(checked_word)
		print ("you win! it took you " + str(len(self.history) + 1) + " guess(es)!")
		


	def display_history(self):
		for entry in self.history:
			print (entry)

	def one_round(self, word, round):
		bad_move = colored("not a valid word, try again", "red")
		
		print ("====================")
		adjusted_round = len(self.word)-round + 1
		round_string = "round# " + str(adjusted_round)
		print (colored(round_string, "blue"))
		print ("--------------------")
		self.display_history()
		print ("--------------------")
		guess = input("guess: ")
		
	
		
		checked_word = self.check(guess)

		if checked_word == bad_move:
			print (checked_word)
			
			return round 
		

		else:
			self.history.append(checked_word)
			if not self.is_winner:
				self.display_history()
		
		
			return round - 1
				
			
	def game(self):
		print ("welcome to wordle!")
		print ("there are " + str(len(self.word)) + " total rounds because the word in question is " + str(len(self.word))+ " letters!")
		
		rounds = len(self.word)

		while rounds > 0 and not self.is_winner:
			rounds = self.one_round(self.word, rounds)
			print ("\n")
		
		if rounds == 0 and not self.is_winner:
			print (colored("you lost! the word was: " + self.word, "red"))


a = Wordle()
a.game()

