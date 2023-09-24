from Graph_Creator import *
import numpy as np
import random
import matplotlib.pyplot as plt
import time
        
def main():
    gc = Graph_Creator()
    edges = gc.ReadGraphfromCSVfile("./Testcases/200") # Reads the edges of the graph from a given CSV file
    num_colours = 3

    """ Hyper parameters - can be varied"""
    population_size = 150 
    # generations = 100
    mutate_prob = 0.008
    sideways_moves_threshold = 1000 
    elitism_rate = 0.06
    culling_rate = 0.6
    num_crossovers = 2

    start_time = time.time()
    max_fitness = -1
    max_fitness_individual = []
    while(True):
        result, result_fitness, flag = Genetic_Algorithm(createPopulation(population_size, num_colours), edges, mutate_prob, num_colours, elitism_rate, culling_rate, population_size, num_crossovers, sideways_moves_threshold, start_time)
        if ((time.time() - start_time) > 44): break

        if(result_fitness > max_fitness): 
            max_fitness = result_fitness
            max_fitness_individual = result

        if (flag): break

    end_time = time.time()

    print("\n\nRoll No : 2020A7PS0143G")
    print("Number of Edges : ", len(edges))
    print("Best state : ")
    print(max_fitness_individual)
    print("Fitness Value of Best State : ", max_fitness)
    print("Time taken : {} seconds".format(end_time - start_time))

def Genetic_Algorithm(population, edges, mutate_prob, num_colours, elitism_rate, culling_rate, population_size, num_crossovers, sideways_moves_threshold, start_time, fitness_thresh=50):
    generation = 0
    best_fitness_inGen = -1
    best_child_inGen = []
    sideways_moves = 0

    while(True):
        
        prev_best_fitness_inGen = best_fitness_inGen

        next_gen = []
        pop_len = len(population)

        weights = [calculateFitness(population[i], edges) for i in range(pop_len)]
        
        if (culling_rate or elitism_rate):
            sorted_indices = np.flip(np.argsort(weights))

            # Elitism
            next_gen = [population[sorted_indices[i]] for i in range(int(elitism_rate * pop_len))]

            # Culling
            if (culling_rate != 0):
                population = [population[sorted_indices[i]] for i in range(int(pop_len*(1-culling_rate)))]
                weights = [weights[sorted_indices[i]] for i in range(len(population))]
                best_fitness_inGen = weights[0]
                best_child_inGen = population[0]
            else:
                best_fitness_inGen = weights[sorted_indices[0]]
                best_child_inGen = population[sorted_indices[0]]

        for i in range(int((population_size-len(next_gen))/2)):
            parent1, parent2 = selectRandomParents(population, weights)

            child1, child2 = kPointCrossoverReproduce(parent1, parent2, num_crossovers)
            # child1, child2 = uniformCrossoverReproduce(parent1, parent2)
            child1 = mutate(child1, mutate_prob, num_colours)
            child2 = mutate(child2, mutate_prob, num_colours)

            child1_fitness = calculateFitness(child1,edges)
            child2_fitness = calculateFitness(child2,edges)

            if child1_fitness > best_fitness_inGen: 
                best_fitness_inGen = child1_fitness
                best_child_inGen = child1
            if child2_fitness > best_fitness_inGen: 
                best_fitness_inGen = child2_fitness
                best_child_inGen = child2
            if best_fitness_inGen >= fitness_thresh:
                return best_child_inGen, best_fitness_inGen, True

            next_gen.append(child1)
            next_gen.append(child2)

        if ((time.time() - start_time) > 44): break

        population = next_gen
        generation += 1

        if (best_fitness_inGen == prev_best_fitness_inGen): 
            sideways_moves += 1
        else: sideways_moves = 0

        if (sideways_moves > sideways_moves_threshold): break

    return best_child_inGen, best_fitness_inGen, False

def createPopulation(population_size, num_colours, V = 50):
    population = []
    
    for i in range(population_size):
        temp_graph = []
        for j in range(V):
            temp_graph.append(random.randint(0,num_colours-1))
        population.append(temp_graph)
    return population

def calculateFitness(individual, edges):
    trackNodes = [True] * len(individual)
    for edge in edges:
        if(individual[edge[0]] == individual[edge[1]]):
            trackNodes[edge[0]] = trackNodes[edge[1]] = False

    fitness = 0
    for val in trackNodes:
        if (val): fitness += 1

    return fitness

def selectRandomParents(population, prob_distn):
    try:
        return random.choices(population, weights=prob_distn, k = 2)
    except ValueError as e: 
        if str(e) != "Total of weights must be greater than zero":
            raise
        else:
            # every possible parent has 0 fitness, so uniformly randomly select them
            return random.choices(population, k = 2)

def reproduce(parent1, parent2):
    crossover = random.randint(1,len(parent1))
    return parent1[:crossover] + parent2[crossover:], parent2[:crossover] + parent1[crossover:]

def kPointCrossoverReproduce(parent1, parent2, k):
    crossoverPoints = random.sample(range(1,len(parent1)), k)
    crossoverPoints.sort()
    crossoverPoints = [0] + crossoverPoints + [len(parent1)]
    child1 = []
    child2 = []
    
    for i in range(len(crossoverPoints)-1):
        if (i%2 == 0): 
            child1 += parent1[crossoverPoints[i]:crossoverPoints[i+1]]
            child2 += parent2[crossoverPoints[i]:crossoverPoints[i+1]]
        else:
            child1 += parent2[crossoverPoints[i]:crossoverPoints[i+1]]
            child2 += parent1[crossoverPoints[i]:crossoverPoints[i+1]]

    return child1, child2

def uniformCrossoverReproduce(parent1, parent2):
    child1 = []
    child2 = []
    for i in range(len(parent1)):
        if random.randint(1,2) == 1: child1.append(parent1[i])
        else: child1.append(parent2[i])
        
    for i in range(len(parent1)):
        if random.randint(1,2) == 1: child2.append(parent1[i])
        else: child2.append(parent2[i])

    return child1, child2


def mutate(child, prob, num_colours = 3):
    for i in range(len(child)):
        if (random.random() < prob):
            # perform mutation
            child[i] = random.choices(population = [j for j in range(num_colours) if j != child[i]], k = 1)[0]

    return child


if __name__=='__main__':
    main()
