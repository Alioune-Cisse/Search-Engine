import connectDB


def dfclean():
    df = connectDB.recupdf()
    #Supprimer (' du début
    df = df.replace(
            to_replace=r"^\('+", value=r"",
            regex=True) 
            
    #Supprimer ',) de la fin
    df = df.replace(
            to_replace=r"',\)$",
            value=r"", regex=True)

    # Supprimer (" du début
    df = df.replace(
        to_replace=r'^\("+', value=r"",
        regex=True)

    # Supprimer ",) de la fin
    df = df.replace(
        to_replace=r'",\)$',
        value=r"", regex=True)
    
    #Supprimer (' du début
    df["commentaires"] = df["commentaires"].replace(
            to_replace=r"^\(+", 
            value=r"", regex=True)
            
    #Supprimer ',) de la fin       
    df["commentaires"] = df["commentaires"].replace(
            to_replace=r",\)$", 
            value=r"", regex=True) 
    
     #Supprimer - de la fin       
    df["auteurs"] = df["auteurs"].replace(
            to_replace=r"\s-\s$", 
            value=r"", regex=True)
    
    return df