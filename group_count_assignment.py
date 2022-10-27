"""
Problem

We want to build M groups of N entities containing multiple elements n_i (n_i is the number of elements of group n).
In each group, the total number of elements (m_i) is the sum of elements of each entity in the group.
We want the vector m_i to have the lowest possible variance.
"""
from dataclasses import dataclass
from typing import Dict, List

import numpy as np


@dataclass
class GroupCountAssignment:
    """
    :attr nbr_groups: M value
    :attr entities_count: n_i vector
    """
    nbr_groups: int
    entities_count: np.ndarray
    entities: List[str]

    def __post_init__(self):
        self.nbr_entities = len(self.entities_count)
        self.group_count_mapping = {i: c for i, c in enumerate(self.entities_count, 1)}
        self.chromosome_validator = self.get_validator()
        self.chromosome_evaluator = self.get_evaluator()

    def generate_random_chromosome(self, n: int) -> np.ndarray:
        """
        Generate n random chromosomes in an array.
        Chromosomes are stacked by lines in the array.
        :return:
        """
        return np.random.randint(1, self.nbr_groups + 1, size=(n, self.nbr_entities))

    def remove_not_validated(self, chromosomes: np.ndarray) -> np.ndarray:
        """
        Remove chromosome that have not assigned at least one entity to each group
        :param chromosomes: chromosomes stacked in array by row
        :return:
        """
        validated_chromosomes = np.apply_along_axis(self.chromosome_validator, arr=chromosomes, axis=1)
        return chromosomes[validated_chromosomes]

    def evaluate(self, chromosomes: np.ndarray) -> np.ndarray:
        """
        Evaluate the chromosomes
        :param chromosomes: chromosomes stacked in array by row
        :return:
        """
        return np.apply_along_axis(self.chromosome_evaluator, arr=chromosomes, axis=1)

    def get_evaluator(self):
        """
        Evaluate each chromosome
        :return:
        """
        def group_count_std(x: np.ndarray):
            return np.std([self.entities_count[x == i].sum() for i in range(1, self.nbr_groups + 1)])
        return group_count_std

    def get_validator(self):
        """
        Validate the unique count value of x equals the nbr of requested groups
        :return:
        """
        def validate_unique_count(x: np.ndarray):
            return np.unique(x).shape[0] == self.nbr_groups
        return validate_unique_count

    def get_group_size(self, chromosome: np.ndarray) -> Dict[int, int]:
        """
        Return the nbr of projects for each group according to a chromosome
        :param chromosome:
        :return:
        """
        return {i: self.entities_count[chromosome == i].sum() for i in range(1, self.nbr_groups + 1)}

    def get_best_from_n_tries(self, n_tries: int) -> np.ndarray:
        """
        Generate n_tries chromosome and return the best division
        :param n_tries: nbr of chromosomes to try
        :return:
        """
        random_start = self.generate_random_chromosome(n_tries)
        random_start_validated = self.remove_not_validated(random_start)
        evaluation = self.evaluate(random_start_validated)
        return random_start_validated[np.argmin(evaluation)]

    def get_groups(self, chromosome: np.ndarray) -> List[List[str]]:
        """
        Return a list of entity group corresponding to the chromosome
        :param chromosome:
        :return:
        """
        groups = []
        for i in range(1, self.nbr_groups + 1):
            groups.append(list(np.array(self.entities)[chromosome == i]))
        return groups
