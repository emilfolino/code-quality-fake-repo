"""
Inventory Functions
"""


def pick(ryggsäcken , item , position = -1):
    """
    Inventory System For Game
    """
    position = int(position)

    if position > len(ryggsäcken):
        print(f"Error! {position} Du kan inte sätta in nåt där")
    elif position == -1:
        ryggsäcken.append(item)
        print(f"{item} lades in i din ryggsäck")
    else:
        ryggsäcken.insert(position, item)
        print(f" {item} har lagt in i din väska på {position} i din väska")

    return ryggsäcken

def inventory(ryggsäcken):
    """
    Checks What Items Are Inside The Ryggsäcken
    """
    print(f"Det finns {len(ryggsäcken)} Saker I ryggsäcken, Dessa är {ryggsäcken}")


def drop(ryggsäcken, item):
    """
    Droppa Item Från Ryggsäcken
    """
    try:
        if item in ryggsäcken:
            ryggsäcken.remove(item)
            print(f"{item} har tagits bort från din väska innehåller {ryggsäcken}")
        else:
            print(f"Error: Listan är tom {item}")
    except ValueError:
        print("Error")   
    return ryggsäcken



def swap(ryggsäcken, item1, item2):
    """
    Byt Plats På Items I Ryggsäcken
    """
    if item1 == item2:
        print("Error")
    else:
        try:
            Item1Place = ryggsäcken.index(item1)
            Item2Place = ryggsäcken.index(item2)

            ryggsäcken[Item1Place], ryggsäcken[Item2Place] = ryggsäcken[Item2Place], ryggsäcken[Item1Place]
            print(f"Du bytte plats på {item1} och {item2}")
        except ValueError:
            print(f"Error {item1} {item2}")
    return ryggsäcken
