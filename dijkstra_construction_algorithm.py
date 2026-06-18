
import heapq

def dijkstra_optimized(graph: dict, start_node: str) -> tuple[dict, dict]:
    """
    优化版Dijkstra最短路径算法（最小堆实现）
    时间复杂度：O((V+E)logV)，优于传统暴力遍历版本
    :param graph: 带权重的邻接图字典
    :param start_node: 起始节点
    :return: 最短距离字典、前驱路径字典
    """
    # 初始化所有节点距离为无穷大
    distance = {node: float("inf") for node in graph}
    distance[start_node] = 0

    # 记录路径前驱节点，用于回溯完整路径
    prev_node = {node: None for node in graph}

    # 最小堆：(当前距离, 当前节点)，初始化压入起点
    heap_queue = []
    heapq.heappush(heap_queue, (0, start_node))

    # 核心算法迭代逻辑
    while heap_queue:
        current_dist, current_node = heapq.heappop(heap_queue)

        # 剪枝：若当前距离大于已记录最短距离，直接跳过
        if current_dist > distance[current_node]:
            continue

        # 遍历当前节点的所有邻接节点
        for neighbor, weight in graph[current_node].items():
            temp_dist = current_dist + weight
            # 松弛操作：更新更短路径
            if temp_dist < distance[neighbor]:
                distance[neighbor] = temp_dist
                prev_node[neighbor] = current_node
                heapq.heappush(heap_queue, (temp_dist, neighbor))

    return distance, prev_node


def get_shortest_path(prev_node: dict, end_node: str) -> list:
    """
    根据前驱节点字典，回溯生成完整最短路径
    :param prev_node: 前驱节点字典
    :param end_node: 终点节点
    :return: 完整路径列表
    """
    path = []
    current = end_node

    while current is not None:
        path.append(current)
        current = prev_node[current]
    
    # 反转路径，从起点到终点
    return path[::-1]


# ====================== 工程场景测试案例 ======================
# 模拟：建筑工地场地节点 + 物料运输距离权重
# 节点：材料仓库、加工区、施工楼栋、废料区、出入口
if __name__ == "__main__":
    # 构建工程场地网络图
    construction_site_graph = {
        "Warehouse": {"ProcessingArea": 4, "Entrance": 2},
        "ProcessingArea": {"Building1": 3, "WasteArea": 1, "Warehouse": 4},
        "Building1": {"WasteArea": 5, "ProcessingArea": 3},
        "WasteArea": {"Entrance": 3, "ProcessingArea": 1, "Building1": 5},
        "Entrance": {"Warehouse": 2, "WasteArea": 3}
    }

    # 以材料仓库为起点，计算全场最优运输路径
    start = "Warehouse"
    dist_result, path_result = dijkstra_optimized(construction_site_graph, start)

    # 输出计算结果
    print("=== 工程场地最短运输距离计算结果 ===")
    for node, dist in dist_result.items():
        full_path = get_shortest_path(path_result, node)
        print(f"到{node} 最短距离：{dist} | 最优路径：{' → '.join(full_path)}")
