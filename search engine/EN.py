from preprocessing import dfclean
import pandas as pd
import spacy
from spacy import displacy

nlp = spacy.load("fr_core_news_sm")
df = dfclean()

def token(df=df,ind=0):
    docx = nlp(df["contenus"][ind])
    newdf = pd.DataFrame()
    names = ["Text", "Taille", "is_Stop", "is_Alpha", "is_Punct"]
    for token in docx:
        row = [token.text,
               token.shape_,
               token.is_stop,
               token.is_alpha,
               token.is_punct]
        newdf = newdf.append(pd.DataFrame([row], columns=names), ignore_index=True)
    return newdf

def dependances(df=df, ind=0, viz=None):
    docx = nlp(df["contenus"][ind])
    newdf = pd.DataFrame()
    names = ["Text", "Tag", "Dep", "Head Text", "Head Tag"]
    for token in docx:
      row = [token.text, token.tag_, token.dep_, token.head.text, token.head.tag_]
      newdf = newdf.append(pd.DataFrame([row], columns=names), ignore_index=True)
      
    if (viz==True) :
        displacy.serve(docx, style='dep', options={'distance': 60})
        
    return newdf
    
def EN(df=df):
    #Extraction des entités nommées
    list_entities = []
    list_titres = []
    list_types = []
    list_sources = []
    list_content = []
    list_date = []
    for elt in df.contenus:
      doc = nlp(elt)
      entite = []
      nature = []
      for entity in doc.ents:
        #print(entity)
        entite.append((entity.text))
        nature.append((entity.label_))
      #source=df.query('contenus'==elt)['source']
      source=df.loc[df['contenus'] == elt, 'source'].iloc[0]
      contents = df.loc[df['contenus'] == elt, 'titre'].iloc[0]
      dates = df.loc[df['contenus'] == elt, 'datePublication'].iloc[0]
      list_titres.append((elt))
      list_entities.append((entite))
      list_types.append((nature))
      list_sources.append(source)
      list_content.append(contents)
      list_date.append(dates)
      
    df = pd.DataFrame(list(zip(list_content,list_titres, list_entities, list_types, list_sources, list_date)),
                      columns=['Titre','Contenus', 'Entité', "Nature", "Source", "Date Publication"])
    return df