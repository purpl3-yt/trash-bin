import glob
import os

for i in glob.glob('*.mp3'):
    if i.find('[SPOTIFY-DOWNLOADER.COM]')!=-1:
        try:
            os.rename(i,i[int(i.find('[SPOTIFY-DOWNLOADER.COM]'))+len('[SPOTIFY-DOWNLOADER.COM]')+1:])
        except FileExistsError:
            pass