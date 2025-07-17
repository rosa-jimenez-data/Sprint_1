# import pandas as pd

# df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})

# print(df.head())

import random

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']
         
def random_phrase(adjectives, nouns):
         
    adjective = random.choice(adjectives)
    nouns = random.choice(nouns)

    return adjective + ' ' + nouns

if __name__ == '__main__':
    pass
    #print(random_phrase(adjectives, nouns))