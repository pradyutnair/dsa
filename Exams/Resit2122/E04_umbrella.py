# Name:
# Student Number:

'''
In this exercise, you will build umbrellas from parts, and evaluate their quality.
The exercise file contains a class Material, which has a name, and a boolean which indicates whether 
the material is waterproof. From Material four classes are derived:  Plastic, Wood, Cloth, and Paper.
Two classes in the exercise file need implementation: Part and Umbrella.
The class Part represents a part of an umbrella. For this exercise, the umbrella parts are the shaft, 
the canopy, and (optionally) the end top. A Part object has a name, a size, and a material from which 
it is constructed. These are given to the __init__() method of Part. You have to implement the 
__init__() method, and a suitable __repr__() method for Part. 
The class Umbrella represents a model umbrella. Via the __init__() method it is given a name and a 
list of parts. You have to implement the __init__() method, and a suitable __repr__() method for 
Umbrella.
Finally, you have to implement a method evaluation() for Umbrella. This method evaluates whether the 
umbrella meets all the requirements that it should have. The requirements are: (1) the sum of the 
sizes of the parts of an umbrella should be 5 at most; and (2) all the parts of the umbrella should 
be waterproof. The method returns a string which is the evaluation of the model. There are four 
possible evaluations, namely:
"<name> meets the requirements"        (total size <=5 and all parts are waterproof)
"<name> is too big"                    (total size > 5 and all parts are waterproof)
"<name> is not waterproof"             (total size <= 5 and not all parts are waterproof)
"<name> is too big and not waterproof" (total size > 5 and not all parts are waterproof)
'''

MAXSIZE=5

class Material:
    def __init__( self, name="", waterproof=False ):
        self.name = name
        self.waterproof = waterproof
    def __repr__( self ):
        return f"Material({self.name},{self.waterproof})"

class Plastic( Material ):
    def __init__( self ):
        super().__init__( "plastic", True )

class Wood( Material ):
    def __init__( self ):
        super().__init__( "wood", True )

class Cloth( Material ):
    def __init__( self ):
        super().__init__( "cloth", True )

class Paper( Material ):
    def __init__( self ):
        super().__init__( "paper" )

class Part:
    def __init__( self, name, size, material ):
        pass
    def __repr__( self ):
        return ""

class Umbrella:
    def __init__( self, name, parts ):
        pass
    def evaluation( self ):
        return ""
    def __repr__( self ):
        return ""


def main():
    plastic = Plastic()
    wood = Wood()
    paper = Paper()
    cloth = Cloth()
    
    plastic_shaft = Part( "plastic shaft", 2, plastic )
    wooden_shaft = Part( "wooden shaft", 3, wood )
    paper_canopy = Part( "paper canopy", 2, paper )
    cloth_canopy = Part( "cloth canopy", 3, cloth )
    plastic_canopy = Part( "plastic canopy", 2, plastic )
    end_top = Part( "end top", 1, wood )

    umbrella_1 = Umbrella( "Model 1", [plastic_shaft, cloth_canopy] )
    umbrella_2 = Umbrella( "Model 2", [wooden_shaft, cloth_canopy] )
    umbrella_3 = Umbrella( "Model 3", [plastic_shaft, paper_canopy] )
    umbrella_4 = Umbrella( "Model 4", [wooden_shaft, paper_canopy] )
    umbrella_5 = Umbrella( "Model 5", [plastic_shaft, cloth_canopy, end_top] )
    umbrella_6 = Umbrella( "Model 6", [plastic_shaft, plastic_canopy, end_top] )
    umbrella_7 = Umbrella( "Model 7", [wooden_shaft, paper_canopy, end_top] )
    
    print( umbrella_1.evaluation() ) # Model 1 meets the requirements
    print( umbrella_2.evaluation() ) # Model 2 is too big
    print( umbrella_3.evaluation() ) # Model 3 is not waterproof
    print( umbrella_4.evaluation() ) # Model 4 is not waterproof
    print( umbrella_5.evaluation() ) # Model 5 is too big
    print( umbrella_6.evaluation() ) # Model 6 meets the requirements
    print( umbrella_7.evaluation() ) # Model 7 is too big and not waterproof

if __name__ == "__main__":
    main()
