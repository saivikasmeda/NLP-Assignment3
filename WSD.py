
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


nltk.download('wordnet')
nltk.download('stopwords')




class simpleLESKWSD :

    
    def __init__(self):
        self.stopwords = set(stopwords.words('english'))
        
        
        
    def sense_tokenizer(self,sense):
        tokens = set(word_tokenize(sense.definition()))
        for example in sense.examples():
            tokens.union(set(word_tokenize(example)))
        tokens = set(tokens)
        return tokens
    
    
    def computeOverlap(self,signature,context):
        gloss = signature.difference( self.stopwords)
        context1 = context.difference( self.stopwords) 
        return len(gloss.intersection(context1))
        
    
    
    
    def simplified_LESK(self,word,sentence):
        
        max_overlap = 0
        context = set(word_tokenize(sentence))
        word_senses = wordnet.synsets(word)
        best_sense = word_senses[0]
        for sense in word_senses:
            signature = self.sense_tokenizer(sense)
            overlap = self.computeOverlap(signature,context)
            if overlap > max_overlap:
                max_overlap = overlap
                best_sense = sense
        
        return best_sense
            
   
        

words = ["singer","performing","year","festival","after_all","accomplished","songwriter","dancer","style","guru","graced","stage","last","joined","big_sister","historic","headlining","tour"]
sentence = ("The singer will not be performing at this year's festival after all. An accomplished singer, songwriter, dancer, and style guru, she graced the festival’s stage last year when she joined her big sister during her historic, headlining tour.")
lesk = simpleLESKWSD()



for word in words:
    best_sense = lesk.simplified_LESK(word,sentence)
    print("Word: " + word)
    print("best sense" +": " , best_sense)
    print(best_sense.definition())
    print("\n")    




