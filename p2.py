#---- 2) Find the string is palindrome or not if not palindrome check whether there is any palindrome sub-string and return palindrome sub-string with max length.
'''eg: i / p: "abcbaca"
  o / p: abcba, 5
'''


def collections(s):
  n = len(s)
  l = []
  rl = []
  result = []

# sub=""
  for i in range(n):
    sub = s[i]
    for j in range(i + 1, n):
      sub += s[j]
      rsub = sub[::-1]
      l.append(sub)
      rl.append(rsub)

      if(sub == rsub):
        result.append(sub)
  # print(result)

  max_len = len(result[0])
  max_str = result[0]
  for i in range(1, len(result)):
    if(len(result[i]) > max_len):
      max_str = result[i]
      max_len = len(result[i])

  print(max_str, max_len)


s = input()
collections(s)
