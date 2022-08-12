from data import sparse_matrix_multiplication_data as data
"""
Returns the dimensions of a matrix
"""


def get_dim(matrix):
    return {'rows': len(matrix), 'columns': len(matrix[0])}


"""
Performs sparce matrix multiplication
"""


def sparse_matrix_multiplication(matrix_a, matrix_b):
    dim_a = get_dim(matrix_a)
    dim_b = get_dim(matrix_b)
    # if inners match
    if dim_a['columns'] == dim_b['rows']:
        # define new matrix
        new = [[0 for x in range(dim_b['columns'])] for y in range(dim_a['rows'])]
        for i in range(dim_a['rows']):
            for j in range(dim_b['columns']):
                new[i][j] = sum([matrix_a[i][k] * matrix_b[k][j] for k in range(dim_a['columns'])])
        return new
    # inners dont match, matrix multiplication not possible
    else:
        return [[]]


print(sparse_matrix_multiplication(data['matrix_a'], data['matrix_b']))
