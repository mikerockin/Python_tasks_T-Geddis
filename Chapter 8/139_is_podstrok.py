def main():
    mystring = 'mrmikhail_88@gmail.com'
    func = strok(mystring)
def strok(mystring):
    if mystring.endswith('.com'):
        print('True')
    else:
        print(False)
main()