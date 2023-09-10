class Request:
    def send():
        print('Sent')
    def send1(self):
        print('Sent allready')


class RequestPlus:
    def send(*args):
        print('Sent', args)

Request.send()

print(Request.send)
print(type(Request.send))
http_request = Request()
print(http_request.send)
print(type(Request.send) is type(http_request.send))

print(type(http_request.send))  # <class 'method'>
print(type(Request.send))  # <class 'function'>

RequestPlus.send()
http_request_plus = RequestPlus()
http_request_plus.send()

http_request.send1()


