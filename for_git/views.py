class HttpRreponse(object):
    pass


def index(request):
    return HttpRreponse("ok")

def test(request):
    print("dev分支代码")