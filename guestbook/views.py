from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.core.exceptions import ObjectDoesNotExist
from guestbook.models import Entry
from guestbook import create_entry_examples

from indextank_client import ApiClient

# DO NOT USE this account in a production environment because some people may be using it as well.
# Go to http://www.indextank.com and sign up for a free account.
API_URL='http://:mmIHCmJbxSlHZI@8vfp1.api.indextank.com'
INDEX_NAME='guestbook'

def list(request):
    entry_list = Entry.objects.all().order_by('-submit_date')[0:10]
    
    return render_to_response('guestbook/entry_list.html', {'entry_list': entry_list})

def create_entries_script(request):
    create_entry_examples()
    return HttpResponse('OK. go to /guestbook and search those entries')

def detail(request, object_id):
    entry_object = get_object_or_404(Entry, pk=object_id)
    entry_object.views += 1
    entry_object.save()

    # create api client and get index
    api = ApiClient(API_URL)
    index = api.get_index(INDEX_NAME)
    
    # variables are accessed by numbers. in this case 'd[0]' in a scoring function will reference 'entry_object.views'
    variables = {0:entry_object.views}
    
    # update the variables of this document
    index.update_variables(entry_object.id, variables)
    
    
    return render_to_response('guestbook/entry_detail.html', {'entry_object': entry_object})
        
def search(request):
    query = request.GET['query']
    # create api client and get index
    api = ApiClient(API_URL)
    index = api.get_index(INDEX_NAME)
    # search by query and sort by views
    search_result = index.search(query, scoring_function=1)
    
    # retrieve results from database
    result_ids = [int(r['docid']) for r in search_result['results']]
    
    entry_list = []
    for result_id in result_ids:
        try:
            entry_object = Entry.objects.get(pk=result_id)
            entry_list.append(entry_object)
        except ObjectDoesNotExist, e:
            pass
    
    return render_to_response('guestbook/entry_list.html', {'query': query, 'entry_list': entry_list})


def submit(request):
    '''
    Create a new entry, save it and index it. Then render the home page
    '''
    new_entry = Entry()
    new_entry.name = request.POST['name']
    new_entry.email = request.POST['email']
    new_entry.text = request.POST['text']
    
    new_entry.save()
    
    api = ApiClient(API_URL)
    index = api.get_index(INDEX_NAME)
    variables = {0:0}
    index.add_document(new_entry.id, 
                    {'text': new_entry.name + ' ' + new_entry.email + ' ' + new_entry.text},
                    variables=variables)
    
    return redirect('guestbook.views.list')
