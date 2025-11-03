import random

class Agent:
    def __init__(self, name, kind):
        self.name = name  
        self.kind = kind   
        self.score = 0
        self.has_met = False 

def simulate(hawk_count, dove_count):
    
    population = []
    for i in range(1, hawk_count+1): 
        population.append(Agent(f'H{i}', 'H'))
    for i in range(1, dove_count+1):
        population.append(Agent(f'D{i}', 'D'))

    random.shuffle(population)
    pairs = []
    for i in range(0, len(population)-1, 2): 
        a, b = population[i], population[i+1]
        if not a.has_met and not b.has_met: 
            pairs.append((a, b))
            a.has_met = b.has_met = True

    for a, b in pairs:
        if a.kind == 'D' and b.kind == 'D': 
            a.score += 50 - 10 
            b.score += - 10 
        elif a.kind == 'H' and b.kind == 'D':
            a.score += 50 
            b.score += 0
        elif a.kind == 'D' and b.kind == 'H':
            a.score += 0
            b.score += 50
        elif a.kind == 'H' and b.kind == 'H':
            winner = random.choice([a,b])
            loser = b if winner == a else a
            winner.score += 50
            loser.score += -100 

    hawk_scores = [agent.score for agent in population if agent.kind=='H']
    dove_scores = [agent.score for agent in population if agent.kind=='D']
    avg_hawk = sum(hawk_scores)/len(hawk_scores) if hawk_scores else 0
    avg_dove = sum(dove_scores)/len(dove_scores) if dove_scores else 0

    return avg_hawk, avg_dove

if __name__ == "__main__":
    hawk_count = int(input("매 개체 수: "))
    dove_count = int(input("비둘기 개체 수: "))
   
    avg_hawk, avg_dove = simulate(hawk_count, dove_count)
    print(f"매 평균 득점: {avg_hawk}")
    print(f"비둘기 평균 득점: {avg_dove}")


