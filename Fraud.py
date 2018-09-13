'''Basic fraud detecter from a hackerrank problem, if spending goes above the
median of a specified previous numbers of days sends a notification to user
function returns number of notifications a user would recieve given spending
each day and number of days tracked'''

from bisect import insort

def fraud(spend,d):
    notifications = 0
    for i in range(len(spend)-d):
        if i == 0:
            trail = spend[i:i+d]
            drop = trail.copy()
            trail.sort()
        else:
            trail.remove(drop[0])
            insort(trail,spend[i+d-1])
            drop.remove(drop[0])
            drop.append(spend[i+d-1])

        if d%2 == 0:
            limit = sum(trail[int(d/2-1):int(d/2)+1])
        else:
            limit = 2*trail[int(d/2)]
        if spend[i+d] >= limit:
            notifications+=1
    return notifications

d = 3
spend = [10,20,30,40,50]

fraud(spend,d)
