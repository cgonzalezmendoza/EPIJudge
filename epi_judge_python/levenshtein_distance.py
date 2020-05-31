from test_framework import generic_test


def levenshtein_distance(word1, word2):
    matrix = [[-1] * len(word1) for _ in word2]

    def recursive_dp(i, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        if matrix[i][j] == -1:
            if word1[j] == word2[i]:
                return recursive_dp(i - 1, j - 1)
            else:
                matrix[i][j] = min(recursive_dp(i - 1, j - 1), recursive_dp(i - 1, j), recursive_dp(i, j - 1)) + 1

        return matrix[i][j]

    return recursive_dp(len(word2) - 1, len(word1) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
