import streamlit as st
st.set_page_config(
        page_title="Python Lab Codes",
        page_icon="snake",
        layout="wide",
    )
st.title("Python Lab Codes")
st.markdown('<hr style="border-top: 2px solid #0074D9;">', unsafe_allow_html=True)
a,b,c = st.columns(3)

with a:
    with st.container(border=True):
        st.subheader("Lab-1 16th July 2024")
        with st.expander("Area of Triangle"):
            st.code('''
#Write a Python program that takes the base and height of a triangle as input
#from the user and prints the area.

base = float(input("Enter base length of the triangle: "))
height = float(input("Enter height of the triangle: "))

print("Area of triangle = ",0.5*base*height," cm2")

''')
        with st.expander("Salary"):
            st.code('''
#Create a Python program that takes the basic salary, HRA (House Rent
#Allowance), and DA (Dearness Allowance) as input from the user and prints
#the total monthly salary.

basic = int(input("Enter basic salary: "))
HRA = int(input("Enter HRA: "))*-1
DA = int(input("Enter DA:"))

print("Total Monthly Salary = ",basic+HRA+DA)


''')

        with st.expander("Area of Circle"):
            st.code('''
#Write a Python program that takes the radius of a circle as input from the
#user and prints the area. (Use π = 3.14159)

radius = float(input("Enter the radius of the circle: "))
pi = 3.14159
print("Area of the circle is: ",pi*radius*radius,"cm2")


''')
        with st.expander("Celcius to Fahrenheit"):
            st.code('''
#Design a Python program that takes the temperature in Celsius as input from
#the user and prints the temperature in Fahrenheit.

c = float(input("Enter the temperature in celsius: "))
f = ((9/5)*c)+32.0

print("The temperature in fahrenheit is: ",f," F")
''')
        with st.expander("Perimeter of Rectangle"):
            st.code('''
#Implement a Python program that takes the length and width of a rectangle
#as input from the user and prints the perimeter.

length = int(input("Enter length of thye rectangle: "))
width = int(input("Enter width of thye rectangle: "))

peri = 2*(length+width)
print("Perimeter of the rectangle:",peri,"cm")


''')
