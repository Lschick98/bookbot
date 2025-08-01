
def word_count(path):
    with open(path) as f:
        return len(f.read().split())
    
def char_count(text):
    freq = {}
    text = text.lower()
    for c in set(text):
        freq[c] = text.count(c)
    return freq

def sort_on(num_char):
    def short_sort(items):
        return items["num"]
    sorted_list = []
    for key, value in num_char.items():
        char = key
        num = value
        key_pair = {"char": char, "num": num}
        sorted_list.append(key_pair)
    sorted_list.sort(reverse=True,key=short_sort)
    return sorted_list