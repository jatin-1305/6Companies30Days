def dis(x1,x2,y1,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        x1,x2,x3,x4 = p1[0],p2[0],p3[0],p4[0]
        y1,y2,y3,y4 = p1[1],p2[1],p3[1],p4[1]
        p12=dis(x1,x2,y1,y2)
        p13=dis(x1,x3,y1,y3)
        p14=dis(x1,x4,y1,y4)
        p23=dis(x2,x3,y2,y3)
        p24=dis(x2,x4,y2,y4)
        p34=dis(x3,x4,y3,y4)
        l=[p12,p13,p14,p23,p24,p34]
        l.sort()
        return True if l[0]==l[1]==l[2]==l[3] and l[0]!=l[-1] and l[4]==l[5] and round(l[4],3)==round((math.sqrt(2))*l[0],3) else False
