# Input : 1+1=2 ---> Output : True \n 2
# Input : 1+1=3 ---> Output : False
# Input : 2^5+4^2-5*4-11=7+3^3-3*6+1 ---> Output True \n 17

equation = input().replace("=","==").replace("^","**")

x = eval(equation)
print(x)
if x: #if x==True
  print(int(eval(equation[:equation.index("=")])))
