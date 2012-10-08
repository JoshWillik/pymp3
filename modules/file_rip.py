class Ripper(object):
	def __init__(self, m_file):
		if mp3(m_file):
			self.editable = mp3(m_file)
			self.main()
	def main(self):
		#editable   = mp3(self.mp3_file)
		f_artist   = self.editable['artist'][0].encode('utf-8')
		f_title    = self.editable['title'][0].encode('utf-8')
		f_cd_num   = self.editable['discnumber'][0].encode('utf-8')
		f_song_num = self.editable['tracknumber'][0].encode('utf-8')
		f_album    = self.editable['album'][0].encode('utf-8')
		#print editable
		if f_cd_num:
			f_cd_num=f_cd_num[0]
		if f_song_num:
			f_song_num=f_song_num[0]
		song_data = {'title':f_title,'artist':f_artist,'cdnumber':f_cd_num,'tracknumber':f_song_num, 'album':f_album}
		print song_data
		self.song_data = song_data


if __name__ == "__main__":
	from sys import argv
	from libs.mut.mutagen.easyid3 import EasyID3 as mp3
	#import parse_config TODO
	base_args = argv
	try: 
		modified = base_args[1]
	except:
		raise Exception('\033[1;38mNo target file specified\033[1;m') #formatt error to grab attention
	script = base_args[0]
	try:
		dat = Ripper(modified)
	except:
		raise Exception("File does not exist, is not an mp3, or is corrupted.")
	else:
		print dat
		print dat.song_data