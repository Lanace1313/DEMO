import random
import math

# 城市坐标
cities = {
    '广州': (113.264434, 23.129162),
    '深圳': (114.057868, 22.543099),
    '珠海': (113.576726, 22.270715),
    '佛山': (113.121435, 23.021478),
    '东莞': (113.751765, 23.020536),
    '惠州': (114.416196, 23.111847),
    '中山': (113.392782, 22.517646),
    '江门': (113.081901, 22.578738),
    '肇庆': (112.465091, 23.046237),
    '阳江': (111.982232, 21.857958),
    '茂名': (110.925456, 21.662999),
    '湛江': (110.364977, 21.274898),
    '梅州': (116.117582, 24.299112),
    '汕头': (116.681972, 23.354091),
    '揭阳': (116.379500, 23.547999),
    '韶关': (113.597522, 24.810403),
    '清远': (113.056042, 23.681774),
    '潮州': (116.622603, 23.656950),
    '河源': (114.700447, 23.743538),
    '汕尾': (115.364238, 22.774485),
    '云浮': (112.044439, 22.929801)
}

# 生成初始解
def generate_initial_solution(cities):
    cities_list = list(cities.keys())
    cities_list.remove('广州')  # 先移除广州
    random.shuffle(cities_list)
    solution = ['广州'] + cities_list + ['广州']  # 加入广州作为起点和终点
    return solution

# 计算路径长度
def calculate_distance(city1, city2):
    lon1, lat1 = cities[city1]
    lon2, lat2 = cities[city2]
    distance = math.sqrt((lon2 - lon1) ** 2 + (lat2 - lat1) ** 2)
    return distance

# 计算路径总长度
def calculate_total_distance(solution):
    total_distance = 0
    for i in range(len(solution) - 1):
        city1 = solution[i]
        city2 = solution[i + 1]
        total_distance += calculate_distance(city1, city2)
    return total_distance

# 模拟退火算法
def simulated_annealing(cities):
    temperature = 10000  # 初始温度
    cooling_rate = 0.003  # 退火速率
    current_solution = generate_initial_solution(cities)
    best_solution = current_solution.copy()
    while temperature > 1:
        new_solution = current_solution.copy()
        # 随机交换两个城市（除了广州）的位置
        index1 = random.randint(1, len(new_solution)-2)
        index2 = random.randint(1, len(new_solution)-2)
        new_solution[index1], new_solution[index2] = new_solution[index2], new_solution[index1]
        current_distance = calculate_total_distance(current_solution)
        new_distance = calculate_total_distance(new_solution)
        # 根据目标函数差和温度决定是否接受新解
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
            current_solution = new_solution
        # 更新最优解
        if calculate_total_distance(current_solution) < calculate_total_distance(best_solution):
            best_solution = current_solution.copy()
        temperature *= (1 - cooling_rate)
    return best_solution

# 执行模拟退火算法
best_route = simulated_annealing(cities)
total_distance = calculate_total_distance(best_route)

print("模拟退火最优线路：", best_route)
print("路径总长度：", total_distance)