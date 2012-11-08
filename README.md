NOTE: Requires installed mutagen library (included, see /modules/libs for details)

Summary: 
non-destructive: moves non-mp3 files to a .delete directory (which is created in the directory the script runs in)
to prevent script from deleting half your library on a bug. it seemed safer that way
Ignores all hidden folders (like .info, .readme.txt, .etcetc, if you want to store data inside the directory without it getting removed)
supports taking metadata and putting it into the file name according to a format specified in ~/.py_mp3.conf
if xfile.xtension already exists in trash, rename target file to xfile(1).xtension. If that doesn't work, try xfile.(2).xtension and so on and so forth

Development: 
Next in the possible development cue are:
installability (extra option, will require investigation and experimentation, please contact for more details)

-c <or> --directory
specifies working directory (required most of the time)
ex: ./pymp3 -c ~/Music <or> ./py_mp3 --directory ~/Music

-r <or> --rip-file
pulls data from file and pastes in file-name
ex: ./pymp3 -c ~/Music -r <or> ./py_mp3 -c ~/Music --rip-file

-d <or> --default-config
resets the config file at ~/.py_mp3.conf to the default format
ex: ./pymp3 -d <or> ./pymp3 --default-config
note: will halt the rest of the program execution

-p <or> --print-metadata:
Prints metadata formatted according to ~/.py_mp3.conf format
ex: ./pymp3 -c ~/Music -p <or> ./pymp3 -c ~/Music --print-metadata

-t <or> --pull-title
pulls data from file title and pastes metadata
ex: ./pymp3 -c ~/Music -t or ./pymp3 -c ~/Music --pull-title

Extra notes: 
Running any operation except -d will move incompatable files to .delete
Invalid files marked .mp3 *should* be passed over with a printed warning.
All hidden files or folders will be ignored, so place important extra data in them

Limitations:
Will not work for folders that have more than 991 duplicate files
Will not work for discnumbers greater than 9
Pulling data from the filename will not work with extra -'s in the title