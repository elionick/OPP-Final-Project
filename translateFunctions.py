from googletrans import Translator

def translate(query):
    translator = Translator()
    trans = (translator.translate(query, dest = 'de'))
    return(trans.text)

if __name__ == '__main__':
    pass
    #translate(query)