# Name:
# Student number:

from os.path import isfile

# This function reads in a tab-separated text file with the largest cities in a country 
# and the population of these cities. It returns the sum of the populations of the 
# cities.
def population_count( file ):
    # Write code here

def main():
    print( "{:,d}".format( population_count ( "netherlands.txt" ) ) )    # 3,197,920
    print( "{:,d}".format( population_count ( "germany.txt" ) ) )        # 10,930,155
    print( "{:,d}".format( population_count ( "unitedstates.txt" ) ) )   # 25,486,026
    print( "{:,d}".format( population_count ( "china.txt" ) ) )          # 106,376,083

if __name__ == "__main__":
    main()
