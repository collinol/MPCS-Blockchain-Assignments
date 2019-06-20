# Merkle Trees - Lab 3
merkle tree class has two main functions for computing hashes and proving path
hash computations is similar to the technique discussed in class and implemented in the C++ code provided  
 The path proof to return the minimum set is a recursive function that takes a given leaf and 
 searches all other nodes at the same depth, where the depths are stored as the values of a dictionary.
 I calculate the possible double sha combinations of the given leaf and available siblings.
 For instance, in we have leaf L and the hashes at nodes A and B are at the same depth of L, we compute
 the double shas of A+L, L+A, B+L and L+B and see if any of these exist in the above level of the merkle tree.
 if sha(sha(B+L)) is in the above depth, we know that B is required for the proof. We then rerun the proof
 with sha(sha(B+L)) (the parent) as the new starting leaf. 
