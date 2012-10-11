class Ripper(object):
	def __init__(self, m_file):
		from libs.mut.mutagen.easyid3 import EasyID3 as mp3
		self.mp3 = mp3
		self.m_file = m_file
		if mp3(m_file):
			self.editable = mp3(m_file)
			self.main()
	def main(self):
		#editable   = mp3(self.mp3_file)
		try:
			f_artist = self.editable['artist'][0].encode('utf-8')
		except KeyError:
			f_artist = "Unknown-Artist"
		try:
			f_title    = self.editable['title'][0].encode('utf-8')
		except KeyError:
			f_title = "Unknown-Track"
		try:
			f_cd_num = self.editable['discnumber'][0].encode('utf-8')
		except KeyError:
			f_cd_num = "0"
		try:
			f_song_num = self.editable['tracknumber'][0].encode('utf-8')
		except KeyError:
			f_song_num = "00"
		try:
			f_album    = self.editable['album'][0].encode('utf-8')
		except:
			f_album = "Unknown-Album"
		# print editable #for debugging-6
		if f_cd_num:
			f_cd_num=f_cd_num[0]
		if f_song_num:
			f_song_num=f_song_num[0]
		if len(f_song_num)+len(f_cd_num) < 3:
			f_song_num = '0'+f_song_num

		song_data = {'title':f_title,'artist':f_artist,'discnumber':f_cd_num,'tracknumber':f_song_num, 'album':f_album, '-':'-'}
		#print song_data #for debugging
		self.song_data = song_data
		#print "\nData pulled from ", self.m_file, "is\n",song_data for debugging only
	def clear(self):
		for i in self.editable:
			self.editable[i]=None
		print self.mp3(self.m_file)


if __name__ == "__main__":
	from sys import argv
	#import parse_config TODO
	base_args = argv
	#print base_args #for debugging
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
		#print dat #for debugging
		#print dat.song_data #for debugging
		pass