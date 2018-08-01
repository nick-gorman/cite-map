from fuzzywuzzy import fuzz
import itertools


def group_author_lists(author_lists):
    groups = []
    for index1, author_list in enumerate(author_lists):

        if index1 == 0:
            groups.append([author_list])
        elif index1 + 1 == len(author_lists):
                continue

        found_groups = []

        for index2, group in enumerate(groups):
            all_authors_in_group = [authors.split(';') for authors in group]
            all_authors_in_group = [item for sublist in all_authors_in_group for item in sublist]

            if matching_authors(all_authors_in_group, author_lists[index1 + 1].split(';')) > 0:
                found_groups.append(index2)

        if len(found_groups) == 0:
            groups.append([author_lists[index1 + 1]])
        else:
            new_group = []
            for index3 in sorted(found_groups, reverse=True):
                for element in groups[index3]:
                    new_group.append(element)
                del groups[index3]
            new_group.append(author_lists[index1 + 1])
            groups.append(new_group)

    return groups


def matching_authors(list1, list2):
    match_count = 0
    for name1, name2 in itertools.product(list1, list2):
        names1 = name1.split(',')
        last_name_1 = names1[0]
        names2 = name2.split(',')
        last_name_2 = names2[0]
        first_name_1 = names1[-1].strip().split(' ')[0]
        first_name_2 = names2[-1].strip().split(' ')[0]
        temp_distance_last = fuzz.ratio(last_name_1.lower().strip(), last_name_2.lower().strip())
        temp_distance_first = fuzz.ratio(first_name_1.lower().strip(), first_name_2.lower().strip())
        if temp_distance_last > 80 and temp_distance_first > 80:
            match_count += 1
    return match_count
