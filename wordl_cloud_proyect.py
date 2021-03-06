# -*- coding: utf-8 -*-
# Final_proyect_coursera


# Here are all the installs and imports you will need for your word cloud script and uploader widget

!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# This is the uploader widget
#def _upload():

    #_upload_widget = fileupload.FileUploadWidget()

   # def _cb(change):
       # global file_contents
       # decoded = io.StringIO(change['owner'].data.decode('utf-8'))
       # filename = change['owner'].filename
      #  print('Uploaded `{}` ({:.2f} kB)'.format(
        #    filename, len(decoded.read()) / 2 **10))
       # file_contents = decoded.getvalue()

    #_upload_widget.observe(_cb, names='data')
    #display(_upload_widget)

# _upload()


file_contents = open('', 'r')




def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ['there','so','one','for','not','in', "the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just",' ','\n','\r']
  
    # LEARNER CODE START HERE
    dicionario =   {}
    
    stringa = ' '
    for lines in file_contents:
        stringa += lines.lower()
    b = stringa.split()
    
    for word in b: 
        if word  not in punctuations and len(word) > 5:
            if word not in dicionario and word not in uninteresting_words:
                dicionario[word] = 1
            else:
                if word not in uninteresting_words  and len(word) > 5:
                    dicionario[word] += 1


    b = {}
    for keys , values in dicionario.items():
       if values > 20:
         b[keys] = values
    
    print(len(b))

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(b)
    return cloud.to_array()


    # Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
file_contents.close()

