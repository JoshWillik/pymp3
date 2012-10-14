class Puller(object):
	def __init__(self, filename):
		self.filename = filename
		self.valid  = ['discnumber','tracknumber','artist','title','album']
		self.format = raw_input("Input parse pattern in format /item/item/item\nValid names are: 'discnumber','tracknumber','artist','title','album'\nSeperate items by with a /\n>> ")
		print self.format #for debugging purposes
		self.format = self.format.split("/")
		print self.format #for debugging purposes
		for item in self.format[:]:
			if not item in self.valid:
				self.format.remove(item)
		print "Parsed format is: ", self.format
		answer = " ";
		while not (answer[0].lower() == 'y' or answer[0].lower() == 'n'):
			answer = raw_input("Continue? (y/n): ")
		if answer[0].lower() == 'n':
			raise Exception("User cancelled excecution")
		self.main(filename) #for debugging
	def main(self, filename):
		filename = filename.split()
		while '-' in filename:
			filename.remove("-")
		print filename
		print self.format



if __name__ == "__main__":
	start = Puller("000 - Unknown-Artist - Unknown-Track")