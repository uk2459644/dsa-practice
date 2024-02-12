
string = input()
n = len(string)


def find_longest_string(str1, str2, str3):
    # find the length of each string
    len1 = len(str1)
    len2 = len(str2)
    len3 = len(str3)
    # compare the lengths and return the longest string

    if len1 > len2 and len1 > len3:
        return str1
    elif len2 > len3 and len2 > len1:
        return str2
    else:
        return str3


def find_longest_of_two(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 > len2:
        return str1
    else:
        return str2


def solve(word: str, start, end, start_word, end_word):
    if start > end:
        return start_word+end_word

    if start == end:
        ans = start_word+word[start]+end_word
        return ans

    if word[start] == word[end]:
        start_word = start_word+word[start]
        end_word = word[end]+end_word
        return solve(word, start+1, end-1, start_word, end_word)

    if word.find(start_word+end_word) == -1:
        string1 = solve(word, start+1, n-1, "", "")
        string2 = solve(word, 0, end-1, "", "")
        return find_longest_of_two(string1, string2)
    string1 = solve(word, start+1, end, "", "")
    string2 = solve(word, start, end-1, "", "")

    return find_longest_string(start_word+end_word, string1, string2)


print(solve(string, 0, n-1, "", ""))
