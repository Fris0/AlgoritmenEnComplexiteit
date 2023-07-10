import fileinput


def check_move(pref_choice, current, dp):
    for choices in pref_choice[current]:
        if dp[choices] == 0:
            dp[choices] = current
            pref_choice[current].remove(choices)
            return 1
        else:
            if (check_move(pref_choice, dp[choices], dp) == 1):
                dp[choices] = current
                pref_choice[current].remove(choices)
                return 1
    return 0


def solve(dp, order, pref_choice):
    for student in order:
        if student[1] == 1:
            choice = pref_choice[student[0]]
            dp[choice[0]] = student[0]
            pref_choice[student[0]].remove(choice[0])
        else:
            check_move(pref_choice, student[0], dp)

    dp = list(set(dp))
    if 0 in dp:
        dp.remove(0)
        print(len(dp))
    else:
        print(len(dp))


if __name__ == "__main__":
    stdnt_cnt = 0
    thss_cnt = 0

    for line in fileinput.input():
        line = list(map(int, line.split(" ")))
        stdnt_cnt = line[0]
        thss_cnt = line[1]
        fileinput.close()
        break

    dp = [0 for i in range(thss_cnt + 1)]
    pref_cnt = dict()
    pref_choice = dict()

    for line in fileinput.input():
        pref = list(map(int, line.split(" ")))
        if pref[0] not in pref_cnt:
            pref_cnt[pref[0]] = 1
            pref_choice[pref[0]] = [pref[1]]
        else:
            pref_cnt[pref[0]] += 1
            pref_choice[pref[0]].append(pref[1])

    pref_cnt = list(sorted(pref_cnt.items(), key=lambda x: x[1]))
    solve(dp, pref_cnt, pref_choice)
