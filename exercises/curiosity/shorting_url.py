import short_url
entrada=input()
size = short_url.encode_url(477)
url = short_url.UrlEncoder(entrada)
print(url)
