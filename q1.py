import math

#create a line segment only with x coordinates
class Segment:

    def __init__(self,point1, point2):
        self.p1 = point1
        self.p2 = point2

    def __str__(self):
        return ("(%i, %i)" % (self.p1, self.p2))

def overlap(seg1, seg2):
    #here modify this statement 
    if ((seg1.p1>=seg2.p1 and seg1.p1<=seg2.p2) or (seg2.p1>=seg1.p1 and seg2.p1<=seg1.p2)):
        return True
    else:
        return False

p1=1
p2=2
p3=2
p4=1
s1=Segment(p1,p2)
s2=Segment(p3,p4)
print(overlap(s1,s2))

