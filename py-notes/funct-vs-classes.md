Functions:
    Take input arguments
    Do something
    Return a result

Program is organized around how data flows and what you do with it.
Functions are action focused

OOP like Java is about structuring information - variables are part of objects, are part of other objects, then inheritance can apply attributes.... these have classes and are state focused.

Use functions when code is action focused

Use classes when your code is state focused

example: stack overflow survey analysis
def show frequencies
def analyze_frequencies

ACTION FOCUSED - want to do things in a certain order and get them done, then print them out.

pretty short file

if we used classes, would end up with a single big golf class and then functions would be methods within the class
we wouldn't have instance variables because state isn't useful

functional solutions simpler than object oriented solutions
ideal to turn things into pure functions - they work independently and do not modify global state
then it becomes easier to write unit tests
flow - action based approach

in another example:

class transactiontype(strfnum):
    deposits = auto{}
    withdrawal = auto{}

class bankaccount
    def __init__(self, initial_balance: int = ) -> None;

    def withdraw

    def transfer

    def _sufficient_balance

    @property

The reason classes are useful here is that a bank account represents a state, and because we have a class, we can create objects of that class. Bank accounts are state focused - it 'is' a certain thing and should always be that thing.

Object oriented programming works well for real concepts, like a real estate system where there are many instances of one thing.

Classes information is populated as a python object while the program runs
When you create an instance of a class, you're creating an object in memory

Each instance stores its own data in memory.

You use json when you need persistence, so you save info to json when the prog ends or data changes and load when it starts.

For a real application, it's most likely that a database will be used instead of a json.