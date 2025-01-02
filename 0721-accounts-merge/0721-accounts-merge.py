class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, n):
        res = n
        while self.par[res] != res:
            self.par[res] = self.par[self.par[res]]
            res = self.par[res]
        
        return res

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return 0

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = self.par[p1]
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = self.par[p2]
            self.rank[p2] += self.rank[p1]
        
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {} # emails -> account index

        for i, emails in enumerate(accounts):
            for email in emails[1:]:
                if email in emailToAcc:
                    uf.union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i

        emailGroup = defaultdict(list) # account index -> emails

        for email, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(email)
        
        result = []
        for i, emails in emailGroup.items():
            result.append([accounts[i][0]] + sorted(emails))

        return result