class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        A = 0
        B = 0
        s_list = ['']*len(secret)
        g_list = ['']*len(guess)


        for i in range(len(secret)):
            s_list[i] = secret[i]
            g_list[i] = guess[i]

        for i in range(len(secret)):
            if secret[i] == guess[i]: 
                A += 1
                s_list.remove(secret[i])
                g_list.remove(guess[i])

    
        for i in range(len(g_list)):
            if g_list[i] in s_list:
                B += 1
                s_list.remove(g_list[i])


        str_ans = str(A) + "A" + str(B) + "B"

        return str_ans