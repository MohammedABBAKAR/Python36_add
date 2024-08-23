# Adding Numbers
# Create a function that takes two number strings and returns their sum as a string.

# Examples
# add("111", "111") ➞ "222"

# add("10", "80") ➞ "90"

# add("", "20") ➞ "Invalid Operation"
# Notes
# If any input is "" or None, return "Invalid Operation".


def add(n1, n2):
    if n1 in ["", None] or n2 in ["", None]:
        return "Invalid Operation"
    sumn = int(n1)+ int(n2)
    return   str(sumn)
    
print(add("2", "2"))



def add(n1, n2):
    if n1 in ["", None] or n2 in ["", None]:
        return "Invalid Operation"
    
    
    result = int(n1) + int(n2)
    
    return str(result)

print(add("111", "111")) 
print(add("10", "80"))   
print(add("", "20"))      
print(add("15", None))    
