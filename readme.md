### Fonctionnement

Le script utilise [youtube-dl](https://github.com/ytdl-org/youtube-dl) pour récupérer la meilleure qualité de vidéo (1080p max) et la meilleure qualité audio, et les fusionne ensuite grâce à ffmpeg.

Installer ffmpeg pour la fusion de l'audio et la vidéo
> brew install ffmpeg

Ajouter les liens Youtube des vidéos à télécharger dans `list.txt`
> https://www.youtube.com/watch?v=xiD40jt4aKU

Lancer le téléchargement des vidéos
> py download.py // sur Windows
> python download.py // sur MacOS

Toutes les vidéos sont stockées dans le dossier `videos`.
