from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    if final_score == 0:
        return 1
    twod_array = [[0 for i in range(final_score + 1)] for j in range(len(individual_play_scores))]
    for i in range(len(individual_play_scores)):
        twod_array[i][0] = 1
    for i in range(1, final_score + 1):
        twod_array[0][i] = 1 if i % individual_play_scores[0] == 0 else 0
    for index, score in enumerate(individual_play_scores):
        if index == 0:
            continue
        for i in range(1, final_score + 1):
            if i - score >= 0:
                twod_array[index][i] = twod_array[index - 1][i] + twod_array[index][i - score]
            else:
                twod_array[index][i] = twod_array[index - 1][i]

    return twod_array[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
