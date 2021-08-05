import re  ## Import re for regular expression
import nltk 
from nltk.corpus import stopwords  ## Import stopwords from nltk.corpus to ignore words like the, he, have..
stop = stopwords.words('english')
from nltk.corpus import wordnet   ## Import wordnet from the NLTK

## define a function which accept file

# def readtxt(filename):
def main():
    f = open('text_cv_v.txt','r')
    contents = f.read()  ## save all the text in a variable 

    ## to fetch the name from cv/resume
    Sentences = nltk.sent_tokenize(contents)  ## to split contents in sentences in list format 
    Tokens = []
    for Sent in Sentences:
        Tokens.append(nltk.word_tokenize(Sent))  ## to split sentences in word in list format

    Words_List = [nltk.pos_tag(Token) for Token in Tokens]  ## mark up the word in text format in particular part of speech 

    Nouns_List = []

    for List in Words_List:
        for Word in List:
            if re.match('[NN.*]', Word[1]):  ## matching noun, singular with the words from Words_List.
                Nouns_List.append(Word[0])  ## if noun found append in Nouns_List[]

    Names = []
    for Nouns in Nouns_List:
        if not wordnet.synsets(Nouns): 
            Names.append(Nouns)

    name1 = Names[0]
    print (f"The name of applicant is:- {name1}")
  
# %% to fetch the email from cv/resume
    #     
    email1 = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", contents)  ## re is used to find same pattern
    email = email1[0]  ## as email is stored in list form, to access only email id
    print (f"The E-mail of {name1} is:- {email}")
# %% to fetch the address from cv/resume
    
    f.seek(0)  ## return cursor to the beginning of the file
    text_list = []  ## store text file line by line 
    line = 1  ## for counting no of lines
    for word in contents:
        if word == '\n':  ## if new line detect 
            line += 1  ## line will increment by 1

    for i in range(line):
        text_list.append(f.readline())  ## readline() method read one line at a time

    for i in range(len(text_list)):
        if "Address" in text_list[i]:  ## to find Address word in list
            print(f"The address of {name1} is:- {text_list[i]}")

# %% to fetch the phone/ mobile number from cv/resume

    mob_number=re.compile(r'\d\d\d\d\d\d\d\d\d\d')  ## Compile a regular expression pattern
    m=mob_number.search(contents)
    print(f"The Mobile number of {name1} is:- {m.group()}")

    f.close()

# readtxt('text_cv_y.txt')
if __name__ == '__main__':
    main()