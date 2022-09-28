from math import inf
import numpy as np
def jarvs(S):
    minimum_x = inf
    minimum_y = inf
    idx = 0
    for n,i in enumerate(S):
        if minimum_x>=i[0] and minimum_y>i[1]:
            minimum_x = i[0]
            minimum_y = i[1]
            idx = n
    start = idx
    V = []
    V.append(S[idx])
    S.pop(idx)
    p = start
    r = start
    for n,i in enumerate(S):
        for j in S:
            if (j[1] - i[1])*(i[0] - V[0][0]) - (j[0] - i[0])*(i[1] - V[0][1])<0:
                break
        else:
            r = n
            break
    V.append(S[r])
    S.pop(r)
    S.append(V[0])
    while V[0] != V[-1]:
        for n,i in enumerate(S):
            for m,j in enumerate(S):
                if n!=m:
                    direction = (i[1] - V[-1][1])*(j[0] - i[0]) - (j[1] - i[1])*(i[0] - V[-1][0])
                    if direction > 0:
                        break
                    elif direction == 0:
                        y_dir1 = (i[1] - V[-1][1])
                        x_dir1 = (i[0] - V[-1][0])
                        y_dir2 = (j[1] - V[-1][1])
                        x_dir2 = (j[0] - V[-1][0])
                        if np.sqrt(y_dir1**2 + x_dir1**2) > np.sqrt(y_dir2**2 + x_dir2**2):
                            V[-1] = S[n]
                            S.pop(n)
                            break
                        else:
                            S.pop(n)
                            break
            else:
                V.append(S[n])
                S.pop(n)
                break

        # min_dir = inf
        # idx_min = 0
        # for n,i in enumerate(S):
        #     direction = (V[-1][1] - V[-2][1])*(i[0] - V[-1][0]) - (i[1] - V[-1][1])*(V[-1][0] - V[-2][0])
        #     if min_dir < direction < 0:
        #         idx_min = n
        #     elif direction == 0:
        #         y_dir1 = (V[-1][1] - V[-2][1])
        #         x_dir1 = (V[-1][0] - V[-2][0])
        #         y_dir2 = (i[1] - V[-2][1])
        #         x_dir2 = (i[0] - V[-2][0])
        #         if np.sqrt(y_dir1**2 + x_dir1**2) < np.sqrt(y_dir2**2 + x_dir2**2):
        #             V[-1] = S[n]
        #             S.pop(n)
        #             break
        # else:
        #     V.append(S[idx_min])
        #     S.pop(idx_min)

    return V[:-1]


def main():
    lst = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    print(jarvs(lst))
    pass



if __name__ == '__main__':
    main()