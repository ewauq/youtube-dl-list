import os

cmd = 'py bin/youtube-dl'
opt = '-f "bestvideo[height<=1080]+bestaudio[ext=m4a]/best[ext=mp4]" --merge-output-format mp4 --output "videos/%(title)s [%(resolution)s].%(ext)s" --restrict-filenames'

print ("----------------------------------------------")
print ("> Lancement du téléchargement des vidéos")
print ("----------------------------------------------")

filepath = 'list.txt'
count = len(open(filepath).readlines())

with open(filepath) as fp:
  for cnt, line in enumerate(fp):
    print(f'\033[0;36;40m> [{cnt+1}/{count}] Téléchargement de {line}\033[0m \n> {cmd} {opt} {line}')
    os.system(f'{cmd} {opt} {line}')

print ("----------------------------------------------")
print ("> Téléchargement des vidéos terminé.")
print ("----------------------------------------------")