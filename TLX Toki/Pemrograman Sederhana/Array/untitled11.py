def search(left, right, query, data, response):
    m = (left + right) // 2

    if left > right:
        return response
    elif data[m][:len(query)] == query:
        response.insert(0, data[m])
        data.pop(m)
        return search(left, right - 1, query, data, response)
    elif data[m][:len(query)] > query:
        return search(left, m - 1, query, data, response)
    elif data[m][:len(query)] < query:
        return search(m + 1, right, query, data, response)

data = []
query = input()
n = int(input())
for i in range(n):
    i = input()
    data.append(i)
    
response = []
hasil = "".join(response)

result = search(0, len(data) - 1, query, data, response)

print(hasil, end="\n")
