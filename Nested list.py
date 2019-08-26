marks=[]
Totalscore=[]
if __name__ == '__main__':
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marks+=[[name,score]]
                Totalscore+=[score]
        b=sorted(list(set(Totalscore)))[1] 

        for a,c in sorted(marks):
             if c==b:
                    print(a)
