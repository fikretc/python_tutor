from pprint import pprint


class HtmlDocument:
    version = 5
    extension = 'html'


pprint(HtmlDocument.__dict__)

print(HtmlDocument.extension)
print(HtmlDocument.version)
home = HtmlDocument()
pprint(home.__dict__)
print(type(home.__dict__))
home.version = 6
pprint(home.__dict__)

HtmlDocument.media_type = 'text/html' #change class var
print(home.media_type)
