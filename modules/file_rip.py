class Ripper(object):
	def __init__(self, m_file):
		self.mp3_file=m_file
		self.main()
	def main(self):
		editable   = mp3(self.mp3_file)
		f_artist   = editable['artist'][0].encode('utf-8')
		f_title    = editable['title'][0].encode('utf-8')
		f_cd_num   = editable['discnumber'][0].encode('utf-8')
		f_song_num = editable['tracknumber'][0].encode('utf-8')
		#print editable
		if f_cd_num:
			f_cd_num=f_cd_num[0]
		if f_song_num:
			f_song_num=f_song_num[0]
		song_data = {'title':f_title,'artist':f_artist,'cd_number':f_cd_num,'song_number':f_song_num}
		print song_data
		self.song_data = song_data


if __name__ == "__main__":
	from sys import argv
	from libs.mut.mutagen.easyid3 import EasyID3 as mp3
	#import parse_config TODO
	base_args = argv
	modified = base_args[1]
	print modified
	dat = Ripper(modified)
	print dat
	print dat.song_data