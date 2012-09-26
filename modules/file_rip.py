class Ripper(object):
	def __init__(self, m_file):
		self.mp3=m_file
		self.main()
	def main(self):
		editable = ID3(self.mp3)
		f_artist = editable.artist
		f_title  = editable.title
		f_cd_num = 
		print editable
		print f_title
		print f_artist
		print f_cd_num
		print f_song_num


if __name__ == "__main__":
	from sys import argv
	from id3f.ID3 import *
	base_args = argv
	modified = base_args[1]
	Ripper(modified)

