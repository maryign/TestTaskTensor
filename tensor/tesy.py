# coding=utf-8
# # You have 100 lamps in array
# # [1,2,3,4,5…..99,100]
# # And we have 100 trained frogs.
# # Each frog jumps on a lamp and turns its each switch on/off, in this order:
# # 1.    First frog just on each lamp
# # 2.    Second frog jump directly to the second lamp and then to the 4th lamp, 6th , 8th …
# # 3.    Third frog jump directly to the third lamp and then to the 6th lamp, 9th , 12th …
# # 4.    Forth frog jump directly to the forth lamp and then to the 8th lamp, 12th , 16th …
# # .
# # .
# # .
# # 100.  The 100 frog jump directly to the 100 lamp and then gets out
# #
# # Now we need to turn the usage of frogs to code, and you need to code it.
# # Our Framework already supplied the function that presses the lamp in the correct index.
# # press(i)
# # Please use this function to move the jumping frogs to code


#codility
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

# def solution(A):
#     # write your code in Python 2.7
#     eqind=[]
#     for i in range(len(A)):
#         sum1 = A[i]
#         sum2 = 0
#         sum3 =0
#         for k in range(i):
#             sum2 = sum2+A[k]
#         for k in range(i+1,len(A)):
#             sum3 = sum3+A[k]
#
#         if sum2 == sum3:
#             eqind.append(i)
#     if len(eqind)==0:
#         eqind.append(-1)
#     return eqind[0]
#
# A = [-1, 3, -4, 5, 1, -6, 2, 1]
# print(solution(A))


# lesson1
# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
#
# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.
#
# Write a function:
#
# int solution(int N);
# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
#
# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.
# print(bin(1041))
# def bingup(intnum):
#     binnum = bin(intnum)[2:]
#     arrlen=[]
#     lengup=0
#     for e in binnum:
#
#         if e=='0':
#             lengup = lengup+1
#         if e=='1':
#             # lengup = 0
#             arrlen.append(lengup)
#             lengup = 0
#
#     max=0
#     for el in arrlen:
#         if el>max:
#             max = el
#         # else:
#         #     arrlen.append(lengup)
#
#     return arrlen
# print bingup(1041)

# task2
# A non-empty zero-indexed array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.
#
# For example, in array A such that:
#
# A[0] = 9  A[1] = 3  A[2] = 9
# A[3] = 3  A[4] = 9  A[5] = 7
# A[6] = 9
# the elements at indexes 0 and 2 have value 9,
# the elements at indexes 1 and 3 have value 3,
# the elements at indexes 4 and 6 have value 9,
# the element at index 5 has value 7 and is unpaired.
# Write a function:
#
# int solution(int A[], int N);
#that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.
# For example, given array A such that:
#
# A[0] = 9  A[1] = 3  A[2] = 9
# A[3] = 3  A[4] = 9  A[5] = 7
# A[6] = 9
# the function should return 7, as explained in the example above.
#
# Assume that:
#
# N is an odd integer within the range [1..1,000,000];
# each element of array A is an integer within the range [1..1,000,000,000];
# all but one of the values in A occur an even number of times.
from string import count


# def solution(A):
#     num = 0
#     if len(A)%2!=0:
#         for each in A:
#             n = A.count(each)
#             # for k in range(len(A)):
#             #     if A[i]==
#             # n= count(each)
#             if n==1:
#                 num =  each
#     return num
# A=[9, 3, 9, 3, 9, 7, 9]
# print solution(A)
# def solution(A, B, M, X, Y):
#     stops = 0
#     # for k in range(len(A)):
#
#     weight = 0
#     passcount=0
#     for i in range(X+1):
#         # print i
#         while(weight<Y):
#             weight = weight+A[i]
#             passcount = passcount+i
#         print passcount
#         floors = set(B[0:passcount])
#         # print floors
#         # stops = len(floors)+1
#         # print stops
#
#     # write your code in Python 2.7
#     return stops
import networkx as nx


# def solution(A, B, M, X, Y):
def solution(A):
    # G=nx.path_graph(5)
    # G = nx.Graph()
    # for e in A:
    #     for n in A:
    #         if e!=n:
    #             G.add_edge(e,n)
    setA = set(A)
    if setA in A:
        return len(set)
    else:
        lena =0
        for a1 in setA:
            for each  in A:
                if a1 == each:
                    lena = lena+1
        return lena

    # return nx.shortest_path(G,weight=1)#.shortest_path_length(G):
        # print e
print solution([7, 3, 7, 3, 1, 3, 4, 1])
    # stop = 0
    # for k in range(len(A)):
    # sumweight = 0
    # for a in A:
    #     sumweight = sumweight+a
    # if len(A)<=X and sumweight<=Y:
    #     stops = len(set(B))+1
    # elif len(A)>X:# and sumweight>Y:
    # weight = 0
    # for a in range(len(A)):
    #     l=0
    #     weight = weight+A[a]
    #     if weight<=Y and a+1<=X:
    #         l=l+1
    #     if weight>Y:
    #         weight = 0
    #     stops = len(set(B[a-l:a]))+1
    #     stop = stop+stops
    # return stop+1

    # weight = 0
    # bind=0
    # stop=0
    # stops=0
    # for a in range(len(A)):
    #     weight = weight+A[a]
    #     if weight>Y and a+1<=X:
    #         bindfin = a
    #         stops = len(set(B[bind:bindfin]))+1
    #         bind = a
    #         weight=0
    #     stop = stop+stops
    # return stop+1
# print solution([60,80,40], [2,3,5], 5, 2, 200)
#
# print solution([40,40,100,80,20], [3,3,2,2,3], 3, 5, 200)
# D=[2,3,5]
# floors = set(D[0:2])
# print len(floors)+1