import string
import datetime

def is_phrase_in(phrase, text):
        text = text.lower()
        phrase = phrase.lower()
        punctuation = string.punctuation
        for c in text:
            if c in punctuation:
                text = text.replace(c, " ")

        text_words = " ".join(text.split()) + " "
        phrase_words = " ".join(phrase.split()) + " "

        if(phrase_words in text_words):
            print(f"{phrase_words} {text_words}")
            return True
        
        print(f"{phrase_words} {text_words}")
        return False

def main():
    print(datetime.datetime.strptime("12 Oct 2016 23:59:59", "%d %b %Y %H:%M:%S"))

main()