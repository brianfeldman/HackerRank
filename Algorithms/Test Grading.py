#Test Grading 

def gradingStudents(grades):
    final = []
    for a in range(len(grades)):
        g = grades[a]
        if g < 37:
            final.append(g)
        elif (g % 5 >= 3):
            n = ((g // 5) + 1) * 5
            final.append(n)
        else: 
            final.append(g)
    return(final)