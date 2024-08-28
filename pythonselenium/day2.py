class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# Create an object of Calculator
calc = Calculator()

# Use the add and subtract methods
print(calc.add(5, 3))       # Output: 8
print(calc.subtract(5, 3))  # Output: 2

name: str = "karthik"
print(name)

browser = ["chrome", "firefox", "safari", "opera"]
#browser[2] = "unkown"
browser[2] = browser[2][::-1]
browser.append("sedat")
ss = browser[2]


print(ss)
print(browser)
print(browser[0:3])