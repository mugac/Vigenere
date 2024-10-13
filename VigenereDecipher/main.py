import matplotlib.pyplot as plt
import string

ct = "dejlogmnpnnravvncvtkrsegvbcjkrkejuakwejurvenzfvippvtadpskbtepskjnrcycpjrloebskvpejcbzskbttfsbpscpvvosbbpifdkjmvyijuomblfkabpjvenraeuwolsegvbcjktfsbpscpvvosbffveeibcvoambzlkekbkvoamjcvoequijjczmekfdvkiezcvtkvttrunfttzbklmtlsygpdcfsmfujuamzjvdejlaifplclzlagbrcbmvotejdvnobsakjcbzpibvejskbtjmisfrrmnznskbtejmifzznedbpfmikjcbzmjzskfmvnzrmoqfnpnnrtvfcouoejpukfzzqocjtzdkpdhjurroayoukjhcbvfvskbtlkegseqjdvotifplclzlymscyplezmrkeujnpnzrloepdrsnpnoihaefmafdmpubpmfsomzprslrneeucvtkvsegvbcjkpoamscypllnotjvploeoejuoajvcbdrdejleifplclzlytfsbpjvaedfskszejmypsgpdrsskwidltvsagpdcfebpnfnitlytisfdirmnzdhrqocjtzdkpdhzodzlakprlkabpjvidgoafcymbtvmezodvylzesbfhfsoqwoafieeeotvfcouztztkldizodvysmpbfeyzotvsnvuufecvozlsygbtijkmzsfdeipzmjnluydttruudtvvuavloepmzdkpqaksiumejwekpvvcaelyupsbvpzoyksitftzkeuoaefjsphruszdhjuakvsmftrtnvkvptszniwjnrocejmzqrzkmpwpfsomoaejsajnpnijuakzmrwecnidblpqoujlfcymbtvmzzkitjcyqouqrrieddhleoszvplaqvjvueqqodfrefnzakfvnvsomoojumvaiefjsphruszniroeadhlesznifcymbtvmirsecbtzwnvwymbzvoegseipzuflfwaejbfiakttmjnrqrzdpfqucbczniibnvaadfskoaepskjjvelfvhfeosfnzakrbpfepivmvsedwyjqeczcyaedjvzodvyuvlocpgzdkvttfqyafcvtkfppiptzoebueizmajnpnvptpvmydaedjmdfnjjmvlocpgzdkpndcvzejkvncvtkfteumolioupbvsaujmvaigbtebckoeaceqqetoeatitizvniebsmftv"
keyLenght = 3;
maxLen = 10
key = "bar"
maxLen = 20

frequency_czech = [
    ("a", 9.5893),
    ("b", 1.7761),
    ("c", 2.9991),
    ("d", 3.7748),
    ("e", 10.9041),
    ("f", 0.1751),
    ("g", 0.2198),
    ("h", 2.4975),
    ("i", 6.6861),
    ("j", 2.3058),
    ("k", 3.5281),
    ("l", 5.7208),
    ("m", 3.6055),
    ("n", 5.9172),
    ("o", 8.0300),
    ("p", 3.1150),
    ("q", 0.0059),
    ("r", 4.3968),
    ("s", 5.5860),
    ("t", 5.3853),
    ("u", 3.5790),
    ("v", 3.9525),
    ("w", 0.0543),
    ("x", 0.0359),
    ("y", 2.8575),
    ("z", 3.3026)
]

def get_freq(text):
    alphabet = string.ascii_lowercase
    freq = {char: 0 for char in alphabet}
    for char in text:
        if char in freq:
            freq[char] += 1
    return freq

def get_coincidence_index(text):
    total = len(text)
    freq = get_freq(text)
    index = 0
    for count in freq.values():
        index += (count * (count - 1)) / (total * (total - 1))
    return index

def get_key_length(ct, maxLen):
    for i in range(2, maxLen+1):
        keyCoincidence = 0
        keyGroups = ['' for j in range(i)]
        for j in range(len(ct)):
            keyGroups[j%i] += ct[j]
        for group in keyGroups:
            keyCoincidence += get_coincidence_index(group)
        keyCoincidence /= i
        print(i, ": ", keyCoincidence)

def relative_freq(group):
    total = len(group)
    freq = get_freq(group)
    rel_freq = {char: (count / total) * 100 for char, count in freq.items()}
    return sorted(rel_freq.items(), key=lambda x: x[0], reverse=False)

def decypher_vigenere(ct, key):
    alphabet = string.ascii_lowercase
    key = key.lower()
    keyLenght = len(key)
    ot = ''
    for i in range(len(ct)):
        ot += alphabet[(alphabet.index(ct[i]) - alphabet.index(key[i % keyLenght])) % 26]
    return ot

Groups = ['' for j in range(keyLenght)]
for i in range(len(ct)):
    Groups[i%keyLenght] += ct[i]
    
fig, axs = plt.subplots(2, keyLenght, figsize=(15, 2 * keyLenght))

for idx, group in enumerate(Groups):
    freqrel = relative_freq(group)
    
    axs[0, idx].bar([val[0] for val in freqrel], [val[1] for val in freqrel], align='center')
    axs[0, idx].set_title(f'Pismeno {idx + 1} Relativní frekvence')
    axs[0, idx].set_xlabel('Pismena')
    axs[0, idx].set_ylabel('Frekvence (%)')
    
    axs[1, idx].bar([val[0] for val in frequency_czech], [val[1] for val in frequency_czech], align='center')
    axs[1, idx].set_title('Ceska frekvence')
    axs[1, idx].set_xlabel('Pismena')
    axs[1, idx].set_ylabel('Frekvence (%)')

print(get_key_length(ct, maxLen))

print(decypher_vigenere(ct, key))

plt.tight_layout()
# plt.savefig('test.pdf')
plt.show()