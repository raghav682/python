class employee:
    def __init__(self):
        print("employr created")
    def __del__(self):
        print("destructor called")
obj=employee()
del obj
        
