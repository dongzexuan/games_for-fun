import numpy as np
import time
import copy

input_s = [[[8], [0],[0], [0], [0], [0], [0], [0], [0]],
           [[0], [0],[3], [6], [0], [0], [0], [0], [0]],
           [[0], [7],[0], [0], [9], [0], [2], [0], [0]],
           [[0], [5],[0], [0], [0], [7], [0], [0], [0]],
           [[0], [0],[0], [0], [4], [5], [7], [0], [0]],
           [[0], [0],[0], [1], [0], [0], [0], [3], [0]],
           [[0], [0],[1], [0], [0], [0], [0], [6], [8]],
           [[0], [0],[8], [5], [0], [0], [0], [1], [0]],
           [[0], [9],[0], [0], [0], [0], [4], [0], [0]],
           ]

haschange = False

def find_neighbor(i, j):
    squa_i = i//3
    squa_j = j//3
    n = []
    for x in range(3):
        for y in range(3):
            if (squa_i * 3 + x) != i or (squa_j * 3 + y) != j:
                n.append((squa_i * 3 + x, squa_j * 3 + y))
    return n


def get_row_num(i, j):
    r = []
    for item in input_s[i][: j] + input_s[i][j + 1:]:
        if len(item) == 1 and item[0] != 0:
            r.append(item[0])
    return r


def get_row_num2(input_s, i, j):
    lst = input_s[i][: j] + input_s[i][j + 1:]
    return uni2(lst)


def get_col_num2(input_s, i, j):
    lst = []
    for row in input_s[: i] + input_s[i + 1:]:
        lst.append(row[j])
    return uni2(lst)


def get_cube_num2(input_s, i, j):
    lst = []
    ind = find_neighbor(i, j)
    for inde in ind:
        if input_s[inde[0]][inde[1]][0] != 0:
            lst.append(input_s[inde[0]][inde[1]])
    return uni2(lst)


def uni2(lst):
    r = []
    u = {}
    for item in lst:
        item.sort()
        if item[0] != 0:
            if tuple(item) in u:
                u[tuple(item)][0] = u[tuple(item)][0] + 1
            else:
                u[tuple(item)] = [1, len(item)]
    for dic_item in u.items():
        if dic_item[1][1] == 1 or dic_item[1][1] == dic_item[1][0]:
            r += list(dic_item[0])
    return list(set(r))


def get_col_num(i, j):
    c = []
    for row in input_s[: i] + input_s[i + 1:]:
        if len(row[j]) == 1 and row[j][0] != 0:
            c.append(row[j][0])
    return c


def get_col(input_s, j):
    c = [x[j] for x in input_s]
    return c


def get_cube_num(i, j):
    n = find_neighbor(i, j)
    c = []
    for ind in n:
        if len(input_s[ind[0]][ind[1]]) == 1 and input_s[ind[0]][ind[1]][0] != 0:
            c.append(input_s[ind[0]][ind[1]][0])
    return c


def get_cube(input_s, i):
    r = i // 3
    c = i % 3
    cube = []
    for x in range(3):
        cube = cube + (input_s[r * 3 + x][c * 3 : c * 3 +3])
    return cube


def solveler(input_s, i, j):
    uniq_row = get_row_num2(input_s, i, j)
    uniq_col = get_col_num2(input_s, i, j)
    uniq_cube = get_cube_num2(input_s, i, j)
    cand = set(range(1, 10)) - set(uniq_row + uniq_col + uniq_cube)
    if cand != set(input_s[i][j]):
        input_s[i][j] = list(cand)
        if len(list(cand)) == 1:
            return True, input_s, True
        else:
            return True, input_s, False
    else:
        return False, input_s, False


def find_uniq(f):
    e = []
    ind = []
    find = []
    items = []
    already = []
    for i in range(9):
        if len(f[i]) > 1:
            e = e + f[i]
            ind = ind + [(i, j) for j in range(len(f[i]))]
        else:
            already.append(f[i][0])
    # print(ind)
    dset = set(e)
    if len(e) == 0:
        return None, None, False
    for item in dset:
        if e.count(item) == 1 and item not in already:
            find.append(ind[e.index(item)])
            items.append(item)
    if len(items) > 0:
        return find, items, True
    else:
        return None, None, False


def find_guess_cand(input_s):
    curr_min = 9
    for i in range(9):
        for j in range(9):
            if len(input_s[i][j]) > 1 and len(input_s[i][j]) < curr_min:
                curr_min = len(input_s[i][j])
                ind = (i, j)
    return ind


def start(input_s):

    haschange = True
    solved = np.zeros((9, 9))
    trial = 0
    try:

        while haschange:
            trial += 1
            haschange = False
            current = False
            for i in range(9):
                for j in range(9):
                    if input_s[i][j][0] == 0 or len(input_s[i][j]) > 1:
                        current, input_s, issolve = solveler(input_s, i, j)
                        if issolve:
                            solved[i, j] = 1
                    else:
                        solved[i, j] = 1
                    if not haschange:
                        haschange = current
            for u in range(9):
                # print('uniq: ', u)
                current_rows, items, row_change = find_uniq(input_s[u])
                if row_change:
                    for current_row, item in zip(current_rows, items):
                        input_s[u][current_row[0]] = [item]
                        solved[u, [current_row[0]]] = 1
                if not haschange:
                    haschange = row_change

                col = get_col(input_s, u)
                current_cols, items, col_change  = find_uniq(col)
                if col_change:
                    for current_col, item in zip(current_cols, items):
                        input_s[current_col[0]][u] = [item]
                        solved[current_col[0], u] = 1
                if not haschange:
                    haschange = col_change

                cube = get_cube(input_s, u)
                # print(cube)
                current_cubes, items, cube_change  = find_uniq(cube)
                if cube_change:
                    for current_cube, item in zip(current_cubes, items):
                        input_s[(u//3) * 3 + current_cube[0]//3][(u % 3) * 3 + current_cube[0] % 3] = [item]
                        solved[(u//3) * 3 + current_cube[0]//3, (u % 3) * 3 + current_cube[0] % 3] = 1
                if not haschange:
                    haschange = cube_change
            # print('total ', trial )
            status = False
            sol = np.sum(solved)
            prev_res = input_s
            if not haschange and np.sum(solved) != 81:
                input_s_now = copy.deepcopy(input_s)
                guess_cand = find_guess_cand(input_s)
                for guess_num in input_s[guess_cand[0]][guess_cand[1]]:
                    # input_s = copy.copy(input_s_now)
                    print('guess, ', guess_cand, guess_num)
                    input_s[guess_cand[0]][guess_cand[1]] = [guess_num]
                    input_s == input_s_now
                    status, prev_res = start(input_s)
                    if status:
                        break
                    else:
                        # print('failed, ', guess_cand, guess_num, 'try next')
                        input_s == input_s_now
                        input_s = copy.deepcopy(input_s_now)
        if status or np.sum(solved) == 81:
            return True, prev_res
        else:
            return False, None
    except:
        return False, None

tic = time.time()
status, final_res = start(input_s)
end = time.time()
for i in range(9):
    print(final_res[i])
print(end - tic)
