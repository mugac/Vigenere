from collections import Counter

ct = "vrchxzveworpuaeywzmeqfvpjveitzcowukwzzspbboiycovllsyfuadmadefrcltnomjvtksbnwkcaewvlgnfzpvvftgbzvwhlirridmqxxgbdjhhsfecagmglmatiwifxtokzxqfdcjrspvxtrksywimthtpaylveiqdewiaxwszrywhoczivltblxbyrjhngmgiokhirogmawiatgviidtnveykodqukerrspaihysrmtvxhyoiid"
keyLenght = 7;
maxLen = 10
key = ""
maxLen = 15

frequen_czech = {
    "a":	9.5893,
    "b":	1.7761,
    "c":	2.9991,
    "d":	3.7748,
    "e":	10.9041,
    "f":	0.1751,
    "g":	0.2198,
    "h":	2.4975,
    "i":	6.6861,
    "j":	2.3058,
    "k":	3.5281,
    "l":	5.7208,
    "m":	3.6055,
    "n":	5.9172,
    "o":	8.0300,
    "p":	3.1150,
    "q":	0.0059,
    "r":	4.3968,
    "s":	5.5860,
    "t":	5.3853,
    "u":	3.5790,
    "v":	3.9525,
    "w":	0.0543,
    "x":	0.0359,
    "y":	2.8575,
    "z":	3.3026
}
sorted_freq_czech = sorted(frequen_czech.items(), key=lambda x: x[1], reverse=True)

def get_coincidence_index(text):
    print(text)

def get_key_length(ct, maxLen):
    for i in range(1, len(ct)):
        match = 0
        ctShift = ct[-i:] + ct[:-i]
        #print(ctShift)
        for j in range(len(ct)):
            if ctShift[j] == ct[j]:
                match += 1
        print(i,": ",match)
    # for i in range(1, len(ct)):
    #     ctShift = ct[-i:] + ct[:-i]
    # return ctShift
        
test = get_key_length(ct, maxLen)

Groups = ['' for j in range(keyLenght)]
for i in range(len(ct)):
    Groups[i%keyLenght] += ct[i]

def get_freq(text):
    freq = Counter(text)
    return freq

def relative_freq(group):
    total = len(group)
    freq = get_freq(group)
    rel_freq = {char: (count / total) * 100 for char, count in freq.items()}
    return sorted(rel_freq.items(), key=lambda x: x[1], reverse=True)




for group in Groups:
    freqrel = relative_freq(group)
    # print(freqrel)
    # print()
    # print(sorted_freq_czech)
    # print("-------------------------------------------------")
    

# print()
# print(Groups)


# for i in range(1, len(ct)):
#         match = 0
#         ctShift = ct[-i:] + ct[:-i]
#         #print(ctShift)
#         for j in range(len(ct)):
#             if ctShift[j] == ct[j]:
#                 match += 1
#         print(i,": ",match)