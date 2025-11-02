import random #랜덤 라이브러리 내부의 모듈들 불러오기

class Agent:
    def __init__(self, name, kind):
        self.name = name    # H1, D1 등. 그냥 매랑 비둘기 이름 지어주기^^
        self.kind = kind    # 'H' 또는 'D'. 종 구분해주기. 매는 H, 비둘기는 D로 함.
        self.score = 0
        self.has_met = False  # 이미 다른 상대와 만났는지 확인... 이미 싸웠으면 다시 안싸움

def simulate(hawk_count, dove_count):
    # 1. 에이전트 생성: 개체군 생성하기
    population = []
    for i in range(1, hawk_count+1): #파이썬에서 가장 많이 사용되는 반복문 for문. range는 리스트 생성해주는 역할임. 
        #대충 1부터 (입력한)개체 수까지의 리스트에서 수를 하나씩 뽑아서 에이전트 이름(H1 이런 식) 정한 다음 'population'리스트에 추가한다고 생각하면 됨.
        population.append(Agent(f'H{i}', 'H'))
    for i in range(1, dove_count+1):
        population.append(Agent(f'D{i}', 'D'))

    # 2. 랜덤 매칭: 아무나 만나라
    random.shuffle(population)
    pairs = []
    for i in range(0, len(population)-1, 2): #참고로 range() 안의 구조는 0부터 시작하는 정수로, 'len(population)-1' 이전의 수까지, 공차가 2인 등차수열의 리스트 만드는 거임.
        a, b = population[i], population[i+1]
        if not a.has_met and not b.has_met: #만나는 경우를 pair리스트에 순서쌍으로 집어넣고, 둘은 이미 만났으니까 더이상 싸울 필요 없다고 표시해주는 거임.
            pairs.append((a, b))
            a.has_met = b.has_met = True

    # 3. 매칭별 점수 계산하기
    for a, b in pairs:
        if a.kind == 'D' and b.kind == 'D': #비둘기 대 비둘기
            a.score += 50 - 10  # 승자 50, 시간 낭비 -10
            b.score += - 10 #시간 낭비 -10
        elif a.kind == 'H' and b.kind == 'D': #매 대 비둘기
            a.score += 50 #승자 50
            b.score += 0
        elif a.kind == 'D' and b.kind == 'H': #비둘기 대 매
            a.score += 0
            b.score += 50
        elif a.kind == 'H' and b.kind == 'H': #매 대 매
            winner = random.choice([a,b])
            loser = b if winner == a else a
            winner.score += 50
            loser.score += -100 #중상자 -100

    # 4. 평균 득점 계산하기
    hawk_scores = [agent.score for agent in population if agent.kind=='H']
    dove_scores = [agent.score for agent in population if agent.kind=='D']
    avg_hawk = sum(hawk_scores)/len(hawk_scores) if hawk_scores else 0
    avg_dove = sum(dove_scores)/len(dove_scores) if dove_scores else 0

    return avg_hawk, avg_dove

#인풋이랑 출력. 무작위로 만나는 프로그램이다보니 같은 수치로 입력해도 결과가 다르게 나올 수 있음.
if __name__ == "__main__":
    hawk_count = int(input("매 개체 수: "))
    dove_count = int(input("비둘기 개체 수: "))
    #첵에서는 매 수 대 비둘기 수가 7:5일 때 각 개체군의 평균 점수가 같아져서 가장 안정하다고 했는데
    #매에다가 7마리, 비둘기에다가 5마리 입력하면 결과가 절대 그렇게 안 나옴..
    #큰 수의 법칙에 따라 통계적 확률이 수학적 확률에 가까워 지려면 시행 횟수를 한없이 크개 해야 하니까..
    #실험 결과 매 7만 마리, 비둘기 5만 마리 정도 풀어놓으니까 어느정도 관찰 되는 듯. 시뮬레이션 할 때 적어도 몇십만 단위로는 하는 거 추천.

    avg_hawk, avg_dove = simulate(hawk_count, dove_count)
    print(f"매 평균 득점: {avg_hawk}")
    print(f"비둘기 평균 득점: {avg_dove}")

#참고로 보고있다시피 파이썬 주석은 앞에 샾 달아서 쓰면 됨. 누군가에게 코드 설명할 땐 이렇게 해보길..
'''이렇게도 쓸 수 있음.'''
