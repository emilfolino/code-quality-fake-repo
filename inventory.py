"""
All functions from kmom04 that handels the inventory list
"""


def pick(fun_bag, fun_item, position = None):
    """
    The function that adds an item to the "bag", aka the list fun_bag
    """
    if position:
        try:
            if int(position) > len(fun_bag):
                raise IndexError

            fun_bag.insert(int(position), fun_item)
            print(("You picked up {} and put it at index {}")
                   .format(fun_item, position))
            return fun_bag
        except IndexError:
            print(("Error. Index {} doesn't exist!"
                   "How big bag do you think you got!").format(position))
            return fun_bag
    else:
        fun_bag.append(fun_item)
        print("You picked up {}".format(fun_item))
        return fun_bag



def inventory(arg, start = None, stop = None):
    """
    The function that displays the items currently in the "bag" aka fun_bag
    """
    temp_arg = arg
    if len(arg) == 0:
        print(arg)
        print("Bag is empty!")
    else:
        if start and stop:
            temp_arg = temp_arg[int(start):int(stop)]
        print(temp_arg)
        print("The bag contains {} items".format(len(arg)))


def drop(fun_bag, fun_item):
    """
    The drop function to remove items from the "bag" aka the list fun_bag
    """
    try:
        fun_bag.remove(fun_item)
        print("Getting rid of that lousy {}!".format(fun_item))
        return fun_bag
    except ValueError:
        print("Error! You got no {}! You can't drop what you aint got yo!".format(fun_item))
        return fun_bag


def swap(fun_bag, fun_item1, fun_item2):
    """
    Swopping indexes of fun_item1 and fun_item2 items in the list fun_bag
    """
    if fun_item1 == fun_item2:
        print("Error, can't swap identical items")
        return fun_bag
    missing_list = []
    try:
        if fun_item1 not in fun_bag:
            missing_list.append(fun_item1)
        if fun_item2 not in fun_bag:
            missing_list.append(fun_item2)
        if missing_list:
            raise ValueError
        temp_item = fun_item2
        fun_bag[fun_bag.index(fun_item2)] = fun_item1
        fun_bag[fun_bag.index(fun_item1)] = temp_item
        print("Swippetiswippetiswap! {} and {} are swapped!".format(fun_item1, fun_item2))
        return fun_bag

    except ValueError:
        if len(missing_list) == 2:
            print("Error! There's no {} nor {}".format(missing_list[0], missing_list[1]))

        else:
            print("Error! There's no {}".format(missing_list[0]))
            print("You cant swap what you aint got!")
        return fun_bag
