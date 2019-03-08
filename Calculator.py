#!C:\Program Files\Python37\python
def calculate(a,b,op):
    if op=='Addition':
        print("sum of two numbers is",int(a)+int(b))
    elif op=='Subtraction':
        print("Subtraction of two numbers is",int(a)-int(b))
    elif op=='Multiplication':
        print("Multiplication of two numbers is",int(a)*int(b))
    elif op=='Modulus':
        print("Modulus of two numbers is",int(a)%int(b))
        

import cgi
print("Content-type:text/html\n")
print("<html>")
print("<heasd><title>My second CGI program</title>")
print("</head>")
print("<body>")
form=cgi.FieldStorage()
a=form.getvalue("first")
b=form.getvalue("second")
op=form.getvalue("operation")
print('<form method="post" action="calculator.py">')
print('<p>Enter first number: <input type="text" name="first"/></p>')
print('<p>Enter second number: <input type="text" name="second"/></p>')
print('<p>Select operation:</p> <select name="operation"><option>Addition</option><option>Subtraction</option><option>Multiplication</option><option>Modulus</option></select>')
print('<input type="submit" value="Submit"/>')
print('<br>')
print('<br>')
print('</body>')
print('</html>')
print('\n')
calculate(a,b,op)