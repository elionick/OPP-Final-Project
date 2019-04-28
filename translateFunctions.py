from googletrans import Translator
query = input("Input your english text")
def translate(query):
    translator = Translator()
    trans = (translator.translate(query, dest = 'de'))
    print(trans.text)

if __name__ == '__main__':
    pass
    #translate(query)