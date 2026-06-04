class Solution:
    def isValid(self, s: str) -> bool:

    ######################
        # countround = 0
        # countcurved = 0
        # countsquare = 0

        # for bracket in s:
        #     if bracket == "(":
        #         countround += 1
        #     if bracket == ")":
        #         countround -= 1
        #     if bracket == "{":
        #         countcurved += 1
        #     if bracket == "}":
        #         countcurved -= 1
        #     if bracket == "[":
        #         countsquare += 1
        #     if bracket == "]":
        #         countsquare -= 1
        #     if countround * countcurved * countsquare < 0:
        #         return False

        # return True

        indexopening = {"(":0, "{":1, "[":2}
        indexclosing = {")":0, "}":1, "]":2}
        lastbracketstack = []
        if s[0] in indexclosing:
            return False

        for bracket in s:
            if bracket in indexopening:
                lastbracketstack.append(bracket)
                print("if bracket in indexopening:")
            elif not lastbracketstack:
                return False
            elif indexopening[lastbracketstack[-1]] == indexclosing[bracket]:
                lastbracketstack.pop(-1)
                print("indexopening[lastbracketstack[-1]] == indexclosing[bracket]:")
            else:
                return False
            print(lastbracketstack)
        print(lastbracketstack)

        return not lastbracketstack


