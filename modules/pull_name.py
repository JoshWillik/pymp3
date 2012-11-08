class Puller(object):
	def __init__(self, p_file, silent = False, format = []):
		import os
		self.os = os

		self.silent = silent #checks if the operation has been silented, used for 2-xnd operation
		self.format = format #for the first time through, needs to get format for names

		self.more_data_check = False #init variable for later use

		root, filetitle = self.os.path.split(p_file) #get rid of root
		filename, extension = self.os.path.splitext(filetitle) #get rid of extension
		self.filename = filename #make module wide
		try:
			if len(self.format) == 0: #if format is blank (on first operation it will be) get format
				self.get_format()
		except:
			self.get_format() #redundancy to make sure format is got if it doesn't exist
		self.name_data = {} #init storage area for data
		self.main(filename) 
		self.pickup_answer = True #used to silence the asking for format on next operation of module
		self.end_format = self.format #pass format up to parent for reuse on next run of module
	
	def main(self, filename):
		chop_format = self.format[:] #to not iterate through a list being modified
		error_message_file = filename #in case error occurs on file, preserve name for error message
		filename = filename.split(' - ') #split data into sections for identification
		while '-' in filename[:]: #remove any instances of dashes in filename, possibly redundant
			filename.remove("-")
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
					# print "!!", chop_format[0] #for debugging
					self.name_data[chop_format[0]] = item
					chop_format.pop(0)
		except IndexError:
			if self.more_data_check is False: #more_data_check could be set to true to avoid further error messages
				answer = 'foobar' #placeholder variable for edit later in operation
				print "More data is available than specified by your naming format." #message
				print filename ,": is not being fully used" #display harvested data
				while not (answer[0].lower() == 'y' or answer[0].lower() == 'n'):
					answer = self.get_input()
					if answer[0].lower() == 'n':
						print "###", error_message_file, " has been skipped" #change to exception to halt execution
					elif answer[0].lower() == 'y':
						self.more_data_check = True  #should preserve, but doesnt.
						#NOTE: silencing further more data warnings was decided against in development
						#code was left in place in case of future administrative decisions

		#print self.name_data #for debugging

	
	def get_format(self):
		if not self.silent: #if 1st operation
			self.valid  = ['discnumber','tracknumber','artist','title','album'] #valid names
			self.format = raw_input("Input parse format in pattern: 'item/album/artist/item'\nValid names are: 'discnumber','tracknumber','artist','title','album'\nSeperate items with a /\n!>> ")
			#print self.format #for debugging purposes
			self.format = self.format.split("/")
			print "Input format is: ", self.format 
			for item in self.format[:]: #remove invalid options from parsed format
				if not item in self.valid:
					self.format.remove(item)
			print "Parsed format is: ", self.format #display finished format
			answer = "x" #init variable for later use
			while not (answer[0].lower() == 'y' or answer[0].lower() == 'n'): #ask user
				answer = self.get_input()
				if answer[0].lower() == 'n':
					raise Exception("User cancelled excecution")
					
	def get_input(self): # reusable get input block
		answer = None
		while not answer:
			answer = raw_input("Continue? (y/n): ")
		return answer

if __name__ == "__main__":
	#modules not designed to function independantly, for testing purposes only
	start = Puller("000 - Unknown-Artist - Unknown-Track.mp3")