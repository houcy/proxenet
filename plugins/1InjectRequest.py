import pimp

def pre_request_hook(request_id, request):
    r = pimp.HTTPRequest(request)
    r.add_header("X-Intercepted-By", "proxenet")
    return str(r)

    
def post_request_hook(request_id, req):
    return req
    

if __name__ == "__main__":
    get_req  = "GET   /   HTTP/1.1\r\nHost: foo\r\n\r\n"
    post_req = "POST / HTTP/1.1\r\nHost: foo\r\nContent-Length: 5\r\n\r\nHello"
    
    print pre_request_hook(get_req)
    print pre_request_hook(post_req)
    
