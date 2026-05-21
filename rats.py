"""Use genetic algorithm to simulate breeding race of super rats."""

import time
import random 
import statistics

# CONSTANTS (weights in grams) 
GOAL = 50000  # Target average weight for the population to reach
NUM_RATS = 20  # Number of adult breeding rats in each generation
INITIAL_MIN_WT = 200  # Minimum initial rat weight
INITIAL_MAX_WT = 600  # Maximum initial rat weight
INITIAL_MODE_WT = 300  # Mode (most frequent) initial rat weight for triangular distribution
MUTATE_ODDS = 0.01  # Probability that a rat's weight mutates during breeding
MUTATE_MIN = 0.5  # Minimum fractional change in weight due to mutation
MUTATE_MAX = 1.2  # Maximum fractional change in weight due to mutation
LITTER_SIZE = 8  # Number of offspring per breeding pair per litter
LITTERS_PER_YEAR = 10  # Number of litters per year (used to estimate years passed)
GENERATION_LIMIT = 500  # Maximum number of generations to simulate

# Ensure even number of rats for pairing (breeding requires pairs)
if NUM_RATS % 2 != 0:
    NUM_RATS += 1

def populate(num_rats, min_wt, max_wt, mode_wt):
    """
    Initialize a population of rats with weights distributed according to a triangular distribution.
    
    Args:
        num_rats (int): Number of rats to generate.
        min_wt (int): Minimum possible weight.
        max_wt (int): Maximum possible weight.
        mode_wt (int): Most likely weight (mode) in the distribution.
        
    Returns:
        list[int]: List of rat weights (integers).
    """
    # random.triangular generates floats; convert to int for weights
    return [int(random.triangular(min_wt, max_wt, mode_wt))
            for i in range(num_rats)]

def fitness(population, goal):
    """
    Calculate the fitness of the population as the ratio of average weight to the goal weight.
    
    Args:
        population (list[int]): List of rat weights.
        goal (int): Target average weight.
        
    Returns:
        float: Fitness score (average weight / goal).
    """
    ave = statistics.mean(population)
    return ave / goal

def select(population, to_retain):
    """
    Select the top breeding rats from the population by weight, split evenly by sex.
    
    Args:
        population (list[int]): List of rat weights.
        to_retain (int): Total number of rats to retain for breeding.
        
    Returns:
        tuple: Two lists of selected males and females (each list length = to_retain/2).
    """
    # Sort population by weight ascending
    sorted_population = sorted(population)
    
    # Number of rats to retain per sex (assuming half males, half females)
    to_retain_by_sex = to_retain // 2
    
    # Split population into females (lighter half) and males (heavier half)
    members_per_sex = len(sorted_population) // 2
    females = sorted_population[:members_per_sex]
    males = sorted_population[members_per_sex:]
    
    # Select the heaviest females and males to retain
    selected_females = females[-to_retain_by_sex:]
    selected_males = males[-to_retain_by_sex:]
    
    return selected_males, selected_females

def breed(males, females, litter_size):
    """
    Generate offspring by randomly combining weights from male and female parents.
    
    Args:
        males (list[int]): List of male rat weights.
        females (list[int]): List of female rat weights.
        litter_size (int): Number of offspring per breeding pair.
        
    Returns:
        list[int]: List of offspring weights.
    """
    # Shuffle parents to randomize pairings
    random.shuffle(males)
    random.shuffle(females)
    
    children = []
    # Pair each male with a female
    for male, female in zip(males, females):
        for _ in range(litter_size):
            # Child weight is a random integer between female and male weights (inclusive)
            child = random.randint(female, male)
            children.append(child)
    return children

def mutate(children, mutate_odds, mutate_min, mutate_max):
    """
    Randomly mutate offspring weights with a given probability and fractional change range.
    
    Args:
        children (list[int]): List of offspring weights.
        mutate_odds (float): Probability of mutation per offspring.
        mutate_min (float): Minimum fractional multiplier for mutation.
        mutate_max (float): Maximum fractional multiplier for mutation.
        
    Returns:
        list[int]: List of mutated offspring weights.
    """
    for index, rat in enumerate(children):
        # If random chance is less than mutate_odds, apply mutation
        if mutate_odds >= random.random():
            # Multiply weight by a random factor between mutate_min and mutate_max, then round
            children[index] = round(rat * random.uniform(mutate_min, mutate_max))
    return children

def main():
    """
    Run the genetic algorithm simulation:
    - Initialize population
    - Iteratively select, breed, and mutate rats
    - Track and print fitness and average weights per generation
    """
    generations = 0

    # Initialize the first generation population
    parents = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT,
                       INITIAL_MODE_WT)
    print("initial population weights = {}".format(parents))
    
    # Calculate initial fitness
    popl_fitness = fitness(parents, GOAL)
    print("initial population fitness = {}".format(popl_fitness))
    print("number to retain = {}".format(NUM_RATS))

    ave_wt = []  # Track average weight per generation

    # Continue until population reaches goal fitness or generation limit reached
    while popl_fitness < 1 and generations < GENERATION_LIMIT:
        # Select top breeding rats
        selected_males, selected_females = select(parents, NUM_RATS)
        
        # Breed offspring from selected parents
        children = breed(selected_males, selected_females, LITTER_SIZE)
        
        # Mutate offspring weights randomly
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        
        # New population includes parents and offspring
        parents = selected_males + selected_females + children
        
        # Calculate new population fitness
        popl_fitness = fitness(parents, GOAL)
        
        print("Generation {} fitness = {:.4f}".format(generations,
                                                      popl_fitness))
        # Record average weight for this generation
        ave_wt.append(int(statistics.mean(parents)))
        
        generations += 1

    # Final output of average weights per generation and summary statistics
    print("average weight per generation = {}".format(ave_wt))
    print("\nnumber of generations = {}".format(generations))
    print("number of years = {}".format(int(generations / LITTERS_PER_YEAR)))

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("\nRuntime for this program was {} seconds.".format(duration))
