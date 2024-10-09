
# arr1 = [1, 4, 5, 7]
# arr2 = [10, 27, 30, 40]
# X = 32

# # Initialize pointers
# i, j = 0, len(arr2) - 1
# pairs = []

# # Initialize the minimum difference
# currsum = arr1[0] + arr2[len(arr2) - 1]
# minsum = abs(currsum - X)
# mini = minsum

# while i < len(arr1) and j >= 0:
#     currsum = arr1[i] + arr2[j]
#     minsum = abs(currsum - X)

#     if minsum < mini:
#         mini = minsum
#         pairs = [(arr1[i], arr2[j])]
#     elif minsum == mini:
#         pairs.append((arr1[i], arr2[j]))
    
#     if currsum < X:
#         i += 1
#     else:
#         j -= 1

# print(pairs)

# maxli=[]
# a,b = input().split()
# for i in range(int(a)):
#     n=list(input().split())
#     n.pop(0)
#     m = max(n)
#     maxli.append(int(m))
# print(maxli)
# sumfx=sum(map(lambda x:x*x,maxli))
# res=sumfx% int(b)
# print(res)
        

def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    return reversed_str

# Example usage
s = "Hello World!"
print("Reversed string:", reverse_string(s))



def reverse_words(s):
    li=[]
    li=s.split()
    print(li)
    li.reverse()
    print(" ".join(li))
reverse_words(s)