"""Apartment List Intern Coding Challenge
   Completed by Shane Lyons on 3/16/18
"""

from collections import deque
import string

def social_net_size(dictionary, word):
    """Returns the size of a social network in a dictionary for a given
    word. A social network is a graph where each node, s_i, is a string and
    each node's neighbors are the strings in dictionary with edit distance
    1 from s_i.

    Args:
        dictionary (list): a collection of strings (assumed to all be
                           uppercase given problem specs)
        word (string): the word for which we want to find the size of its
                       social network (assumed to be uppercase given specs)
    Returns:
        int: the size of the social network
    """

    def check_new_word(word):
        """A helper function used in social_net_size to check if we have
        created a valid word and that we have already not counted that word
        towards the size of the social network. I chose to make this an
        inner function since I need to mutate visited and stack.

        Args:
            word (string): the word we want to check

        Returns:
            int: 1 if we found a new word in the social network, 0 otherwise
        """
        if word in dictionary and word not in visited:
            visited.add(word)
            # add to stack in case its neighbors are also part of the
            # social network
            stack.append(word)
            return 1
        return 0

    dictionary = set(dictionary)
    # for the trival case that we're looking for a word not in the dictionary
    if word not in dictionary:
        return 0

    MAX_WORD_LEN = len(max(dictionary, key=len))
    visited, stack = set([word]), deque([word])

    social_size = 1

    while stack:
        cur_var = stack.popleft()
        cur_len = len(cur_var)
        for i in range(cur_len):
            # deletion operation - if the length of the word is one we don't
            # need to compute deletions
            if cur_len > 1:
                deletion = cur_var[:i] + cur_var[(i+1):]
                # social_size will increment by one if we find a new word,
                # otherwise check_new_word returns zero
                social_size += check_new_word(deletion)
            for char in string.ascii_uppercase:
                # substitution operation
                substitution = cur_var[:i] + char + cur_var[(i+1):]
                social_size += check_new_word(substitution)
                # insertion operation - if the length of the word is the
                # largest in the dictionary we don't need to insert
                if cur_len < MAX_WORD_LEN:
                    insertion = cur_var[:i] + char + cur_var[i:]
                    social_size += check_new_word(insertion)
                    # also need to account for insertion at the end of a
                    # string which we do at the first pass through
                    if not i:
                        insertion = cur_var + char
                        social_size += check_new_word(insertion)
    return social_size
