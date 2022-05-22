
"""
/************************************************************************
|       ======================RUBICTRON=====================           |
|                   Oooo                                               |
+============oooO--(   )===============================================+
|           (   )   ) /                                                |
|            \ (   (_/                   .--.......--.                 |
|             \_)                     .-(   |||| ||    )-.             |
|____________________________________/   '--'''''''--''   \____________|
Created By    : Asitha Sandakalum(asitha@synopsys.com) 
Creation Date :
Last Modified :

-----------------------------------------------------------------------*/
"""
import sys 
import re  
import pickle
import nltk
from nltk.corpus import stopwords
import pandas as pd 
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import linear_kernel
from JfinderModelIntf import JfinderModelIntf

class JfinderModel(JfinderModelIntf):

    def __init__(self, model_name):
        try:
            self.setmodels(model_name)
        except:
            print("cannot load models")

    def setmodels(self, model_name):
        self.trained_model = self.load_model(model_name+".pickle")
        self.cleand_coepus = self.load_model(model_name+"_corpus.pickle")
        self.tfidf_model = self.load_model(model_name+"_model.pickle")    
    
    def clean_text(self, text, remove_stopwords=True):
        # Clean the text, with the option to remove stopwords.
     
        # Convert words to lower case and split them
        words = text.lower().split()
    
        # Optionally remove stop words (true by default)
        if remove_stopwords:
            try:
                stops = set(stopwords.words("english"))
            except:
                nltk.download('stopwords')
                stops = set(stopwords.words("english"))
            words = [w for w in words if w not in stops]
     
        cleaned_text = " ".join(words)
    
        # Clean the text
        cleaned_text = re.sub(r"[^A-Za-z0-9(),!.?\'\`]", " ", cleaned_text)
        cleaned_text = re.sub(r"\'s", " 's ", cleaned_text)
        cleaned_text = re.sub(r"\'ve", " 've ", cleaned_text)
        cleaned_text = re.sub(r"n\'t", " 't ", cleaned_text)
        cleaned_text = re.sub(r"\'re", " 're ", cleaned_text)
        cleaned_text = re.sub(r"\'d", " 'd ", cleaned_text)
        cleaned_text = re.sub(r"\'ll", " 'll ", cleaned_text)
        cleaned_text = re.sub(r",", " ", cleaned_text)
        cleaned_text = re.sub(r"\.", " ", cleaned_text)
        cleaned_text = re.sub(r"!", " ", cleaned_text)
        cleaned_text = re.sub(r"\(", " ( ", cleaned_text)
        cleaned_text = re.sub(r"\)", " ) ", cleaned_text)
        cleaned_text = re.sub(r"\?", " ", cleaned_text)
        cleaned_text = re.sub(r"\s{2,}", " ", cleaned_text)
        
        # remove all non-words (make a list)
        words = re.split('\W+', cleaned_text)  
        # words = cleaned_text.split()
     
        # Shorten words to their stems
        stemmer = SnowballStemmer('english')
        stemmed_words = [stemmer.stem(word) for word in words]
     
        cleaned_text = " ".join(stemmed_words)
     
        # Return cleaned text 
        return(cleaned_text)

    def extract_clean_documents_from_corpus(self, corpus):
    # Input: corpus is a list of dictionaries(with all fields and data) 
        # print("Extracting and Cleaning documents...")
        final_corpus = []
        list_of_docs = []
        i = 0
        for ticket_dict in corpus:
            # print("Processing ", ticket_dict['summary'])
            doc_cleaned_text = ''
            document_of_words = (str(ticket_dict['summary'])+" "+str(ticket_dict['description']))
            # document_of_words = (str(ticket_dict['question1']))
            doc_cleaned_text = self.clean_text(document_of_words)
            list_of_docs.append(doc_cleaned_text)
            final_corpus.append({'key': ticket_dict['key'],'summary':ticket_dict['summary'], 'index': i})
            # final_corpus.append({'qid1':ticket_dict['qid1'], 'words':doc_cleaned_text, 'index':i})
            i += 1
        return list_of_docs, final_corpus   

    def train_and_save_model(self, model_name):
        df = pd.read_csv(model_name+'.csv')
        df.dropna(inplace=True)
        corpus = df.to_dict('records')

        new_tfidf_model = TfidfVectorizer()
        
        list_of_docs,training_ticket_corpus = self.extract_clean_documents_from_corpus(corpus)

        tfidf_trainingset = new_tfidf_model.fit_transform(list_of_docs)

        self.save_model(tfidf_trainingset,model_name+".pickle")
        self.save_model(new_tfidf_model,model_name+"_model.pickle")
        self.save_model(training_ticket_corpus,model_name+"_corpus.pickle")

        self.setmodels(model_name)

    def find_top_n_similar_documents(self, n, tfidf_test, tfidf_trainingset, cleaned_training_corpus):
        n += 1
        cosine_similarities = linear_kernel(tfidf_test, tfidf_trainingset).flatten()
        related_docs_indices = cosine_similarities.argsort()[:-n:-1]
        related_jira_ids = []
        for ticket in cleaned_training_corpus:
            if(ticket['index'] in related_docs_indices):
                related_jira_ids.append({'key':ticket['key'],'summary':ticket['summary']})
        return related_docs_indices, related_jira_ids
       
    def getresult(self, num, search_string):
        cleaned_document = self.clean_text(search_string)
        cleaned_document = [cleaned_document]
        tfidf_test = self.tfidf_model.transform(cleaned_document)
        related_indices, related_jiras = self.find_top_n_similar_documents(num, tfidf_test[0:1], self.trained_model, self.cleand_coepus)
        return related_jiras 


if __name__ == "__main__":
    test = JfinderModel("test-data-54000")
    test.train_and_save_model("test-data-54000")
    result = test.getresult(10, sys.argv[1])
    print(result)


