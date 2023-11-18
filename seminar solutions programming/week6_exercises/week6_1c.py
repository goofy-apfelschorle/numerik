import matplotlib.pyplot as plt

def generate_F(b, t, e_min, e_max):

    F = []

    for e in range(e_min, e_max+1):
        f = []
        for m in range(1, b**t):
            f.append(m*(b**(e-t)))
        F.append(f)
    return F

def generate_normal_F(b, t, e_min, e_max):

    F = []

    for e in range(e_min, e_max+1):
        f = []
        for m in range(b**(t-1), b**t):
            f.append(m*(b**(e-t)))
        F.append(f)

    return F

def realToF(x, F, normalized=False):



    if not normalized:
        F_flat = [n for f in F for n in f]
        closest = F_flat[0]
        for n in F_flat:
            if abs(n-x) < abs(closest-x):
                closest = n
        return closest, abs((closest-x)/x)


    l = 0
    r = (len(F[0])*len(F))-1
    #print(x, F)
    mid = l+(r-l)//2
    while l<=r:
        mid = l+(r-l)//2
        #print(mid//len(F[0]), mid % len(F[0]), l, r)
        if F[mid//len(F[0])][mid % len(F[0])] == x:
            return F[mid//len(F[0])][mid % len(F[0])], 0

        if F[mid//len(F[0])][mid % len(F[0])] > x:
            r = mid - 1
        else:
            l = mid + 1

    #print(F[mid//len(F[0])][mid % len(F[0])])
    if mid > 0 and abs(F[mid//len(F[0])][mid % len(F[0])]-x)>abs(F[(mid-1)//len(F[0])][(mid-1) % len(F[0])]-x):
            closest=F[(mid-1)//len(F[0])][(mid-1) % len(F[0])]
    else:
        closest=F[mid//len(F[0])][mid % len(F[0])]
    if mid<(len(F[0])*len(F))-1 and abs(closest-x)>abs(F[(mid+1)//len(F[0])][(mid+1) % len(F[0])]-x):
        closest=F[(mid+1)//len(F[0])][(mid+1) % len(F[0])]

    return closest, abs((closest-x)/x)        


if __name__ == "__main__":

    #F = generate_F(2, 2, -1, 9)
    F = generate_normal_F(2, 2, -4, 11)
    for i in range(1, 1001):
        print(realToF(i/7, F, normalized=True))

    # colors = ["orange", "red", "blue", "purple", "green", "cyan"]
    #
    # for i, f in enumerate(F):
    #     plt.scatter(f, range(i*len(f), (i+1)*len(f)), color=colors[i % len(colors)])
    #
    # plt.show()
