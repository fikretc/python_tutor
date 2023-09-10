from pprint import pprint


class HtmlDocument:
    extension = 'html'
    version = '5'


HtmlDocument.media_type = 'text/html'

print("dict of class variables:")
pprint(HtmlDocument.__dict__)
 # dict of class variables

print(f"HtmlDocument.__name__: {HtmlDocument.__name__}") # HtmlDocument

print(type(HtmlDocument))  # <class 'type'>
print(isinstance(HtmlDocument, type)) # True

print(HtmlDocument.extension) # html
print(HtmlDocument.version) # 5

extension = getattr(HtmlDocument, 'extension')
version = getattr(HtmlDocument, 'version')

print(extension)  # html
print(version)  # 5

media_type = getattr(HtmlDocument, 'media_type', 'text/html')
print(media_type) # text/ 

HtmlDocument.version = 10 # class variable
setattr(HtmlDocument, 'version', 10) # class variable
print(f"HtmlDocument.version: {HtmlDocument.version}")

HtmlDocument.media_type = 'text/html'
print(f"HtmlDocument.media_type: {HtmlDocument.media_type}" )

delattr(HtmlDocument, 'version') #delete attribute of class
# print(f"HtmlDocument.version (error): {HtmlDocument.version}")
