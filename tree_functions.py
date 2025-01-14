__author__ = "Lena Collienne, Jordan Kettles"

import os
from ctypes import *

lib = CDLL(f"{os.path.dirname(os.path.realpath(__file__))}/tree.so")


class NODE(Structure):
    _fields_ = [("parent", c_long), ("children", c_long * 2), ("time", c_long)]

    def __init_(self, parent, children, time):
        self.parent = parent
        self.children = children
        self.time = time


class TREE(Structure):
    _fields_ = [("node_array", POINTER(NODE)), ("num_leaves", c_long)]

    def __init_(self, node_array, num_leaves):
        self.node_array = node_array
        self.num_leaves = num_leaves


class TREE_ARRAY(Structure):
    _fields_ = [("trees", POINTER(TREE)), ("num_trees", c_long)]

    def __init_(self, trees, num_trees):
        self.trees = trees
        self.num_trees = num_trees


# from tree.h

get_empty_node = lib.get_empty_node
get_empty_node.argtypes = []
get_empty_node.restype = NODE

get_empty_tree = lib.get_empty_tree
get_empty_tree.argtypes = [c_long]
get_empty_tree.restype = POINTER(TREE)

free_tree = lib.free_tree
free_tree.argtypes = [POINTER(TREE)]

copy_tree = lib.copy_tree
copy_tree.argtypes = [POINTER(TREE), POINTER(TREE)]

get_empty_tree_array = lib.get_empty_tree_array
get_empty_tree_array.argtypes = [c_long, c_long]
get_empty_tree_array.restype = TREE_ARRAY

free_tree_array = lib.free_tree_array
free_tree_array.argtypes = [TREE_ARRAY]

print_tree = lib.print_tree
print_tree.argtypes = [POINTER(TREE)]
print_tree.restype = c_int

same_topology = lib.same_topology
same_topology.argtypes = [POINTER(TREE), POINTER(TREE)]
same_topology.restype = c_int

same_tree = lib.same_tree
same_tree.argtypes = [POINTER(TREE), POINTER(TREE)]
same_tree.restype = c_int

mrca = lib.mrca
mrca.argtypes = [POINTER(TREE), c_long, c_long]
mrca.restype = c_long

# from rnni.h

nni_move = lib.nni_move
nni_move.argtypes = [POINTER(TREE), c_long, c_int]
nni_move.restype = c_int

rank_move = lib.rank_move
rank_move.argtypes = [POINTER(TREE), c_long]
rank_move.restype = c_int

rnni_neighbourhood = lib.rnni_neighbourhood
rnni_neighbourhood.argtypes = [POINTER(TREE)]
rnni_neighbourhood.restype = TREE_ARRAY

rank_neighbourhood = lib.rank_neighbourhood
rank_neighbourhood.argtypes = [POINTER(TREE)]
rank_neighbourhood.restype = TREE_ARRAY

decrease_mrca = lib.decrease_mrca
decrease_mrca.argtypes = [POINTER(TREE), c_long, c_long]
decrease_mrca.restype = c_int

rnni_distance = lib.rnni_distance
rnni_distance.argtypes = [POINTER(TREE), POINTER(TREE)]
rnni_distance.restype = c_long

findpath = lib.findpath
findpath.argtypes = [POINTER(TREE), POINTER(TREE)]
findpath.restype = TREE_ARRAY

first_findpath_move = lib.first_findpath_move
first_findpath_move.argtypes = [POINTER(TREE), POINTER(TREE)]
first_findpath_move.restype = POINTER(TREE)

# from spr.h

spr_move = lib.spr_move
spr_move.argtypes = [POINTER(TREE), c_long, c_long, c_int]
spr_move.restype = c_int

all_spr_neighbourhood = lib.all_spr_neighbourhood
all_spr_neighbourhood.argtypes = [POINTER(TREE), c_int]
all_spr_neighbourhood.restype = TREE_ARRAY

rspr_neighbourhood = lib.rspr_neighbourhood
rspr_neighbourhood.argtypes = [POINTER(TREE)]
rspr_neighbourhood.restype = TREE_ARRAY

hspr_neighbourhood = lib.hspr_neighbourhood
hspr_neighbourhood.argtypes = [POINTER(TREE)]
hspr_neighbourhood.restype = TREE_ARRAY

# from exploring_rnni.h

random_walk_distance = lib.random_walk_distance
random_walk_distance.argtypes = [POINTER(TREE), c_long]
random_walk_distance.restype = c_long

first_iteration_fp = lib.first_iteration_fp
first_iteration_fp.argtypes = [POINTER(TREE_ARRAY), c_long, c_long, c_long]
first_iteration_fp.restype = c_int

sos = lib.sos
sos.argtypes = [POINTER(TREE_ARRAY), POINTER(TREE)]
sos.restype = c_long

mrca_array = lib.mrca_array
mrca_array.argtypes = [POINTER(TREE), POINTER(TREE)]
mrca_array.restype = POINTER(c_long)

mrca_differences = lib.mrca_differences
mrca_differences.argtypes = [POINTER(TREE), POINTER(TREE)]
mrca_differences.restype = c_long

symmetric_cluster_diff = lib.symmetric_cluster_diff
symmetric_cluster_diff.argtypes = [POINTER(TREE), POINTER(TREE), c_long]
symmetric_cluster_diff.restype = c_long
