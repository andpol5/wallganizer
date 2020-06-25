import urllib

urls = [
    'https://old.reddit.com/r/wallpaper/top/?sort=top&t=all'
    'https://old.reddit.com/r/wallpaper/top/?sort=top&t=all&count=25&after=t3_dy4hy2',
    'https://old.reddit.com/r/wallpaper/top/?sort=top&t=all&count=50&after=t3_e2bj3l',
    'https://old.reddit.com/r/wallpaper/top/?sort=top&t=all&count=75&after=t3_f8gk9h',
]

for u in urls:
    page = urllib.request.open.urlopen(a)
