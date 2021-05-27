from flask import Flask,render_template,request
from heapq import nlargest
import re

import spacy 
nlp = spacy.load('en_core_web_sm')
from spacy.lang.en.stop_words import STOP_WORDS
#stopwords = list(STOP_WORDS)
from string import punctuation
app = Flask(__name__)

#summarizer
@app.route('/summarizer_spacy',methods=['GET','POST'])
def summariser_spacy(raw_docx):
    raw_text = raw_docx
    docx = nlp(raw_text)
    stopwords = list(STOP_WORDS)
    word_frequencies = {}  
    for word in docx:  
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    sentence_list = [ sentence for sentence in docx.sents ]

    sentence_scores = {}  
    for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 100:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

    summary_sentences = nlargest(15, sentence_scores, key=sentence_scores.get)
    final_sentences = [ w.text for w in summary_sentences ]
    summary = ' '.join(final_sentences)
    return(summary)

#cleaning function
def clean_text(t1):
    t1=re.sub(r'\[[0-9]*\]',' ',t1)               ####removing brackets and extra spaces
    t1=re.sub(r'\s+',' ',t1)
    t2=t1
    t2=re.sub('[^a-zA-Z]',' ',t1)        ####removing special characters and digits
    t2=re.sub(r'\s+',' ',t1)
    return t2

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/text',methods=['GET','POST'])
def text():
    if request.method == 'POST':
        raw_text1 = request.form['text']
        #cleaned_text1 = clean_text(raw_text1)
        summary_scraped = summariser_spacy(raw_text1)
        return render_template('index.html',summary_scraped=summary_scraped)

@app.route('/about')
def about():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)