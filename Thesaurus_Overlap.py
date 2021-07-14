import json
import urllib.request, urllib.parse, urllib.error

# ___________________________________________________________________
# Enter words of interest  ('smelly offensive') to find any overlapping synonyms
words = 'beginning'

## input function if desirable
# words = input("Enter words of interest to find any overlapping synonyms ('strong true'):")

# ___________________________________________________________________
words = words.split()

syn_dict = {}
#loop to load data for each word
try:
    for word in words:
        url = 'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/'+word+'?key=53d8ba08-53f4-49b4-be6c-cadbab5a3aaf'
        response = urllib.request.urlopen(url)
        data = json.load(response)

        syn_list = []
        #loop to get to (python, not Merriam) dictionary within (python) dictionary
        for datum in data:
            #now at lowest level of (python) dictionary, which is where the synonyms are
            for item in datum['meta']['syns']:
                #looping through all the synonyms listed for the word and adding distinct synonyms to a list
                for syn in item:
                    if syn not in syn_list:
                        syn_list.append(syn)
                syn_list.sort()
        syn_dict.update({word:syn_list})

    # Convert Dictionary to Lists of List
    res = []
    for key, val in syn_dict.items():
        res.append(val)

    #find intersection of lists
    overlap = list(set.intersection(*map(set,res)))
except:
    overlap = []
    syn_list = []
overlap.sort()

if len(overlap) == 0 and len(syn_list) == 0:
    print('Word(s) not found.')
elif len(overlap) == 0:
    print('These words have no overlapping synonyms.')
else:
    for i in overlap:
        print(i)
