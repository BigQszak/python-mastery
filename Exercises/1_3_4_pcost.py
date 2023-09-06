import sys

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename,'r') as f:
        for line in f:
            temp = 0.0
            stock_list = line.split()
            try:
                temp = int(stock_list[1])*float(stock_list[2])
                total_cost = total_cost + temp

            except ValueError as error:
                print('Could not parse:', repr(line))
                print('Reason:', error)
                print()
            
    return total_cost

if __name__ == '__main__':
    print(portfolio_cost('C:/Users/krzak/OneDrive/Pulpit/Code/python-mastery/Data/portfolio3.dat'))
    #print(portfolio_cost(sys.argv[1]))