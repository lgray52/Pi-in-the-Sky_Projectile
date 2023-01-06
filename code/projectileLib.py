from statistics import mean, stdev

def findMax(vals):
    meanVal = mean(vals)
    deviation = stdev(vals)

    for i in vals:  # remove noise from data
        zScore = (vals[i]-meanVal)/deviation

        if zScore > 3:  # remove outliers more than 3 standard deviations from mean
            del vals[i]

    maxVal = max(vals)

    return maxVal