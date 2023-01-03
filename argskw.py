def function(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)
    for key , value in kwargs.items():
        print(f"{key} in {value}")


normal="i am a good guy"
args = ["Tanmoy","Laptop","Devops"]
kwargs ={"Learn": "Devops", "code":"python","knowlege": "networks"}
function(normal, *args, **kwargs )