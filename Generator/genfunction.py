def pagination(max_limit,page_size=10):
    i = 0

    while (i<max_limit):
        page_limit = i+ page_size
        j = i
        result = []
        while (j < page_limit):
            if j < max_limit:
               result.append(j)
            j= j +1
        yield result
        i = i + page_size

print("----------")
page = pagination(20)
print(next(page))
print(next(page))
print("----------")

print("------ Pagination --------")
for i in pagination(86):
    print(i)