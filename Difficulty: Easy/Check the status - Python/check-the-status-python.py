class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if a<0 and b <0:
            if flag == True:
                return True
            else:
                return False
        elif a>0 and b<0:
            if flag == True:
                return False
            else:
                return True
        elif a<0 and b>0:
            if flag == True:
                return False
            else:
                return True