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
    p3.question = 'How much leg thrust does Superman need to leap over a tall building with a single bound?'
    p3.pub_date = datetime.datetime.now()
    p3.save()
    
    p3.choice_set.create(choice='4,000lbs', votes=9)
    p3.choice_set.create(choice='6,000lbs', votes=2)
    p3.choice_set.create(choice='8,000lbs', votes=5)
    p3.save()
    
    p4 = Poll()
    p4.question = 'Who is the most realistic superhero?'
    p4.pub_date = datetime.datetime.now()
    p4.save()
    
    p4.choice_set.create(choice='Batman', votes=9)
    p4.choice_set.create(choice='Green Arrow', votes=2)
    p4.choice_set.create(choice='Kick-Ass', votes=5)
    p4.save()

    p5 = Poll()
    p5.question = 'Who is the fastest superhero?'
    p5.pub_date = datetime.datetime.now()
    p5.save()
    
    p5.choice_set.create(choice='Superman', votes=2)
    p5.choice_set.create(choice='Flash', votes=2)
    p5.choice_set.create(choice='Robin', votes=9)
    p5.save()
