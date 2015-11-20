class Styles:
	'''
	Utility class for programmatically creating Qt Gui Style Sheets
	See readme for help.
	''' 
	class Style:
		def __init__(self, name):
			self.name = name
			self.commands = {}

		def set(self, command, value=''):
			if (command not in self.commands):
				self.commands[command] = ''
			self.commands[command] = value
			return self

		def __str__(self):
			string = self.name + ' {'
			for command in self.commands:
				string += ' ' + command + ' : ' + str(self.commands[command]) + ';  '
			string += '}'
			return string

	def __init__(self):
		self.rules = {}
		pass

	def __getitem__(self, index):
		if index not in self.rules.keys():
			self.rules[index] = self.Style(index)
		return self.rules[index]

	def __str__(self):
		string = ''
		for rule in self.rules.keys():
			string += str(self.rules[rule]) + ' '
		return string