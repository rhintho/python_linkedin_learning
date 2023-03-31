# Demo für die Formatierung von Strings
from string import Template

str1 = "Das ist ein '{0}' von '{1}'.".format("String", "Sebastian")
print(str1)

templ = Template("Das ist ein '${obj}' von '${author}'.")
str2 = templ.substitute(obj="String", author="Sebastian")
print(str2)

# Alternative mit Dictionaries
data = {"obj": "String", "author": "Sebastian"}
str3 = templ.substitute(data)
print(str3)
