########################################
### similaritymeasures.py
########################################
from math import *
from decimal import Decimal
 
 
class Similarity():
    """ Five similarity measures function """
 
    # euclidean distance
    def euclidean_distance(self, x, y):
        """ return euclidean distance between two lists """
 
        return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))
 
    # manhattan distance
    def manhattan_distance(self, x, y):
        """ return manhattan distance between two lists """
 
        return sum(abs(a - b) for a, b in zip(x, y))
 
    # minkowski distance
    def nth_root(self, value, n_root):
        """ returns the n_root of an value """
 
        root_value = 1 / float(n_root)
        return round(Decimal(value) ** Decimal(root_value), 3)
 
    def minkowski_distance(self, x, y, p_value):
        """ return minkowski distance between two lists """
 
        return self.nth_root(sum(pow(abs(a - b), p_value) for a, b in zip(x, y)),
                             p_value)
 
    # consine similarity
    def square_rooted(self, x):
        """ return 3 rounded square rooted value """
 
        return round(sqrt(sum([a * a for a in x])), 3)
 
    def cosine_similarity(self, x, y):
        """ return cosine similarity between two lists """
 
        numerator = sum(a * b for a, b in zip(x, y))
        denominator = self.square_rooted(x) * self.square_rooted(y)
        return round(numerator / float(denominator), 3)
 
    # jaccard similarity
    def jaccard_similarity(self, x, y):
 
        """ returns the jaccard similarity between two lists """
 
        intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
        union_cardinality = len(set.union(*[set(x), set(y)]))
        return intersection_cardinality / float(union_cardinality)
    
    
########################################
### similarity.py
########################################
from similaritymeasures import Similarity
 
def main():
    """ the main function to create Similarity class instance and get used to it """
 
    measures = Similarity()
 
    print (measures.euclidean_distance([0, 3, 4, 5], [7, 6, 3, -1]))
    print (measures.jaccard_similarity([0, 1, 2, 5, 6], [0, 2, 3, 5, 7, 9]))
 
if __name__ == "__main__":
    main()


출처: https://dbrang.tistory.com/1201 [디비랑[dɪ'bɪraŋ]]

출처: https://dbrang.tistory.com/1201 [디비랑[dɪ'bɪraŋ]]

출처: https://dbrang.tistory.com/1201 [디비랑[dɪ'bɪraŋ]]
