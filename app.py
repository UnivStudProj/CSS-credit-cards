import eel

eel.init("web")


@eel.expose
def call_in_js(x):
    print(x)
    
    
eel.call_in_python("Hwww")

eel.start("index.html", size=(700, 700))