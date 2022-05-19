class MinimumEditDistance:

    def __init__(self, insert_cost=1, delete_cost=1, sub_cost=2):

        self._insert_cost = insert_cost
        self._delete_cost = delete_cost
        self._sub_cost = sub_cost
        self._distance_matrix = []

    def distance(self, source, target):
        n = len(source)
        m = len(target)
        self._distance_matrix = [[0 for x in range(m + 1)] for x in range(n + 1)]

        for i in range(1, n + 1):
            self._distance_matrix[i][0] = i * self._delete_cost

        for j in range(1, m + 1):
            self._distance_matrix[0][j] = j * self._insert_cost

        for j in range(1, m + 1):
            for i in range(1, n + 1):
                if source[i - 1] == target[j - 1]:
                    self._sub_cost = 0
                else:
                    self._sub_cost = 2
                self._distance_matrix[i][j] = min(self._distance_matrix[i - 1][j] + self._delete_cost,
                                                  self._distance_matrix[i][j - 1] + self._insert_cost,
                                                  self._distance_matrix[i - 1][j - 1] + self._sub_cost)

        return self._distance_matrix[i][j]

    def print_matrix(self):
        print(self._distance_matrix)


source_str = input('Enter source string: ')
target_str = input('Enter target string: ')

minimumEditDistance = MinimumEditDistance(1, 1, 2)  # Pass insert, delete and substitution costs (Optional)
distance = minimumEditDistance.distance(target_str, source_str)
print(f' Edit distance from {source_str} to {target_str}  is {distance}')
print('Printing the distance matrix.....')
minimumEditDistance.print_matrix()
