from polls.models import Poll, Choice
import datetime


def create_some_polls():
    p1 = Poll()
    p1.question = 'What do u think about mojito\'s drink?'
    p1.pub_date = datetime.datetime.now()
    p1.save()
    
    p1.choice_set.create(choice='It\'s great', votes=5)
    p1.choice_set.create(choice='The worst drink i\'ve ever had', votes=2)
    p1.choice_set.create(choice='What are u talking about?', votes=0)
    p1.save()
    
    p2 = Poll()
    p2.question = 'What\'s your favorite superhero?'
    p2.pub_date = datetime.datetime.now()
    p2.save()

    p2.choice_set.create(choice='Green lantern', votes=3)
    p2.choice_set.create(choice='Flash', votes=7)
    p2.choice_set.create(choice='Shazam', votes=0)
    p2.save()
    
    p3 = Poll()
    p3.question = 'Which editor do you use to create your website?'
    p3.pub_date = datetime.datetime.now()
    p3.save()
    
    p3.choice_set.create(choice='Dreamweaver', votes=9)
    p3.choice_set.create(choice='Frontpage', votes=2)
    p3.choice_set.create(choice='GoLive', votes=5)
    p3.save()
    
    p4 = Poll()
    p4.question = 'Do you have a flash enabled browser?'
    p4.pub_date = datetime.datetime.now()
    p4.save()
    
    p4.choice_set.create(choice='Yes', votes=9)
    p4.choice_set.create(choice='No', votes=2)
    p4.choice_set.create(choice='Don\'t know', votes=5)
    p4.save()

    p4 = Poll()
    p4.question = 'Do you have a flash enabled browser?'
    p4.pub_date = datetime.datetime.now()
    p4.save()
    
    p4.choice_set.create(choice='Yes', votes=9)
    p4.choice_set.create(choice='No', votes=2)
    p4.choice_set.create(choice='Don\'t know', votes=5)
    p4.save()
