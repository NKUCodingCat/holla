d_header = {
        "Content-Type": "text/html",
        "Server":       "Holla/0.0.x"
      }
d_content = "This is the default response of Holla."
code_dict = {
    
    # ======= 2xx =============
    
    "200":"OK", 
    
    # ======= 4xx =============
    
    "400":"Bad Request",
    "401":"Unauthorized",
    "402":"Payment Required",
    "403":"Forbidden",
    "404":"Not Found",
    "405":"Method Not Allowed",
    "406":"Not Acceptable",
    "407":"Proxy Authentication Required",
    "408":"Request Timeout",
    "409":"Conflict",
    "410":"Gone",
    "411":"Length Required",
    "412":"Precondition Failed ",
    "413":"Payload Too Large ",
    "414":"URI Too Long ",
    "415":"Unsupported Media Type",
    "416":"Range Not Satisfiable ",
    "417":"Expectation Failed",
    "418":"I'm a teapot ",
    "421":"Misdirected Request",
    "422":"Unprocessable Entity",
    "423":"Locked",
    "424":"Failed Dependency",
    "426":"Upgrade Required",
    "428":"Precondition Required ",
    "429":"Too Many Requests",
    "431":"Request Header Fields Too Large",
    "451":"Unavailable For Legal Reasons",
    
    # ========== 5xx ========
    
    "500":"Internal Server Error"
     }

class Response(object):
    def __init__(self, content = d_content, status = 200, header = {}):
        self.header  = dict(d_header, **header).items()
        self.status  = "%s %s"%(status, code_dict[str(status)])
        self.content = content
        
    def __str__(self):
        return "<%s object @ %s> with \nstatus:  %s\nheaders: %s"%(self.__class__, hex(id(self)), self.status, repr(self.header))
        


class HTTPError(Exception):
    def __init__ (self, code = 500, info = ""):
        self.code = code
        self.info = info
        if self.info:
            print "Error %s Occured: <%s>"%(self.code, self.info)
        self.resp_obj = Response(self.info, code)
        self.header, self.status, self.content = self.resp_obj.header, self.resp_obj.status, self.resp_obj.content      
           
           
    def __str__(self):
        
        return "HTTPError - %s : Info: %s\nResponse object is \n"(self.code, self.info if self.info else "None", str(self.resp_obj))
        

    def error_web(self):
        
        return """
            
        """
     
    def error_json(self):
        
        pass