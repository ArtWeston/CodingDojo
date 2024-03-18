from classes.ninja import Ninja, HolyNinja, PoliticalNinja
from classes.pirate import Pirate, GothPirate, PreppyPirate


# Make Ninjas
michelangelo = Ninja("Michelanglo")
the_pope = HolyNinja("The Pope")
uncle_sam= PoliticalNinja("Uncle Sam")

# Make Pirates
jack_sparrow = Pirate("Jack Sparrow")
bruce = PreppyPirate("Bruce")
marilyn_manson = GothPirate("Marilyn Manson")

def print_all_stats(pirates, ninjas):
    for pirate in pirates:
        pirate.show_stats()
    print()
    for ninja in ninjas:
        ninja.show_stats()

print("Round 1\n")
uncle_sam.attack(marilyn_manson)
the_pope.attack(jack_sparrow)
michelangelo.attack(michelangelo)
print()
jack_sparrow.attack(uncle_sam)
bruce.attack(michelangelo)
marilyn_manson.hook_attack(uncle_sam)
print("\nEnd of Round 1 Results:\n")
print_all_stats(Pirate.pirate_roster, Ninja.ninja_roster)

print("Round 2\n")
uncle_sam.establish_prohibition(jack_sparrow)
the_pope.use_ninja_holy_water(uncle_sam)
michelangelo.throw_shuriken(jack_sparrow)
print()
jack_sparrow.drink_rum()
bruce.hook_attack(the_pope)
marilyn_manson.attack(uncle_sam)
print("\nEnd of Round 2 Results:\n")
print_all_stats(Pirate.pirate_roster, Ninja.ninja_roster)


