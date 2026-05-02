def maxScore(ps_values, F):

    variables = {}

    names = ['a', 'b', 'c', 'd', 'e']
    profits = []

    for i,value in enumerate(ps_values):
        profit = value-F
        profits.append({'name' : names[i],
                        'profit' : profit,
                        'value' : 10
                        })
        variables[names[i]] = 0

    profits.sort(key = lambda x: x['profit'], reverse = True)

    current_sum = 0

    for item in profits:
        if item['profit'] >= 0:
            variables[item['name']] = 10
            current_sum += 10

    if current_sum < 20:
        remaining_to_choose = [item for item in profits if item['profit'] < 0]

        for item in remaining_to_choose:
            if current_sum < 20:
                variables[item['name']] = 10
                current_sum += 10
            else:
                break
    
    a = variables['a']
    b = variables['b']
    c = variables['c']
    d = variables['d']
    e = variables['e']


    score = (60-(a+b+c+d+e))*F + a*ps_values[0] + b*ps_values[1] + c*ps_values[2] + d*ps_values[3] + e*ps_values[4]

    return score


def main():
    ps_values = [90, 105, 110, 80, 120]
    F = 100
    
    score = maxScore(ps_values, F)
    print(score)

main()