def panggil(func):
    return func
def helloworld():
    return "HELLO WORLD"
def main():
    s = panggil(helloworld())
    print(s)
    if _name_ == '_main_':
        main()