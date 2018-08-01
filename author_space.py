from fuzzywuzzy import fuzz
import itertools


def group_author_lists(author_lists):
    groups = []
    for index, author_list in enumerate(author_lists):

        if index == 0:
            groups.append([author_list])
        else:
            if author_list in [item for sublist in groups for item in sublist]:
                continue

        all_authors_in_group = [authors.split(';') for authors in groups[-1]]

        if matching_authors(all_authors_in_group, author_list[index + 1]) > 0:
            groups[-1].append(author_list[index + 1])
        else:
            groups.append([author_list])
    return groups


def matching_authors(list1, list2):
    match_count = 0
    for name1, name2 in itertools.product(list1, list2):
        temp_distance = fuzz.ratio(name1, name2)
        if temp_distance > 80:
            match_count += 1
    return match_count
