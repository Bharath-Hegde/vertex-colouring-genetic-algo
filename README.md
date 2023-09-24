# Genetic Algorithm for the Vertex Colouring Problem

__Vertex colouring problem__: Given a randomly generated undirected graph (V,E) where the edge set E contains edges that are randomly selected from all possible edges in the graph, there are no self-loop edges and |V| = 50, colour each vertex with any of k (=3) colours such that no two adjacent vertices have the same color.

## Table of Contents

- [1-Genetic Algorithm](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#1-genetic-algorithm)
   - [1.1-Performance](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#11-performance)
      - [1.1.1-Performance Over Generations](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#111-performance-over-generations)
      - [1.1.2-Performance with Increasing Edges](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#112-performance-with-increasing-edges)
- [2-Improved Genetic Algorithm](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#2-improved-genetic-algorithm)
   - [2.1-Hyperparameters](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#21-hyperparameters)
      - [2.1.1-Population Size](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#211-population-size)
      - [2.1.2-Number of Generations](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#212-number-of-generations)
      - [2.1.3-Mutation Probability](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#213-mutation-probability)
   - [2.2-Makeup of Next Generation](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#22-makeup-of-next-generation)
      - [2.2.1-Elitism](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#221-elitism)
      - [2.2.2-Culling](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#222-culling)
   - [2.3-Crossover Mechanism](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#23-crossover-mechanism)
      - [2.3.1-k Point Crossover](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#231-k-point-crossover)
      - [2.3.2-Uniform Crossover](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#232-uniform-crossover)
   - [2.4-Random Restarts](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#24-random-restarts)
   - [2.5-Results](https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo#25-results)


## 1-Genetic Algorithm

This section contains the results of the standard genetic algorithm, implemented as
described by Russel and Norvig. Similar to the representation of a state in the 8 queens problem,
an individual in the population here is represented by a 50 dimensional list. Each position in
this list takes values 0, 1 or 2 corresponding to the colours red, green or blue respectively.

### 1.1-Performance

In each case, the algorithm was run over 50 generations with a population size of 100
and a small mutation probability of 0.005. The results are recorded below.

#### 1.1.1-Performance Over Generations

The plot below shows how the fitness values changed over the generations on an average.
For each edge number, the average of best fitness values in each generation, across 20
runs of the algorithm has been plotted.

<p align="center">
  <img width="500" alt="Screenshot 2023-09-24 at 10 41 03 AM" src="https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo/assets/82595435/57d97097-b973-4cf0-b295-79b1ed2321b3">
</p>

<div align="center">
  Figure 1: Average of fitness growth with generations
</div>
<br/>
Here generation ’0’ is the randomly initialized population. We can make the following
observations from the above plot.

- On an average, there is a general trend of increasing fitness with generations.
- The improvement in fitness across generations decreases with increase in edges. This
    is seen with the almost flat graph for 500 edges versus the graph for 100 edges.
- The graphs progressively shift downwards with increasing edges. This is because
    with more number of edges, nodes are adjacent to more nodes and the chances that
    a random initialization makes the node fit decreases.

#### 1.1.2-Performance with Increasing Edges

For each of the edge numbers 100, 200, 300, 400 and 500 the algorithm was run 20
times (using a randomly generated graph each time) and the average of the fitness values
obtained in each run has been plotted below. As expected, the fitness obtained drops
with the increase in number of edges, since the complexity of the graph increases.

<p align="center">
  <img width="500" alt="Screenshot 2023-09-24 at 11 00 19 AM" src="https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo/assets/82595435/82c1b703-af68-454d-8e4f-a3018c157cdf">
</p>
<div align="center">
  Figure 2: Variation of average output fitness with edges
</div>

## 2-Improved Genetic Algorithm

### 2.1-Hyperparameters

In the genetic algorithm implementation, there are variables such as population size, number of generations
across which the algorithm is run and the probability of mutation of a child graph’s node
colour, that may be changed. This section discusses the effect of these parameters on
the fitness values. In each case where fitness values have been plotted, they have been
averaged over 20 runs of the algorithm, keeping all parameters other than the one in
question, same.

#### 2.1.1-Population Size

There is significant improvement in performance with increasing population when the
population is low (10-100 individuals). However the graph saturates at larger populations
(100-200). This observation is helpful since larger populations took significantly more
time to run than smaller ones. Increasing population beyond the middle range will
demand more computational time while offering little boost in fitness.

<p align="center">
  <img width="448" alt="Screenshot 2023-09-24 at 11 03 34 AM" src="https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo/assets/82595435/08a559c1-02ed-4ca3-95b2-125e5bf16cd3">
</p>
<div align="center">
  Figure 3: Variation of average output fitness with population size
</div>

#### 2.1.2-Number of Generations

Similar to population size, performance improves with more generations and saturates
for higher number of generations.

<p align="center">
  <img width="509" alt="Screenshot 2023-09-24 at 11 05 27 AM" src="https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo/assets/82595435/033a2f10-2916-40b0-9dbb-1599f6f305b6">
</p>
<div align="center">
  Figure 4: Variation of average output fitness with number of generations
</div>
<br/>
To examine the saturation more closely, consider the iteration when the best fitness
was obtained for 500 generations. Plotted below is the growth of fitness for this iteration.
Initially, since there is higher amount of randomness in the population, large jumps are
made in fitness. However, with increase in generations the diversity decreases and the
population often gets stuck on a fitness (Eg. generations 200 to 300) until some successful
mutations persist and help in jumping out of that fitness.  
<br/><br/>
<p align="center">
  <img width="509" alt="Screenshot 2023-09-24 at 11 06 16 AM" src="https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo/assets/82595435/c3059484-a6b8-48d9-a984-464b4de27268">
</p>
<div align="center">
  Figure 5: Variation of fitness of best individual in population over 500 generations
</div>

#### 2.1.3-Mutation Probability

Increasing the mutation probability beyond 0.1 had negative effects on the fitness. However, below 0.1 
no correlation was observed.

### 2.2-Makeup of Next Generation

In both of the following methods, elitism and culling, the population is kept constant
after each generation so that the effect of the method themselves are isolated.

#### 2.2.1-Elitism

In the original implementation, it is possible that the fitness values may decrease with
generations. Since this is not desirable and we would like to retain the properties that
make the previous generations fit, I have implemented elitism. Given the elitism rate,
(population×elitism rate) parents are directly sent to the next generation, and only
the remaining slots are populated with children. This way the it is guarenteed that our
fitness doesn’t decline.

<p align="center">
  <img width="509" alt="Screenshot 2023-09-24 at 11 07 08 AM" src="https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo/assets/82595435/a5992fdf-3db3-4ad3-9155-353d760824b1">
</p>
<div align="center">
  Figure 6: Variation of average output fitness with elitism rate
</div>
<br/>
As seen from the graph there is a clear improvement from no elitism to use of just 2%
elitism. However with further increase, there is not much improvement and fitness even
starts to decrease around 5%. The reproduce process increases diversity in the population
while the elitism process decreases it. The decrease in fitness can thus be explained by
the loss of diversity due to lesser children being produced by recombination, which is an
important component of the genetic algorithm.

#### 2.2.2-Culling

Given the culling rate, (population×culling rate) parents are discarded, and only the
remaining parents are allowed to reproduce. This ensures that only the well performing
individuals pass on their information to the next generation.
As seen from the plot below, high rates of culling prove to be useful with increase in
fitness even upto 50% culling. But after this point the improvement falters, again due
to over-culling resulting in the loss of diversity, provided by the decently well performing
individuals.

<p align="center">
  <img width="509" alt="Screenshot 2023-09-24 at 11 07 57 AM" src="https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo/assets/82595435/dba99623-57dd-43dd-9d8c-fc7292212a00">
</p>
<div align="center">
  Figure 7: Variation of average output fitness with culling rate
</div>

### 2.3-Crossover Mechanism

#### 2.3.1-k Point Crossover

Instead of choosing 1 pivot across which crossover is done for reproduction, k points
can be chosen across which the childs are interleaved. This helps in greater mixing of
information between parents. In the case that k = 1, it is same as the original reproduce
method with a single crossover. However, as observed in the plot below, there seems to be no improvement from increasing the
number of crossovers in the algorithm.

<p align="center">
  <img width="450" alt="Screenshot 2023-09-24 at 11 08 48 AM" src="https://github.com/Bharath-Hegde/vertex-colouring-genetic-algo/assets/82595435/6f42d54c-d23d-498b-a450-f6166bc20841">
</p>
<div align="center">
  Figure 8: Variation of average output fitness with number of crossovers
</div>



#### 2.3.2-Uniform Crossover

For each colour of the child, we can uniformly randomly choose a parent to inherit from.
However not much of a effect on results was seen through this again. The implementation
is included in the code as _uniformCrossoverReproduce_ , but not used.

### 2.4-Random Restarts

Since the fitness saturates with large number of generations, we can instead break out
of the current run and restart the algorithm with a fresh population. A _sideways_move_
count is kept for each run, which counts the number of generations for which the fitness
has not improved. If this count reaches 1000, the algorithm stops and starts again.
Finally, the best state across all runs is reported.
This improved the performance in general, since we may have a higher chance of
encountering a fit state by abandoning fruitless searches.

### 2.5-Results

Using the observations of testing, the best results of the code on the 50, 100 and 200 edges
test cases, were obtained as follows.

```
Number of Edges : 50
Best state : [2, 2, 1, 1, 0, 1, 0, 1, 2, 2, 1, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 1, 2, 2, 1, 1, 1, 0, 0, 2, 0, 1, 0, 1, 2, 2, 0, 1, 1, 2, 0, 1, 0, 1, 1, 2]
Fitness Value of Best State : 50
Time taken : 0.031055927276611328 seconds
```

```
Number of Edges : 100
Best state : [1, 2, 2, 0, 2, 2, 1, 2, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 1, 2, 2, 1, 0, 2, 0, 2, 1, 1, 1, 0, 1, 1, 0, 1, 2, 0, 1, 0, 1, 1, 1, 2, 2, 1, 0, 0, 2, 0, 0, 1]
Fitness Value of Best State : 50
Time taken : 9.011797904968262 seconds
```

```
Number of Edges : 200
Best state : [1, 1, 0, 1, 0, 0, 2, 1, 0, 0, 0, 1, 2, 2, 2, 0, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2, 0, 1, 2, 0, 2, 1, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 1, 2, 1, 2, 0, 1, 1, 0]
Fitness Value of Best State : 30
Time taken : 44.00137901306152 seconds
```
