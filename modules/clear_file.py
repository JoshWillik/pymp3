class Clearer(object): 
	def __init__(self, edit_file):
		import mutagen.easyid3 as foobar
		self.mp3 = foobar.EasyID3
		self.main(edit_file)
	def main(self, edit_file):
		try:
			delete_metadata= self.mp3(edit_file)
			delete_metadata.clear()
			delete_metadata.save()
			print edit_file, "successfully cleared"
		except ValueError:
			print "File has already been cleared, or an unknown error has occured"

if __name__ == "__main__":
	#for debugging, do not use as individual module
	import os
	Clearer(os.path.expanduser("~/lar.mp3"))