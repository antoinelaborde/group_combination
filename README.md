# group_combination
A mini-package to find the best group combination

This package implement algorithms to solve some issues regarding group combination.

## Group division
Let's give an example of application: I want to plot the Gantt graph of X projects that are divided into N business units.
For more convenience I want to plot the projects by business units in multiple subplots. I've already decided that I
want M subplots at the end.
The issue is that the number of projects is very different from one business unit to another so I cannot say each subplot 
will contain 2 or 3 business units.
As a consequence there a lot of combinations to be tested to find a suitable one. The combinatory of this problem is quite high
so I would like to rely on a simple Genetic Algorithm.

### Chromosome definition

A chromosome is defined by a N-dimensional array containing the group assignment.
For example, the chromosome below:
```
c = [1, 1, 2, 3, 2, 4, 4]
```
means that the first two business units are assigned to group 1.

### Chromosome validation

A chromosome is valid iff there is no empty group among the M ones.

### Chromosome evaluation

Ideally, we would like to have the same number of projects in every subplot. To evaluate this,
we calculate the variance of the number of projects by group.
