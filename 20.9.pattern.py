# # 1..
# # * * * * * 
# #   * * * * *
# #     * * * * *
# #       * * * * *
# #         * * * * *
# n = 5
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for k in range(n):
#         print("*", end=" ")
#     print()



# # 2..
# # *****

# # *   *

# # *   *

# # *****
# n = 4   
# m = 5   
# for i in range(n):
#     for j in range(m):
#         if i == 0 or i == n - 1 or j == 0 or j == m - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# # 3..
# # A
# # AB
# # ABC
# # ABCD
# for i in range(26):
#     for j in range(i+1):
#         print(chr(65+j ), end="")
#     print()


# # 4..
# # A
# # BB
# # CCC
# # DDDD
# # EEEEE
# for i in range(26): 
#     for j in range(i+1):
#         print(chr(65+i ), end="")
#     print()



# # 5..
# # E 
# # DE 
# # CDE 
# # BCDE
# # ABCDE 
# n = 5   
# for i in range(n):
#     start = 69 - i  
#     for j in range(i + 1):
#         print(chr(start + j), end="")
#     print()


# # 6..
# #     *
# #    **
# #   ***
# #  ****
# # *****
# n = 5  
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")   
#     for k in range(i):
#         print("*", end="")  
#     print()


# # 7..
# #     1
# #    12
# #   123
# #  1234
# # 12345
# n = 5  
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")   
#     for k in range(1, i + 1):
#         print(k, end="")     
#     print()



# # 8..
# # 12345
# #  1234
# #   123
# #    12
# #     1
# n = 5
# for i in range(n, 0, -1):
#     for s in range(n - i):
#         print(" ", end="")
#     for j in range(1, i+1):
#         print(j, end="")
#     print()


# # 9..
# # ABCDE
# #  ABCD
# #   ABC
# #    AB
# #     A
# n = 5
# for i in range(n, 0, -1):
#     for s in range(n - i):
#         print(" ", end="")
#     for j in range(i):
#         print(chr(65 + j), end="")   
#     print()



# # 10..
# #         * * * * * 
# #       * * * * *
# #     * * * * *
# #   * * * * *
# # * * * * *
# n = 5  
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end=" ")
#     for j in range(n):
#         print("*", end=" ")
#     print()


# # 11.. 
# #         1 2 3 4 5 
# #       1 2 3 4 5
# #     1 2 3 4 5
# #   1 2 3 4 5
# # 1 2 3 4 5
# n = 5
# for i in range(n):
#     for s in range(n - i - 1):
#         print("  ", end="")
#     for j in range(1, n + 1):
#         print(j, end=" ")
#     print()


# # 12..
# #         A B C D E 
# #       A B C D E
# #     A B C D E
# #   A B C D E
# # A B C D E
# n = 5
# for i in range(n):
#     for s in range(n - i - 1):
#         print("  ", end="")
#     for j in range(n):
#         print(chr(65 + j), end=" ")
#     print()



# # 13.. 
# #         * 
# #       * * *
# #     * * * * *
# #   * * * * * * *
# # * * * * * * * * *
# n = 5  
# for i in range(n):
#     for s in range(n - i - 1):
#         print("  ", end="")
#     for j in range(2 * i + 1):
#         print("*", end=" ")
#     print()


# # 14..
# #         * 
# #       *   *
# #     *       *
# #   *           *
# # * * * * * * * * *
# n = 5 
# for i in range(n):
#     for s in range(n - i - 1):
#         print("  ", end="")
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2 * i or i == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



# # 15..
# # * * * * * * * * * 
# #   * * * * * * * 
# #     * * * * * 
# #       * * * 
# #         * 
# n = 5  
# for i in range(n, 0, -1):
#     for s in range(n - i):
#         print("  ", end="")
#     for j in range(2 * i - 1):
#         print("*", end=" ")
#     print()


# # 16..
# # *
# # **
# # ***
# # ****
# # ***
# # **
# # *
# n = 4 
# for i in range(1, n + 1):
#     print("*" * i)
# for i in range(n - 1, 0, -1):
#     print("*" * i)

# # 17..
# #    *
# #   **
# #  ***
# # ****
# #  ***
# #   **
# #    *
# n = 4  
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * i)
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "*" * i)



# # 18..
# #     * 
# #    * * 
# #   * * * 
# #  * * * * 
# # * * * * * 
# #  * * * * 
# #   * * * 
# #    * * 
# #     * 
# n = 5 
# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "* " * i)



# # 19..
# # 1
# # 12
# # 123
# # 1234
# # 12345
# n = 5  
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()


# # 20..
# # 12345
# # 1234
# # 123
# # 12
# # 1
# n = 5 
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()



# # 21..
# # 1
# # 12
# # 1 3
# # 1  4
# # 12345
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if j == 1 or j == i or i == n:
#             print(j, end="")
#         else:
#             print(" ", end="")  
#     print()


# # 22..
# #     1
# #    232
# #   34543
# #  4567654
# # 567898765
# n = 5  
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(i, 2 * i):
#         print(j, end="")
#     for j in range(2 * i - 2, i - 1, -1):
#         print(j, end="")
#     print()


# # 23..
# #     1
# #    1 2
# #   1   3
# #  1     4
# # 1 2 3 4 5
# n = 5  
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         if j == 1 or j == i or i == n:
#             print(j, end=" ")
#         else:
#             print(" ", end=" ")
#     print()



