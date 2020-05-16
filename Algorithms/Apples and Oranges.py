#Apples and Oranges
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ah = 0
    oh = 0
    for app in apples:
        if app >= (s - a) and app <= (t - a):
            ah += 1
    for ora in oranges:
        if ora >= -(b - s) and ora <= -(b - t):
            oh += 1
    print(ah)
    print(oh)