def tallest_skyscraper(lst):
    for i in range(len(lst)):
        if 1 in lst[i]:
            return (len(lst)) - i
