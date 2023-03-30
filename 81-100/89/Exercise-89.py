adjectives = ['nice','strong', 'cute']
def add_adverb_ending(adjectives, ending):
    return [ word + ending for word in adjectives]

add_adverb_ending(adjectives, 'ly')