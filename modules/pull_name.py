class Puller(object):
	def __init__(self, p_file, silent = False, format = []):
		import os
		self.os = os
		self.silent = silent
		self.format = format

		self.more_data_check = False

		root, filetitle = self.os.path.split(p_file)
		filename, extension = self.os.path.splitext(filetitle)
		self.filename = filename
		try:
			if len(self.format) == 0:
				self.get_format()
		except:
			self.get_format()
		self.name_data = {}
		self.main(filename) #for debugging
		self.pickup_answer = True
		self.end_format = self.format
	
	def main(self, filename):
		chop_format = self.format[:]
		filename = filename.split(' - ')
		while '-' in filename[:]:
			filename.remove("-")
		#print filename #for debugging
		#print self.format #for debugging
		try:
			for item in filename:
				# print item #for debugging
				# print chop_format #for debugging
				# print "=" * 10 #for debugging
				if len(chop_format) > 1:
					if chop_format[0] == 'discnumber' and chop_format[1] == 'tracknumber':
						self.name_data[chop_format[0]] = item[0]
						self.name_data[chop_format[1]] = item[1:]
						chop_format.pop(0)
						chop_format.pop(0)
					elif chop_format[1] == 'discnumber' and chop_format[0] == 'tracknumber':
						self.name_data[chop_format[0]] = item[-1]
						self.name_data[chop_format[1]] = item[:-1]
						chop_format.pop(0)
						chop_format.pop(0)
					else:
						# print "!!", chop_format[0] #for debugging
						self.name_data[chop_format[0]] = item
						chop_format.pop(0)
						# print "**", item #for debugging
				else:
					# print "!!", chop_format[0]#for debugging
					self.name_data[chop_format[0]] = item
					chop_format.pop(0)
		except IndexError:
			if self.more_data_check is False:
				answer = 'foobar'
				print "More data is available than specified by your naming format."
				while not (answer[0].lower() == 'y' or answer[0].lower() == 'n'):
					answer = self.get_input()
					if answer[0].lower() == 'n':
						raise Exception("User cancelled excecution")
					elif answer[0].lower() == 'y':
						self.more_data_check = True
		#print self.name_data #for debugging

	
	def get_format(self):
		if not self.silent:
			self.valid  = ['discnumber','tracknumber','artist','title','album']
			self.format = raw_input("Input parse format in pattern: 'item/album/artist/item'\nValid names are: 'discnumber','tracknumber','artist','title','album'\nSeperate items with a /\n!>> ")
			#print self.format #for debugging purposes
			self.format = self.format.split("/")
			print "Input format is: ", self.format 
			for item in self.format[:]:
				if not item in self.valid:
					self.format.remove(item)
			print "Parsed format is: ", self.format
			answer = "x"
			while not (answer[0].lower() == 'y' or answer[0].lower() == 'n'):
				answer = self.get_input()
				if answer[0].lower() == 'n':
					raise Exception("User cancelled excecution")
	def get_input(self):
		answer = None
		while not answer:
			answer = raw_input("Continue? (y/n): ")
		return answer

if __name__ == "__main__":
	start = Puller("000 - Unknown-Artist - Unknown-Track.mp3")