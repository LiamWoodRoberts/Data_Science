'''Basic fraud detecter from a hackerrank problem. Notifies user if spending goes above twice the 
median of a specified previous numbers of days. Function takes in daily spending and number of days tracked
and returns the number of notifications a user would recieve.'''

from bisect import insort

def fraud(spend,d):
    notifications = 0
    for i in range(len(spend)-d):
        #Create sorted transaction history on first loop through
        if i == 0:
            history = spend[i:i+d]
            history.sort()

        #Use bisect module to drop and insert values at each iterations
        else:
            drop = bisect(history,spend[i-1])-1
            del history[drop]
            insort(history,spend[i+d-1])

        # Cases for odd and even d values
        if d%2 == 0:
            median = sum(history[int(d/2-1):int(d/2)+1])/2
        else:
            median = history[int(d/2)]

        # Add notification if a transaction goes above 2x the history median
        if spend[i+d] >= 2*median:
            notifications+=1

    return notifications
