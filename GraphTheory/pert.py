import math

def pert_est(expected, optimistic, pessimistic):
    """
    PERT算法实现
    :param expected: 预期时间
    :param optimistic: 最乐观时间
    :param pessimistic: 最悲观时间
    :return: PERT估算时间
    """
    return (optimistic + 4 * expected + pessimistic) / 6

def pert_analysis(activity_list):
    """
    PERT分析实现
    :param activity_list: 活动列表，每个元素为[activity_name, optimistic, expected, pessimistic]
    :return: (关键路径, 项目总预期时间)
    """
    # 初始化活动信息
    activity_dict = {}
    for activity in activity_list:
        name, optimistic, expected, pessimistic = activity
        activity_dict[name] = [optimistic, expected, pessimistic]

    # 计算PERT估算时间
    for activity in activity_dict:
        optimistic, expected, pessimistic = activity_dict[activity]
        activity_dict[activity].append(pert_est(expected, optimistic, pessimistic))

    # 初始化活动关系
    activity_relation = {}
    for activity in activity_dict:
        activity_relation[activity] = []

    # 建立活动关系
    for activity in activity_dict:
        optimistic, expected, pessimistic, pert = activity_dict[activity]
        for successor in activity_dict:
            if successor != activity:
                successor_optimistic, successor_expected, successor_pessimistic, successor_pert = activity_dict[successor]
                if optimistic <= successor_optimistic <= expected and optimistic <= successor_expected <= expected and optimistic <= successor_pessimistic <= expected:
                    activity_relation[activity].append(successor)

    # 计算每个活动的最早开始时间（EST）
    est_dict = {activity: 0 for activity in activity_dict}
    for activity in activity_dict:
        if not activity_relation[activity]:
            est_dict[activity] = activity_dict[activity][3]

    while True:
        is_updated = False
        for activity in activity_dict:
            if activity_relation[activity]:
                est = max([est_dict[predecessor] + activity_dict[predecessor][3] for predecessor in activity_relation[activity]])
                if est > est_dict[activity]:
                    est_dict[activity] = est
                    is_updated = True
        if not is_updated:
            break

    # 计算每个活动的最晚开始时间（LST）和总浮动时间（TF）
    lst_dict = {activity: est_dict[activity] for activity in activity_dict}
    tf_dict = {}
    for activity in activity_dict:
        if not activity_relation[activity]:
            tf_dict[activity] = 0

    while True:
        is_updated = False
        for activity in activity_dict:
            if activity_relation[activity]:
                lst = min([lst_dict[successor] - activity_dict[activity][3] for successor in activity_relation[activity]])
                if lst < lst_dict[activity]:
                    lst_dict[activity] = lst
                    is_updated = True
                    tf_dict[activity] = lst_dict[activity] - est_dict[activity]
        if not is_updated:
            break

    # 计算项目总预期时间和关键路径
    total_expected_time = max([lst_dict[activity] + activity_dict[activity][3] for activity in activity_dict])
    critical_path = []
    for activity in activity_dict:
        if lst_dict[activity] + activity_dict[activity][3] == total_expected_time:
            critical_path.append(activity)

    return (critical_path, total_expected_time)

activity_list = [
['A', 3, 6, 9],
['B', 2, 4, 6],
['C', 1, 2, 3],
['D', 2, 3, 4],
['E', 1, 2, 3],
['F', 3, 4, 5],
['G', 2, 3, 4]
]

critical_path, total_expected_time = pert_analysis(activity_list)
print("关键路径为：", critical_path)
print("项目总预期时间为：", total_expected_time)