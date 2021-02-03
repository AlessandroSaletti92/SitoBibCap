def get_all_values(nested_dictionary):
    for key, value in nested_dictionary.items():
        if isinstance(value,dict):
            get_all_values(value)
        if isinstance(value,list):
            for i in value:
                get_all_values(i)
        else:
            if (value == "") or (value is None):
                nested_dictionary[key] = "Non disponibile"


                

def replaceindict(dict):
    dict['_id'] = 'n.a.'
    res = str(dict).replace("''","'Non disponibile'").replace('None',"'Non disponibile'")
    return eval(res)
