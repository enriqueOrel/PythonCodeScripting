# -*- coding: utf-8 -*-
"""sample.ipynb


"""

f = open('/content/4363.txt', 'r')

def calculate_frequencies(argument):
  global take_strings
  take_strings = []
  for lines in f:
   take_strings += lines.split()
 
calculate_frequencies(f)

def filtering_words(entrada):
  dicionario = {}
  punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~-’'''
  uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", 
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", 
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", 
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", 
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", ' ','\n','—']
  momentaneo = ' '
  for words in entrada:
      if words not in punctuations:
        if words not in dicionario and words not in uninteresting_words:
          dicionario[words] = 1
        else:
          if words not in uninteresting_words:
            dicionario[words] += 1
  dicionario
  print(dicionario)


filtering_words(take_strings)

a = ' asca, ascaksmakfmkas, askmaskfmkasmf  kama akmsckma '
b  = {}
lista = []

for palabras in a:
  while palabras != ' ':
    b['a'] = palabras

print(b)
