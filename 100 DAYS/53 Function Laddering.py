
# fucntion ladderiing
def calc():
    def subs(a,b):
        def addd(a,b):
            print(f"add : a={a},b={b}")
        print(f"sub : a={a},b={b}")
        return addd
    return subs

calc()(4,5)(8,1)