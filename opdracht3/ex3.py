"""
Auteur: Mark Jansen
Studentnummer: 13385569
Gemaakt op: 24-11-2022

Samenvatting:
Een implementatie van het type longest sequence algoritme. Met dit algoritme
wordt de langste subsequence berekend.

Gebruik:
- Run de de python code met python3 <pythonfile> <inputfile>
- Het resultaat wordt naar standard output gestuurd.
"""

import fileinput


def find_sequence(answer, sol, ans_idx, sol_idx, sequence_len, dp):
    """
    Look for the longest sequence in the string/sub string given.

    Answer: Char array with the answer to compare to the solution.
    Solution: Char array with the solution.
    ans_idx = int with start value -1.
    sol_idx = int with start value -1.
    sequence_len = int that gives the length of the sol string.
    dp = Matrix to store subproblem answers

    Output: If index is at end of string, then
            return empty, else if value is the same
            , then return current value plus the next in the
             sequence, else longest sub sequence of sub string.
    """
    if ans_idx == sequence_len or sol_idx == sequence_len:
        return ""
    elif dp[ans_idx + 1][sol_idx + 1] != -1:
        return dp[ans_idx + 1][sol_idx + 1]
    elif answer[ans_idx + 1] == sol[sol_idx + 1]:
        dp[ans_idx + 1][sol_idx + 1] = answer[ans_idx + 1] + find_sequence(answer, sol, ans_idx + 1, sol_idx + 1, sequence_len, dp)
        return dp[ans_idx + 1][sol_idx + 1]
    else:
        solution_sub = find_sequence(answer, sol,
                                     ans_idx, sol_idx + 1, sequence_len, dp)
        answer_sub = find_sequence(answer, sol,
                                   ans_idx + 1, sol_idx, sequence_len, dp)
        solution_sub_len = len(solution_sub)
        answer_sub_len = len(answer_sub)

        if solution_sub_len == answer_sub_len:
            if solution_sub < answer_sub:
                dp[ans_idx + 1][sol_idx + 1] = solution_sub
                return dp[ans_idx + 1][sol_idx + 1]
            else:
                dp[ans_idx + 1][sol_idx + 1] = answer_sub
                return dp[ans_idx + 1][sol_idx + 1]
        elif answer_sub_len < solution_sub_len:
            dp[ans_idx + 1][sol_idx + 1] = solution_sub
            return dp[ans_idx + 1][sol_idx + 1]
        else:
            dp[ans_idx + 1][sol_idx + 1] = answer_sub
            return dp[ans_idx + 1][sol_idx + 1]


if __name__ == "__main__":
    """
    Read line(s) from input and call sequence function

    Side-effect: Print result of function to standard output.
    """
    answers = []
    sol = 0

    for line in fileinput.input():
        answer_cnt, sol = line.split(" ")[0], (line.split(" ")[1])
        fileinput.close()
        break

    sol = sol[:len(sol) - 1]
    for line in fileinput.input():
        answer = line[:len(line) - 1]
        dp = [[-1 for i in range(len(sol) + 1)] for j in range(len(sol) + 1)]
        answer = find_sequence(answer, sol, -1, -1, len(sol) - 1, dp)
        print(len(answer), answer)
