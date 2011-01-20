from guestbook.models import Entry
from indextank_client import ApiClient

import time

# DO NOT USE this account in a production environment because some people may be using it as well.
API_URL='http://:mmIHCmJbxSlHZI@8vfp1.api.indextank.com'
INDEX_NAME='guestbook'

def create_entry_examples():
    api = ApiClient(API_URL)
    index = api.get_index(INDEX_NAME)
    doc_vars = {0:0}

    entry = Entry()
    entry.name = 'leandro'
    entry.email = 'support@indextank.com'
    entry.text = 'Hello world!'
    entry.save()

    index.add_document(entry.id, 
                    {'text': entry.name + ' ' + entry.email + ' ' + entry.text},
                    variables= doc_vars)

    entry = Entry()
    entry.name = 'juan'
    entry.email = 'juan@mail.com'
    entry.text = 'Just passed to say hello'
    entry.save()

    index.add_document(entry.id, 
                    {'text': entry.name + ' ' + entry.email + ' ' + entry.text},
                    variables=doc_vars)
    
    entry = Entry()
    entry.name = 'leandro'
    entry.email = 'support@indextank.com'
    entry.text = 'hey, it\'s me again. HeLLo!!!'
    entry.save()

    index.add_document(entry.id, 
                    {'text': entry.name + ' ' + entry.email + ' ' + entry.text},
                    variables=doc_vars)


def restart_index():
    '''
    if the public index is dirty, you can delete it a create it again
    '''
    api = ApiClient(API_URL)
    index = api.get_index(INDEX_NAME)
    index.delete_index()
    index.create_index()
    while not index.has_started:
        time.sleep(1)
    
    # add a fuction to sort results. 'd[0]' refers to the 0-variable of each document
    index.add_function(1, 'd[0]')
        
    print 'index restarted'
