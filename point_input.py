input=input("Please enter an point where x and y coordinates are separated by comma (i.e. 20,-10.23):")
x,y=map(float,input.split(","))
sq_x=x**2
sq_y=y**2
print("x^2: ",sq_x,", y^2: ",sq_y,"")