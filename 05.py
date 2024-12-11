def is_correctly_ordered_update(ordering_rules, page_updates):
    i = 1
    while i < len(page_updates):
        previous = page_updates[i-1]
        current = page_updates[i]
        for must_be_before, must_be_after in ordering_rules:
            if must_be_before == current and must_be_after == previous:
                # print("Broken rule: ", must_be_before, "|", must_be_after)
                return False
        i += 1
    return True


def sum_of_middle_numbers_of_correctly_ordered_updates(ordering_rules, pages_updates):
    # print(pages_updates)
    middle_numbers_sum = 0
    for page_updates in pages_updates:
        # print("Page updates: ", page_updates, "\n", "Ordering rules: ", ordering_rules, "\n", sep='')
        if is_correctly_ordered_update(ordering_rules, page_updates):
            # print("Middle number:", page_updates[len(page_updates)//2])
            middle_numbers_sum += page_updates[len(page_updates)//2]
    return middle_numbers_sum


def fix_incorrectly_ordered_update(ordering_rules, page_updates):
    while True:
        i = 1
        is_correct = True
        while i < len(page_updates):
            previous = page_updates[i-1]
            current = page_updates[i]
            for must_be_before, must_be_after in ordering_rules:
                if must_be_before == current and must_be_after == previous:
                    # print("Broken rule: ", must_be_before, "|", must_be_after)
                    page_updates[i] = previous
                    page_updates[i-1] = current
                    is_correct = False
                    break
            i += 1
        if is_correct:
            return page_updates


def sum_of_middle_numbers_of_correctly_ordered_updates2(ordering_rules, pages_updates):
    # print(pages_updates)
    middle_numbers_sum = 0
    for page_updates in pages_updates:
        # print("Page updates: ", page_updates, "\n", "Ordering rules: ", ordering_rules, "\n", sep='')
        if not is_correctly_ordered_update(ordering_rules, page_updates):
            fixed_page_updates = fix_incorrectly_ordered_update(ordering_rules, page_updates)
            # print("Middle number:", fixed_page_updates[len(fixed_page_updates)//2])
            # print(fixed_page_updates)
            middle_numbers_sum += fixed_page_updates[len(fixed_page_updates)//2]

    return middle_numbers_sum


if __name__ == '__main__':
    ordering_rules, pages_updates = open("./05_input.txt").read().split("\n\n")
    ordering_rules = list(map(
            lambda x: tuple(map(lambda x: int(x), x.split("|"))),
            ordering_rules.strip().split("\n")))
    pages_updates = list(map(
            lambda x: list(map(lambda x: int(x), x.split(","))),
            pages_updates.strip().split("\n")))
    print(sum_of_middle_numbers_of_correctly_ordered_updates(ordering_rules, pages_updates))
    print(sum_of_middle_numbers_of_correctly_ordered_updates2(ordering_rules, pages_updates))
