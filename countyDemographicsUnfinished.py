import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(high_income_counties(counties))
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(lowest_median_income(counties))
    print(state_with_most_counties(counties))
    print(percent_most_hispanic_or_latino(counties))

def high_income_counties(counties):
    """Return a LIST of the counties with a median household income over $90,000."""
    num_counties=[]
    for data in counties:
        if data['Income']['Median Household Income'] > 90000:
            num_counties.append(data['County'])
    return(num_counties)
    

def lowest_median_income(counties):
    """Return a name of a county with the lowest median household income"""
    tempLowest = counties[0]
    for data in counties:
        if data['Income']['Median Household Income'] < tempLowest['Income']['Median Household Income']:
            tempLowest = data
    return(tempLowest['County'])

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    #Hint: you can use < to compare strings in Python. ex) "cat" < "dog" gives the value True
    first = counties[0]
    for data in counties:
        if data['County'] < first['County']:
            first = data
    return(first['County'])

    
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    highestPercent = counties[0]
    for data in counties:
        if data['Age']['Percent Under 18 Years'] > highestPercent['Age']['Percent Under 18 Years']:
            highestPercent = data
    return(highestPercent['Age']['Percent Under 18 Years'])
    

def county_most_under_18(counties):
    """Return the name a county with the highest percent of under 18 year olds."""
    highestPercent = counties[0]
    for data in counties:
        if data['Age']['Percent Under 18 Years'] > highestPercent['Age']['Percent Under 18 Years']:
            highestPercent = data
    return(highestPercent['County'])
    
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #1. Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    states = {}
    for data in counties:
        state = data['State']
        if state in states:
            states[state]+=1
        else:
            states[state] = 1
    #2. Find the state in the dictionary with the most counties
    mostCounties = 'CA'
    for data in states:
        if states[data] > states[mostCounties]:
            mostCounties = data
    #3. Return the state with the most counties
    return(mostCounties)
    
def percent_most_hispanic_or_latino(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    percentHispanicLatino = counties[0]
    for data in counties:
        if data['Ethnicities']['Hispanic or Latino'] > percentHispanicLatino['Ethnicities']['Hispanic or Latino']:
            percentHispanicLatino = data
    return(percentHispanicLatino['County'])
if __name__ == '__main__':
    main()
