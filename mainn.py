import ollama

# name = input("Enter your name: ")
# department = input("Enter your department: ")
# print(f"my name is {name} and I'm from {department} department.")
system='''
you explain programming error messages to a 2nd year emgineering student.reply in 3 parts;
1)what it means in plain english
2)why it happens
3)how to fix it
keep it under 120 words.
'''
response = ollama.chat(model='gemma3:1b', messages=[
        {
            'role': 'system',
            'content': system

        },
        {'role': 'user', 'content': 'python error-NameError: name"x" is not defined'}
])
print(response.message.content)