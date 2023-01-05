class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ind_a,ind_b,ind_c=-1,-1,-1
        count=0
        for i,x in enumerate(s):
            if x=='a':
                ind_a=i
            elif x=='b':
                ind_b=i
            else:
                ind_c=i
            if i>1:
                count+=min([ind_a,ind_b,ind_c])+1
        return count
