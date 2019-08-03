import os
print (os.getcwd())
lst=os.listdir()
txt_file=[x for x in lst if x.__contains__('.txt')]
print(txt_file)