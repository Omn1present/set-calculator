class mySet(list):
    def union(self, other):
        return mySet([i for n,i in enumerate([*self,*other]) if i not in [*self,other][:n]])

    def intersect(self, other):
        return mySet([elem for elem in self if elem in other])


    def difference(self, other):
        return mySet([elem for elem in self if elem not in other]) 

    def __repr__(self):
        return '{' + ', '.join(self) + '}' 

    def __add__(self,other):
        return self.union(other)

    def __sub__(self,other): 
        return self.difference(other)  
    
    def compliment(self):
        return universal-self 
    
    def __eq__(self, other): 
        return sorted(self)==sorted(other) 

def set_arg():
    arg = [i for i in input('Input elements for set, separated by commas (e.g.: 1,2,3,4...)').split(',')] 
    return [i for n, i in enumerate(arg) if i not in arg[:n]] 

def main():
    a=mySet(set_arg()) 
    b=mySet(set_arg()) 
    c=mySet(set_arg())
    global universal 
    universal = a.union(b).union(c)
    print(f'Set A:{a}\nSet B:{b}\nSet C:{c}\nUniversal set:{universal}') 
    print(f'Union of sets A and B={a+b}\nIntersection of sets B and C={b.intersect(c)}\nDifference of sets A and C={a-c}\nCompliment of set A is {a.compliment()}') 

if __name__ == '__main__':
    main()
