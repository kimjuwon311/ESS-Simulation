import matplotlib.pyplot as plt #matplolib 이라고 하는 파이썬 라이브러리임. 표나 그래프로 도식화 할 때 많이 이용함.

#(수동 입력 필요!!) 리스트인데, 값은 다 임의로 넣어둔 거고 지금 총 6개 시뮬레이션만 그래프로 표현하는 상황임. 더 만들어도 됨.
simulation_names = ["sim1", "sim2", "sim3", "sim4", "sim5", "sim6"] #시뮬레이션 이름. sim+n형식으로 해놓음.

#(수동 입력 필요!!) 각각 시뮬레이션에서 매 개체군이랑 비둘기 개체군 평균 점수 입력하는 부분. 꼭 리스트 지켜서 입력하셈(이를테면 첫번째 칸엔 "sim1"의 경우..)
hawk_scores = [10, 5, -20, 15, 25, 0]     # 매 평균 점수
dove_scores = [20, 15, 30, 10, -5, 0]     # 비둘기 평균 점수

#(수동 입력 필요!!) 각각 시뮬레이션에서 매랑 비둘기 개체 수. 보기 편하라고 넣어 둠. 그래프 점 위에 표시 될거임.
hawk_counts = [30, 25, 20, 15, 40, 35]    # 매 개체 수
dove_counts = [70, 75, 80, 85, 60, 65]    # 비둘기 개체 수

# 그래프 크기. 범위가 넓어서 좀 크게 해 둠.
plt.figure(figsize=(10, 6))

# 꺾은 선 그래프
plt.plot(simulation_names, hawk_scores, label="Hawk Avg score", marker='o', linewidth=2, color='red')
plt.plot(simulation_names, dove_scores, label="Dove Avg score", marker='s', linewidth=2, color='blue')

# 각각 시뮬레이션 당 비둘기, 매 수 그래프. 색은 구분해놨는데 겹쳐서 표시될 수도 있긴 함. 어쩔 수 없는 듯.
for i, name in enumerate(simulation_names):
    plt.text(i, hawk_scores[i] + 3, f"H={hawk_counts[i]}", ha='center', fontsize=9, color='red')
    plt.text(i, dove_scores[i] - 6, f"D={dove_counts[i]}", ha='center', fontsize=9, color='blue')

# 기타 그래프 스타일. 참고로 각 축에 들어가는 이름은 한글로 입력하면 깨져서 꼭 영어로 입력해야 함.
plt.title("Hawk-Dove simulation: Average score by Simulation", fontsize=16, pad=20)
plt.xlabel("Simulations", fontsize=13)
plt.ylabel("Avg score", fontsize=13)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.ylim(-120, 60)

# 출력하는 부분
plt.show()


