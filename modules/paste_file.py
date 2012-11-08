class Paster(object):
	def __init__(self, file_data, filename):
		import mutagen.easyid3 as mp3
		import os
		self.os = os
		self.used = mp3.EasyID3

		self.file_data = file_data
		self.main(file_data,filename)
	def main(self,data,filename):
		try:
			to_paste = self.used(self.os.path.expanduser(filename))
			for pair in data:
				to_paste[pair] = data[pair]
			to_paste.save()
		except:
			print filename, " is not an mp3, is corrupted, or is otherwise unusable"
			
if __name__ == "__main__":
	#modules not designed to function independantly, for testing purposes only
	file_dat = {'tracknumber': '02', 'discnumber': '1', 'title': 'Love Has Found Us', 'artist': 'Bellarive'}
	start = Paster(file_dat, "~/lar.mp3")