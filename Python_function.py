#def keyword fun_name(parameters):
#stmt(body part)
#retun
def sum(a,b):
    print(a+b)
sum(9,6)
#function with default argument
def myfun(x,y=90):
    print("x=",x)
    print("y=",y)
myfun(20)
#lambda function :
#[lambda keyword argument:expresion]

def cube(y):
    return y*y*y
l_cube=lambda y:y*y*y
print("using fun def with def keyword,cube:",cube(5))
print("using lambda fun cube:",l_cube(5))
