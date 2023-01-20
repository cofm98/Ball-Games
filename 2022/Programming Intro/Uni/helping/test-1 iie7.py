class ExampleClass:
    myNameIs = "Cat Man"
    iLikeCats = False
    def check (character, likesCats : bool):
        character.iLikeCats = likesCats

character_1 = ExampleClass()
print("Do they like cats? " + str(character_1.iLikeCats))
character_1.check(True)
print("Do they like cats now? " + str(character_1.iLikeCats))
