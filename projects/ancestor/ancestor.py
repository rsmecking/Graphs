from util import Stack

# def earliest_ancestor(ancestors, starting_node):
#     s = Stack()
#     visited = set()
#     s.push([begin_word])
#     while s.size() > 0:
#         path = s.pop()
#         v = path[-1]

#         if v not in visited:
#             visited.add(v)
#             if v == end_word:
#                 return path

#             for neighbor in get_neighbors(v):
#                 path_copy = list(path)
#                 path_copy.append(neighbor)
#                 s.push(path_copy)

def earliest_ancestor(self, ancestors, starting_node, visited=set()):
    if ancestors in visited:
        return None
    visited.add(ancestors)

    if ancestors == starting_node:
        return [ancestors]

    for v in self.get_neighbors(ancestors):
        subpath = self.earliest_ancestor(v, starting_node, visited=visited)
        if subpath is not None:
            return [ancestors, *subpath]