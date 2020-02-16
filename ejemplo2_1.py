from urllib.request import urlopen

html = urlopen('http://localhost:8000/ejemplo2.php')

print(html.read().decode('utf-8'))
