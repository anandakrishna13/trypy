def find(text,key):
    if key in text:
        print('\'{0}\' exists in \'{1}\''.format(key,text))
    else:
        print('key does not exists')


userInputText=input('Enter text : ')
userInputKey= input('Enter search key : ')

find(text=userInputText,key=userInputKey)
