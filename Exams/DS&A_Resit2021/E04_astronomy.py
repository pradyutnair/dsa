# Name:
# SNR:

class AstronomicalObject:
    def __init__( self, name ):
        self.name = name
    def __repr__( self ):
        return self.name
        
class Star( AstronomicalObject ):
    pass

# Make sure that a planet is an AstronomicalObject.
class Planet:
    # Create a suitable __init__() method for Planet.
    # The method gets a name, a radius (in km), a distance from the star (in Mkm), and a list of moons.
    def __init__( self, name, radius, distance, moons=[] ):
        pass
    # The following method returns the largest moon belonging to the planet.
    # If the planet has no moons, return None.
    def biggestmoon( self ):
        return None
    # Create a suitable __repr__() method for Planet.
    def __repr__( self ):
        return ""

# Make sure that a moon is an AstronomicalObject.
class Moon:
    # Create a suitable __init__() method for Moon.
    # The method gets a name, and a radius (in km).
    def __init__( self, name, radius ):
        pass
    # Create a suitable __repr__() method for Moon.
    def __repr__( self ):
        return ""

class StarSystem:
    def __init__( self, star, planets=[] ):
        self.star = star
        self.planets = planets
    # planets_by_distance() returns a list of the planets, sorted by distance from the star.
    def planets_by_distance( self ):
        return []
    # moons_by_name() returns a list of all the moons in the system, sorted by name.
    def moons_by_name( self ):
        return []
    def __repr__( self ):
        return "[{},{}]".format( self.star, self.planets )
   
def main():
    sol = Star( "Sol" )
    luna = Moon( "Luna", 1737 )
    phobos = Moon( "Phobos", 11.2667 )
    deimos = Moon( "Deimos", 6.2 )
    charon = Moon( "Charon", 606 )
    nix = Moon( "Nix", 39 )
    hydra = Moon( "Hydra", 40 )
    kerberos = Moon( "Kerberos", 12 )
    styx = Moon( "Styx", 11 )
    earth = Planet( "Earth", 6371, 149.6, [luna] )
    mars = Planet( "Mars", 3389.5, 227.9, [phobos, deimos] )
    mercury = Planet( "Mercury", 2349.7, 57.91 )
    venus = Planet( "Venus", 6051, 108.2 )
    pluto = Planet( "Pluto", 1188.3, 5900, [charon, hydra, kerberos, nix, styx] )
    solsystem = StarSystem( sol, [earth, mars, mercury, pluto, venus] )

    print( mercury )
    print( earth )
    print( pluto )
    print( pluto.biggestmoon() )
    print( earth.biggestmoon() )
    print( venus.biggestmoon() )
    print( solsystem.planets_by_distance() )
    print( solsystem.moons_by_name() )
    
if __name__ == "__main__":
    main()
    
'''
Expected output:

Mercury(2349.7, 57.91, [])
Earth(6371, 149.6, [Luna(1737)])
Pluto(1188.3, 5900, [Charon(606), Hydra(40), Kerberos(12), Nix(39), Styx(11)])
Charon(606)
Luna(1737)
None
[Mercury(2349.7, 57.91, []), Venus(6051, 108.2, []), Earth(6371, 149.6, [Luna(1737)]), Mars(3389.5, 227.9, [Phobos(11.2667), Deimos(6.2)]), Pluto(1188.3, 5900, [Styx(11), Kerberos(12), Nix(39), Hydra(40), Charon(606)])]
[Charon(606), Deimos(6.2), Hydra(40), Kerberos(12), Luna(1737), Nix(39), Phobos(11.2667), Styx(11)]
'''