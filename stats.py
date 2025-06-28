def count_word(f):
    count = 0
    for i in f.split():
        count += 1
    return count

def number_letters(f):
    dict = {} 
    for i in f:
        letter = i.lower()
        if letter not in dict:
            dict[letter]= 1
        else:
            dict[letter] += 1
    return dict

def sort_on(items):
    return items["num"]

def sorted_dict(d):
    dict= []
    for key,value, in d.items():
        temp ={}
        temp["char"] = key
        temp["num"] = value
        dict.append(temp)
    
    dict.sort(reverse=True, key=sort_on)
    return dict


