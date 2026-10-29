class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for item in strs:
            n = len(item)
            res += "#"
            number = str(len(item))
            n_len = str(len(number))
            res += n_len
            res += number
            res += item
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []


        flag_n_len = 0

        flag_n = 0

        

        count = 0
        # len_number = 0
        number = ""
        # n_len_cal = 0
        
        # n_count = 0
        n = 0

        s_len = len(s)
        index = 0

        decoded = ""

        while index < s_len:
            
            if s[index] == "#" and count == 0 and n == 0:
                flag_n_len = 1

            elif flag_n_len == 1:
                n_len_c = int(s[index])
                flag_n_len = 0
                flag_n = 1

            elif flag_n == 1:
                number += s[index]

                if len(number) == n_len_c:
                    n = int(number)
                    number = ""

                    flag_n = 0
                    if n == 0:
                        res.append(decoded)
            
            else:

                decoded += s[index]
                count += 1

                if count == n:
                    res.append(decoded)
                    decoded = ""
                    count = 0
                    n = 0
            index += 1
        return res