

#coding=utf-8
print("hello chenlei")
print("请输入第一个数值")
num1 = float(input())
print("请输入第二个数值")
num2 = float(input())
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")
ysf=int(input())
def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def division(x,y):
    return x / y
if ysf==1:
    print(num1, "+", num2, "=", addition(num1, num2))
elif ysf==2:
    print(num1, "-", num2, "=", subtraction(num1, num2))
elif ysf==3:
    print(num1, "*", num2, "=", multiplication(num1, num2))
elif ysf==4:
    print(num1, "/", num2, "=", division(num1, num2))
else:
    print("非法输入")