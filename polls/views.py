from django.conf import settings
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from polls.models import Choice, Poll
from polls import create_some_polls

from indextank_client import ApiClient

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/poll_detail.html', {
            'object': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))

def search(request):
    query = request.GET['query']
    api = ApiClient(settings.API_URL)
    index = api.get_index(settings.INDEX_NAME)
    search_result = index.search(query)
    
    result_ids = [int(r['docid']) for r in search_result['results']]
    
    object_list = Poll.objects.filter(pk__in=result_ids)
    
    return render_to_response('polls/poll_list.html', {'query': query, 'object_list': object_list})
        
def create_polls(request):
    create_some_polls()
    return HttpResponse('Polls created')
