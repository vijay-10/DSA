# from pytube import YouTube

# my_vid = YouTube("https://youtu.be/w4ClQO0FFQg")

# print(my_vid.title)
# print(my_vid.thumbnail_url)

# my_vid = my_vid.streams.get_lowest_resolution()
# my_vid.download()

def bruteforce(T, P):
    n, m = len(T), len(P)
    for i in range(n-m):
        j = 0
        while (j<m and T[i + j] == P[j]): j = j + 1
        if  j == m: return i
    return "There is no substring of T matching P."
            
result = bruteforce("abcdef", "de")
print(result)