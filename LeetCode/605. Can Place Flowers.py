class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        zero_count = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                zero_count = zero_count + 1
            else:
                pass
        elif len(flowerbed) == 2:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                zero_count = zero_count + 1
            else:
                pass
        else:
            if flowerbed[0] ==0 and flowerbed[1]==0:
                zero_count=zero_count+1
                flowerbed[0]=1
            for x in range(1,len(flowerbed)-1):

                print(x)
                preele = flowerbed[x - 1]
                curele = flowerbed[x]
                nexele = flowerbed[x + 1]

                if preele == 0 and curele == 0 and nexele == 0:
                    zero_count = zero_count + 1
                    flowerbed[x]=1
                else:
                    pass
            if flowerbed[-1]==0 and flowerbed[-2]==0:
                zero_count=zero_count+1
                flowerbed[-1]=1


        if n <= zero_count:
            return True
        else:
            return False


call = Solution()
print(call.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
