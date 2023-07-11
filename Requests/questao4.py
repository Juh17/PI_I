import urllib.request

u = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsw2q3-y9LqecOewhnE7JbSTBAUDAo8m4R0g&usqp=CAU"

image = "ogum.jpeg"

urllib.request.urlretrieve(u, image)