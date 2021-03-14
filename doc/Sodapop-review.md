So the first thing I notice is that you've got attributes in your
UI class. You might be doing things differently than me, but it
seems like the code is set up in a way that you don't need
attributes for that class. There's also no way (that I can see)
to initialize those attributes, since you have to get them from
the user each time they're used. Once again though, our plans for
the code aren't going to be the same, so if it's in your plan,
never mind!
The next thing I saw is that you've got the number of objects 
that can be created from or by another class. I like that you've 
added that, because it makes to easier to see the limits on each
class. That might get tricky with user input dictating things like
how many cards a deck can make, but I do not really understand
UML well enough to actually say this would be a problem.
I also notice that you have an arrow going from your Deck to your
NumberSet class. I didn't think of the fact that a Deck does 
need to access specific numberSets, and I'll have to take 
another look at my plan to see if I need an arrow there as well!
Overall, your diagram reads easily and logically. I think any 
critiques I had were a bit nitpicky; good work!!
