graph = {
    'L': ['n', 'a'],
    'a': ['b', 'n'],
    'n': ['c'],
    'c': [],
    'b': [],
}



topo = []
visited = set()
def build_topo(v):
    print(f'building topo at {v}.', end=' ')
    if v not in visited:
        print(f'{v} is not already visited.')
        visited.add(v)
        for child in graph[v]:
            build_topo(child)
        topo.append(v)
    else:
        print(f'{v} is already visited; skipping.')

build_topo('L')

print(topo)



'''
why do we need to topological sort?

it's because if we call .backward() on a node that doesn't have its gradient fully calculated, then all previous nodes will have incorrect values.
so we must make sure that IF we call .backward() on a node that all nodes that use its value (e.g. have arrows coming to them from this node) get called first.

So basically never have arrows pointing back. if this were the case, we might call .backward on a node that doesn't have its gradient fully calculated. in fact we would.

gradients always flow backwards along arrows. if we have an arrow that flows backwards, then the gradients will travel forwards along that arrow.




Ok. You have to ask "what is the purpose of _backward()?"
The purpose of _backward() is to set the gradient of the children nodes. it has nothing to do with the current node.
HOWEVER.
in order to properly set the gradient of your children, the one thing you need is a correct value of your own gradient. That's the chain rule.
and if you have an arrow pointing backward, then you know that gradient will flow forward. Meaning that the gradient of the current node will change in the future.
So now is NOT the time to call _backward() on it. Because its gradient is not yet fulfulled.




now why does this topological ordering work?
- it either adds a after calling topo on n (in which case a is properly after n)
- or it calls topo on a first, which then adds n before a again since a depends on n.
'''
