def case_fixer(input_name, output_name):
    """fixes case"""
    ret = ''
    with open(input_name) as file:
        paragraph = file.readlines()
    for line in paragraph:
        ret += ''.join(line.lower().lstrip())
    with open(output_name, 'w') as file:
        file.write(ret)


# setup a file to convert
text = """Hey??
  This is A funny looking text 
    That nEeds converting 
      tO lower cAse"""
f = open('test.txt', 'w')
f.write(text)
f.close()
# test your function
case_fixer('test.txt', 'output.txt')
print(open('output.txt').read())