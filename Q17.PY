
def most_popular(sales):
    freq = {}

    # Count the frequency of each product ID
    for i in sales:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    # Initially assume the first element is the answer
    ans = sales[0]

    # Find the element with maximum frequency
    for i in freq:
        if freq[i] > freq[ans]:
            ans = i
        elif freq[i] == freq[ans] and i < ans:
            ans = i

    return ans


sales = list(map(int, input("Enter the sales: ").split()))

print("Most popular item:", most_popular(sales))
