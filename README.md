# Thesaurus-Overlap
Pull overlapping synonyms between multiple word.

This is a very basic program I wrote to get familiar with APIs and to create a tool I wished existed while prepping a slide deck for a client. I had two concepts in mind, and I was fairly certain there was a single word that meant both. In that spirit, this program uses the Merriam Webster API to read through all the synonyms of entered words and prints any synonyms which are synonyms of all the entered words. It's definitely a bit coarse in places, but gets the job done. As many words as desired can be entered into the 'words' variable (including one if you just want to use it as a standard thesaurus).

The user key is unique to me from Merriam Webster and limited to 1,000 pulls per day, but I am doubtful that this will draw much attention, so I'll take the risk.

One note: So far, I haven't created a mechanism to limit the synonyms to one meaning of a word that as several meanings (e.g. sanction), but I don't find it troublesome when using this as a writing tool. 
