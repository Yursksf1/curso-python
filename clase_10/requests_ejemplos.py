import requests

#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://jsonplaceholder.typicode.com/posts/1')

#print the response text (the content of the requested file):
#print(x.text)

#print(x.json())

respuesta = x.json()
print(respuesta["title"])