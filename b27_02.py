class Gcd_Lcm:
    def __init__(self,a: int,b: int) -> None:
        self.a = a
        self.b = b
        self.gcd = self.get_GCD()
        self.lcm = self.get_LCM()

    # 2値の最大公約数を求める
    def get_GCD(self) -> int:
        a,b = self.a,self.b
        while a >= 1 and b >= 1:
            if a >= b:
                a = a % b
            else:
                b = b % a
        if a != 0:
            return a
        return b

    # 2値の最小公倍数を求める
    def get_LCM(self) -> int:
        a,b = self.a,self.b
        lcm = (a * b) // self.gcd
        return lcm

a,b = map(int,input().split())
gcd = Gcd_Lcm(a,b)

print(gcd.lcm)
