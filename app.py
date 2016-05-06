from holla import holla_server , holla_base_app
import json
        
A = holla_base_app()
B = {"aaa":"shfpisef", "gg":{"shdfisoe":6, "sues":89}}

@A.route("/Hello/<id>")
@A.route("/Hello")
def Hello(*args, **kw):
    return "Hello%s!"%(' %s'%kw.get('id', None) if kw.get('id', None) else '')
    
@A.route("/benchmark/json_test")
def j():
    return json.dumps(B)
    
@A.route("/benchmark/pure_text_test")
def hduw():
    return "AHAHHAHAHAHAHAHA"

holla_server(A).run_server(reload = False)
