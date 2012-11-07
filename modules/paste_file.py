class Paster(object):
	def __init__(self, file_data, filename):
		import mutagen.easyid3 as mp3
		import os
		self.os = os
		self.used = mp3.EasyID3

		self.file_data = file_data
		self.main(file_data,filename)
	def main(self,data,filename):
		to_paste = self.used(self.os.path.expanduser(filename))
		for pair in data:
			to_paste[pair] = data[pair]
		to_paste.save()

if __name__ == "__main__":
	file_dat = {'tracknumber': '02', 'discnumber': '1', 'title': 'Love Has Found Us', 'artist': 'Bellarive'}
	start = Paster(file_dat, "~/lar.mp3")