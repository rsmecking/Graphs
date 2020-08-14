from room import Room
from player import Player
from world import World
from util import Graph, Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
print("The amount of rooms in this map is ",len(room_graph))
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# Dictionary for referencing opposite paths
opposite_direction = {"n": "s", "s": "n", "e": "w", "w": "e"}


# # Create dictionary similar to "get_neighbors" in graph Class
# get_neighbors = {}
# def bfs(starting_room_id):
#         # create an empty queue and enqueue PATH To the Starting Vertex ID
#         queue = Queue()
#         queue.enqueue([starting_room_id])
#         # create a set to store visited vertices
#         visited = set()
#         path = [] + [starting_room_id]

#         # while the queue is not empty
#         while queue.size() > 0:
#             # dequeue the first PATH
#             path = queue.dequeue()
#             # grab the last vertex from the Path
#             room = path[-1]

#             # check if the vertex has not been visited
#             if room not in visited:
#                 # mark it as visited
#                 visited.add(room)

#                 # then add A Path to its neighbors to the back of the queue
#                 for next_room in self.get_neighbors[room]:
#                     #check if room has been explored "?"
#                     if get_neighbors[room][next_room] is "?":
#                         return path
#                     # make a copy of the path
#                     path_copy = list(path)
#                     # append the neighbor to the back of the path
#                     path_copy.append(next_room)
#                     # enqueue out new path
#                     queue.enqueue(path_copy)

def explore(starting_room, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # create a visited set if one doesn't exist
        if visited is None:
            visited = set()
        # create an empty path if one doesn't exist
        if path is None:
            path = []
        # Add the starting room id to visited set
        visited.add(starting_room.id)
        # append starting room id to the path
        path.append(starting_room.id)

        # Explore rooms and their paths with Room method
        for neighbor_room in starting_room.get_exits():
            # print("-------here-----", neighbor_room)
            # need to store room to decide what to do with it
            room = starting_room.get_room_in_direction(neighbor_room)

            # Checks to see if room hasn't been visited
            if room.id not in visited:
                # recurse 
                new_path = explore(room, visited)
                # If valid path store in path
                if new_path:
                    # Add the the new pathways to the path with the reverse directons
                    reverse_path = [neighbor_room] + new_path + [opposite_direction[neighbor_room]]
                    # print(reverse_path)
                path = path + reverse_path

        return path  


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = explore(player.current_room)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
# print("---------here-------------", player.current_room)
visited_rooms.add(player.current_room)


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