# # 24..
# # 1 2 3 4 5
# # 2     5
# # 3   5
# # 4 5
# # 5
# n = 5
# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         if i == 1:
#             print(j, end=" ")
#         elif j == i or j == n:
#             print(j, end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# # 25..
# #         1 
# #       1 2 3 
# #     1 2 3 4 5 
# #   1 2 3 4 5 6 7 
# # 1 2 3 4 5 6 7 8 9 
# #   1 2 3 4 5 6 7 
# #     1 2 3 4 5 
# #       1 2 3 
# #         1
# n = int(input("Enter n: "))   
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end=" ")
#     for j in range(1, 2 * i):
#         print(j, end=" ")
#     print()

# for i in range(n - 1, 0, -1):
#     for j in range(n - i):
#         print(" ", end=" ")
#     for j in range(1, 2 * i):
#         print(j, end=" ")
#     print()



# # 26..
# # 123456789
# #  1234567
# #   12345
# #    123
# #     1
# #    123
# #   12345
# #  1234567
# # 123456789
# n = 5  
# for i in range(n, 0, -1):
#     for s in range(n - i):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print(j, end="")
#     print()

# for i in range(2, n + 1):
#     for s in range(n - i):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print(j, end="")
#     print()


# # 27..
# # ABCDEFGHI
# #  ABCDEFG
# #   ABCDE
# #    ABC
# #     A
# #    ABC
# #   ABCDE
# #  ABCDEFG
# # ABCDEFGHI
# n = 5 
# for i in range(n, 0, -1):
#     for s in range(n - i):
#         print(" ", end="")
#     for j in range(i * 2 - 1):
#         print(chr(65 + j), end="")
#     print()

# for i in range(2, n + 1):
#     for s in range(n - i):
#         print(" ", end="")
#     for j in range(i * 2 - 1):
#         print(chr(65 + j), end="")
#     print()



# # 29..
# # *****
# # *   *
# # *   *
# # *   *
# # ***** 
# rows = 5
# cols = 5
# for i in range(rows):
#     for j in range(cols):
#         if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



# # 30..
# # 1 2 3 4 5 
# # 1       5
# # 1       5
# # 1       5
# # 1 2 3 4 5
# rows = 5
# cols = 5
# for i in range(1, rows + 1):
#     for j in range(1, cols + 1):
#         if i == 1 or i == rows or j == 1 or j == cols:
#             print(j, end=" ")
#         else:
#             print("  ", end="")
#     print()




# # 31..
# # A B C D E 
# # A       E
# # A       E
# # A       E
# # A B C D E
# rows = 5
# cols = 5
# for i in range(rows):
#     for j in range(cols):
#         if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
#             print(chr(65 + j), end=" ")  
#         else:
#             print("  ", end="")
#     print()



# # 32..
# #     *    
# #    * *   
# #   *   *  
# #  *     * 
# # *       *
# #  *     * 
# #   *   *  
# #    * *   
# #     *    
# n = 5  
# for i in range(1, n + 1):
#     for j in range(1, 2 * n):
#         if j == n - i + 1 or j == n + i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# for i in range(n - 1, 0, -1):
#     for j in range(1, 2 * n):
#         if j == n - i + 1 or j == n + i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# # 33..
# #     1    
# #    2 2   
# #   3   3  
# #  4     4 
# # 5       5
# #  4     4 
# #   3   3  
# #    2 2   
# #     1    
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, 2 * n):
#         if j == n - i + 1 or j == n + i - 1:
#             print(i, end="")
#         else:
#             print(" ", end="")
#     print()

# for i in range(n - 1, 0, -1):
#     for j in range(1, 2 * n):
#         if j == n - i + 1 or j == n + i - 1:
#             print(i, end="")
#         else:
#             print(" ", end="")
#     print()



# # 34..
# #     A    
# #    A C  
# #   A   E  
# #  A     G
# # A       I
# #  A     G
# #   A   E  
# #    A C   
# #     A    
# n = 5  
# for i in range(1, n + 1):
#     line = [' '] * (2 * n - 1)
#     line[n - i] = chr(65)  
#     line[n + i - 2] = chr(65 + 2*(i-1))  
#     print(''.join(line))

# for i in range(n - 1, 0, -1):
#     line = [' '] * (2 * n - 1)
#     line[n - i] = chr(65)
#     line[n + i - 2] = chr(65 + 2*(i-1))
#     print(''.join(line))


# # 35..
# #     1
# #    1 1
# #   1 2 1
# #  1 3 3 1
# # 1 4 6 4 1
# n = 5  
# for i in range(n):
#     print(' ' * (n - i - 1), end='')
#     val = 1
#     for j in range(i + 1):
#         print(val, end=' ')
#         val = val * (i - j) // (j + 1)  
#     print()


# # 36..
# # *       *
# # **     **
# # ***   ***
# # **** ****
# # *********
# # **** ****
# # ***   ***
# # **     ** 
# # *       *
# n = 5  
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end="")
#     for j in range(1, (n-i)*2 + 1):
#         print(" ", end="")
#     for j in range(1, i+1):
#         print("*", end="")
#     print()

# for i in range(n-1, 0, -1):
#     for j in range(1, i+1):
#         print("*", end="")
#     for j in range(1, (n-i)*2 + 1):
#         print(" ", end="")
#     for j in range(1, i+1):
#         print("*", end="")
#     print()



# # 37 ..
# # **********
# # ****  ****
# # ***    ***
# # **      **
# # *        *
# # *        *
# # **      **
# # ***    ***
# # ****  ****
# # **********
# n = 5  
# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print("*", end="")
#     for j in range(1, (n-i)*2 + 1):
#         print(" ", end="")
#     for j in range(1, i+1):
#         print("*", end="")
#     print()

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end="")
#     for j in range(1, (n-i)*2 + 1):
#         print(" ", end="")
#     for j in range(1, i+1):
#         print("*", end="")
#     print()



