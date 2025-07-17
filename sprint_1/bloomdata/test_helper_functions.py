import bloomdata.helper_functions as hf

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

def test_random_phrase():
    assert type(hf.ra .random_phrase(adjectives, nouns)) == str
