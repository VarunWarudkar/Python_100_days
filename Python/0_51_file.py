import io
import string
import os

#help_str = help(os)
with open("os.txt",'w') as f:
    f.write("""Python is a versatile and widely-used programming language known for its simplicity and readability. Created by Guido van Rossum and first released in 1991, Python has gained immense popularity over the years and is now considered one of the top programming languages. It offers a wide range of features and capabilities, making it suitable for various domains such as web development, data analysis, machine learning, and scientific computing.

One of the key strengths of Python is its easy-to-understand syntax, which emphasizes code readability. The language's use of indentation and clean structure makes it highly readable, reducing the chances of errors and enhancing collaboration among developers. Python also has a vast standard library that provides numerous pre-built modules and functions, enabling developers to accomplish tasks efficiently without reinventing the wheel.

Python's versatility is reflected in its support for multiple programming paradigms, including procedural, object-oriented, and functional programming. This flexibility allows programmers to choose the most appropriate approach for their specific needs. Additionally, Python's extensive third-party package ecosystem, with tools such as NumPy, Pandas, and TensorFlow, empowers developers to tackle complex tasks and accelerate development.

Python's popularity is further bolstered by its vibrant community. The Python community is known for its inclusivity, supportiveness, and the availability of extensive documentation and online resources. This community-driven aspect ensures that developers can seek help, collaborate on projects, and share knowledge easily.

Moreover, Python's cross-platform compatibility allows it to run seamlessly on various operating systems, including Windows, macOS, and Linux. This portability makes Python an attractive choice for developers working on different platforms.

In conclusion, Python's simplicity, readability, versatility, extensive library support, and thriving community have contributed to its widespread adoption. Its ability to handle diverse programming tasks and its focus on developer productivity make it a language of choice for beginners and experienced programmers alike.""")
    #f.truncate(10)
with open("os.txt",'r') as f:
    data = f.read()
    #print(f.read())

d_words = data.split(" ")
print(len(d_words))

















