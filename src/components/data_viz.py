import os
import pandas as plt
from wordcloud import WordCloud
import matplotlib.pyplot as plt




class VizStore():
    def __init__(self,df):
        self.df = df
        self.WCplot() # To initialize data word cloud plot


    def WCplot(self): # word cloud plot
        first_col = self.df.columns[0]
        colData = self.df[first_col]
        singletxt = ''
        for mem in colData:
            singletxt += str(mem)
        # Create a WordCloud object
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(singletxt)
        # Plot the word cloud
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig('static/temp/WCplot.png') # saving wordcloud in static/temp/ folder
        #plt.show()






