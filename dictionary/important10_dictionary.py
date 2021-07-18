import  json
from difflib import  get_close_matches

def file_value(filename):
    with open(filename) as f:
        a=json.load(f)
    return a

def file_key(filename):
    with open(filename) as f:
        a=json.load(f)
        b=a.keys()
    return b


def close_match(a):
    c=file_key("data.json")
    b=get_close_matches(a,c)
    return b
    


def get_word_1(word):
    word=word.lower()
    with open("data.json") as f:
        a=json.load(f)
        c=a.keys()
        if word in c:
            return word
        elif word.title() in c:
            return word.title()
        elif word.upper() in c:
            return word.upper()
        else:
            return False
    
def dict(word):
    a=get_word_1(word)
    if type(a) is str:
        return a
    elif a==False:
        c=close_match(word.lower())
        return c



def meaning(a):
    d=dict(a)
    b=file_value("data.json")
    c=file_key("data.json")
    if type(d) is str:
        print(f" '{d}' meaning is: {b[d]}")
    elif type(d) is list and len(d)>0:
        print("\nTHERE IS THE MOST POSSIBLE MATCHES OF THIS GIVEN WORD:\n")
        for i in range(len(d)):
            if d[i] in c:
                print(f"{i+1}> '{d[i]}' meaning is:{b[d[i]]}\n")
            else:
                print(f"{i+1}> '{d[i]}' : THIS WORD IS NOT IN OUR DICTIONARY")
    else:
        print(f"\n{a} : THIS WORD IS NOT IN OUR DICTIONARY OR YOU ENTER A MEANINGLESS WORD")
    


a=input("ENTER THE WORD THAT YOU WANT THE MEANING OF IT : ")
b=meaning(a)

