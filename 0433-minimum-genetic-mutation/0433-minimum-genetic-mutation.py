class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        bank = set(bank)
        queue = deque()
        queue.appendleft(startGene)
        level = 0
        visited = {startGene}

        letters = ['A', 'C', 'G', 'T']

        while queue:
            for _ in range(len(queue)):
                gene = queue.pop()

                if gene == endGene: return level

                for i in range(len(gene)):
                    for letter in letters:
                        newGene = gene[:i] + letter + gene[i+1:]
                        if newGene in bank and newGene not in visited:
                            queue.appendleft(newGene)
                            visited.add(newGene)
            
            # every new level will have genes with a mutation differing from previous 
            # level by 1 letter
            level += 1

        return -1