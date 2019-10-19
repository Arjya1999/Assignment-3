def func():
    try:
        print(5/0)
    except:
        print("Arithmetic Error has occured")
print(func())