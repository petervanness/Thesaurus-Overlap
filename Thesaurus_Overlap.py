import json
import urllib.request, urllib.parse, urllib.error

api_key = ''

# ___________________________________________________________________
# Enter words of interest  ('smelly offensive') to find any overlapping synonyms
words = 'beginning'

## input function if desirable
# words = input("Enter words of interest to find any overlapping synonyms ('aa bb cc'):")

# ___________________________________________________________________
words = words.split()

syn_dict: dict[str,list] = {}
missing_words = []

for word in words:
    url = f'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={api_key}'
    response = urllib.request.urlopen(url)
    data = json.load(response)
    if isinstance(data[0], dict):
        for definition in data:
            for syn_group in definition['meta']['syns']:
                if word in syn_dict.keys():
                    syn_dict[word] = list(set(syn_dict[word] + syn_group))
                else:
                    syn_dict[word] = syn_group
    else:
        syn_dict[word] = []
        print(f'{word} not found.')
        missing_words.append(word)

for word in words:
    if (word not in syn_dict.keys() or syn_dict[word] == [] or syn_dict[word] == '') and word not in missing_words:
        print(f'Synonyms for {word} not found.')


res = [sorted(i) for i in syn_dict.values()]
overlap = list(set.intersection(*map(set,res)))
overlap.sort()

if len(overlap) == 0:
    print('These words have no overlapping synonyms.')
else:
    for i in overlap:
        if i not in words:
            print(i)
