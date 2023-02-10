# Given a string that contains a text, print out how many words are there in the string

def count_words(text):
    result_list = text.split(' ')
    print(len(result_list))

    
count_words('I am a text, please, count my words')

