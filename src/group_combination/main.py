import numpy as np

from src.group_combination.group_count_assignment import GroupCountAssignment

if __name__ == "__main__":
    count_by_group = np.array([27, 19, 12,  9,  8,  7,  6])
    entities = ['BU LOTERIE', 'FONCTION COMMERCIALE', 'BU SPORT', 'DIRECTION CLIENTS',
       'DIRECTION DATA & IA', 'ABU PAIEMENT ET SERVICES', 'FINANCE']
    gca = GroupCountAssignment(
        4,
        count_by_group,
        entities
    )
    random_start = gca.generate_random_chromosome(10000)
    random_start_validated = gca.remove_not_validated(random_start)
    evaluation = gca.evaluate(random_start_validated)
    print(np.sort(evaluation)[:10])
    print(random_start_validated[np.argsort(evaluation)][:5])
    print(gca.get_group_size(random_start_validated[np.argsort(evaluation)][0]))
    print(gca.get_groups(random_start_validated[np.argsort(evaluation)][0]))

