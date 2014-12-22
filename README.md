Wikipedia-Category-Tree
=======================

This is a python program which will generate category tree with the root as given category.

Requirements
============
wikitools

Usage
===========
python categoryTree.py category_name depth output_file

category_name : Category which we are looking into.This category will form the root of Category tree.

depth : This argument decides the depth of the category tree

output_file : The output will generate in this file. The format of output is adjacency representation. For eg: cat:subcat1,subcat2


Example
===========
python categoryTree.py Linear_algebra 1 cat_tree.txt

category_name : Linear_algebra

depth : 1

output_file : cat_tree.txt

Generated Output: cat_tree.txt

Linear_algebra:Theorems in linear algeb,nvex geom,Determinants,Invariant subspaces,Linear operators,Matrices,Matrix th,Multilinear algeb,Numerical linear algeb,Singular value decomposition,Spectral th,Super linear algeb,Topological vector spaces,Vector spaces,Vectors,Linear algebra stubs

Linear operators:Bilinear operators,Generalizations of the derivativ,Integral transforms,Linear operators in calculus,Matrices,Transforms,Unitary operators

Matrices:Random matrices,Sparse matrices

Topological vector spaces:Fréchet spaces,Normed spaces,Sobolev spaces

Vector spaces:Function spaces,Metric linear spaces

Vectors:Topological vector spaces,Vector calculus
