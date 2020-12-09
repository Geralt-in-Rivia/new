from model.modelB import modelB
from model.modelA import model
from TestTool import test

while True:
    service = input("""Here is our list of services:
    0:Text classification
    1:Return Reverse text
    2:Quit
    Choose a service:""")
    if service == '2':
        print("Thank you for your use!\n")
        exit()
    if service == '0':
        text = input("Enter text:")
        kind = input("Choose a model(A/B):")
        if kind == 'A':
            M = model()
        elif kind == 'B':
            M = modelB()
        print("The classification results:%d\n"%M.predict(text))
        flag = input("Do you want to know the The accuracy rate(Enter y/n):")
        if flag == 'y':
            A={text, M.predict(text)}
            print("The accuracy rate:%d%%\n"%test(A))
        elif flag == 'n':
            print("Thank you for your use!\n")
            continue
    if service == '1':
        text = input("Enter text:")
        print(text[::-1]+'\n')
