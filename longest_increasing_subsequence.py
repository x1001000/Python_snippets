sequence = input('Input a sequence separated by \",\"\n')
length = [1]*len(sequence)
for R in range(len(sequence)):
    for L in range(R):
        if sequence[L] < sequence[R]:
            if length[L] >= length[R]:
                length[R] += 1
max_length = max(length)
result = []
for i in range(len(sequence)-1,-1,-1):
    if max_length == length[i]:
        result.append(sequence[i])
        max_length -= 1
result.reverse()
print 'I found one LIS in your sequence...\n' + str(result)
