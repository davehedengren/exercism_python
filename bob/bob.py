#
# Skeleton file for the Python "Bob" exercise.
#

def hey(what):
    what = what.strip()
    #He answers 'Whoa, chill out!' if you yell at him.
    if what.isupper():
        return 'Whoa, chill out!' 
    #Bob answers 'Sure.' if you ask him a question.
    if what.endswith('?'): 
        return 'Sure.'
    #He says 'Fine. Be that way!' if you address him without actually saying
    #anything
    if not what:
        return 'Fine. Be that way!'
    #He answers 'Whatever.' to anything else.
    else:
        return 'Whatever.'

