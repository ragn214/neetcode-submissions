class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #$mapping charcount to list of anagrams
                #defaultdict(list) helps when the key doesn't yet exist.
        for s in strs:
            count = [0] * 26   # to store all 26 possible letters and the counts

            for c in s:
                count[ord(c) - ord("a")] += 1 # ord = ascii number.
                #Subtract from ascii value of "a" gives index

            res[tuple(count)].append(s) # tuple because lists can't be keys in dicts

        return list(res.values())

        # grouped_anagrams = [[]]
        # for index, string in enumerate(strs):
        #     print("")
        #     print(index,string)
        #     print("".join(sorted(strs[index])))
        #     print("before ")
        #     print(grouped_anagrams)
        #     print("sorted")
        #     sorted_grouped_anagrams = [[''.join(sorted(word)) for word in sublist] for sublist in grouped_anagrams]
        #     print(sorted_grouped_anagrams)

        #     for sublist in grouped_anagrams:
        #         if "".join(sorted(strs[index])) in sorted_grouped_anagrams:
        #             grouped_anagrams.append([strs[index]])
        #         else:
        #             grouped_anagrams[-1].append(strs[index])

        #     print("after ") 
        #     print(grouped_anagrams)
        # return grouped_anagrams