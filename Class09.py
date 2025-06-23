def sum(*a: int)->int: #a will be multiple value
 sum = 0
 for i in a:
  sum= sum+i
 return sum

print(sum(1,2,3,4))



def info(naem:str,matial_status:bool,age:int int=30):#jis ko value dani vo last ma ho by default
 print('name',naem)
 print('age',age)
 print('matial_status',False)


#potion only arguments 

def posfun(x,y,/,z): #/ sy phaly jitny b arguments ho gy potion ma ho gy
 print(x+y+z)

#keyword only arguments # 
#lamda function
#global scope local scope