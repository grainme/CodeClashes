#Example:--------------------------
#>>> md
#>>> md5fg27dm5p
#Between the first letter m and the last letter d, we have the values 5 and 27.
#Thus, we obtain: 5 + 27 = 32 -------------------

import re


def main():
    n = input()
    s = input()
    try:
        word = s[s.index(n[0]):s.rindex(n[len(n)-1])+1]
        print(sum(list(map(int,re.findall("\d+",word)))))
    except ValueError:
        print(0)

        
if __name__=="__main__":
    main()
