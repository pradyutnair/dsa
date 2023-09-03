# Name: Pradyut Nair
# Student number: 

def is_sorted( itemlist: list ):
    """
    itemlist: any list
    :return: True if the list is sorted in ascending order, False otherwise
    """
    if not itemlist:
        return True
    if len(itemlist) <= 1:
        return True
    for index in range(len(itemlist)-1):
        # print(f"{itemlist[index]} vs {itemlist[index+1]}")
        if itemlist[index] > itemlist[index+1]:
            return False
    return True
    
    
def main():
    print( is_sorted( [1,2,3,4,5,8,12,14,17,23,25,25,27] ) )    # True
    print( is_sorted( [1,2,3,4,5,8,12,11,14,17,23,25,25,27] ) ) # False
    print( is_sorted( [] ) ) # True
    print( is_sorted( [4] ) ) # True
    print( is_sorted( ["apple","banana","cherry","grape","orange"] ) ) # True
    print( is_sorted( ["apple","banana","cherry","orange","grape"] ) ) # False

if __name__ == "__main__":
    main()
