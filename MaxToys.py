# Another HackerRank challenge, finding the greatest number of elements which
#stay below a certain sum

def MaxToys(prices,k):
    toys = 0
    budget = [i for i in prices if i < k]
    budget.sort()
    for i in budget:
        k = k - i
        if k > 0:
            toys +=1
        else:
            return toys
    return toys
