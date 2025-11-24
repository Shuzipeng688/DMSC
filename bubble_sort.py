def bubble_sort(arr):
    """
    冒泡排序算法
    时间复杂度：O(n²)
    空间复杂度：O(1)
    稳定性：稳定1111
    """
    n = len(arr)
    
    # 外层循环控制排序轮数
    for i in range(n):
        # 优化：如果某一轮没有发生交换，说明已经有序
        swapped = False
        
        # 内层循环控制每轮比较次数
        # 每一轮后，最大的元素会"冒泡"到末尾，所以可以减少比较次数
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果没有发生交换，提前结束排序
        if not swapped:
            break
    
    return arr


def bubble_sort_demo():
    """冒泡排序演示"""
    # 测试数据
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1, 2, 3, 4, 5],  # 已排序
        [5, 4, 3, 2, 1],  # 逆序
        [42],             # 单个元素
        []                # 空数组
    ]
    
    for i, arr in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print(f"原始数组: {arr}")
        
        # 创建副本进行排序，保持原数组不变
        sorted_arr = arr.copy()
        bubble_sort(sorted_arr)
        
        print(f"排序后:   {sorted_arr}")
        print("-" * 40)


def bubble_sort_step_by_step(arr):
    """
    逐步显示冒泡排序过程
    用于教学演示
    """
    n = len(arr)
    print(f"初始数组: {arr}")
    print()
    
    for i in range(n):
        print(f"第 {i + 1} 轮排序:")
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                print(f"  交换 {arr[j]} 和 {arr[j + 1]}: {arr[:j]} -> {arr[j:j+2]} -> {arr[j+2:]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            else:
                print(f"  不交换 {arr[j]} 和 {arr[j + 1]}")
        
        print(f"  第 {i + 1} 轮后: {arr}")
        
        if not swapped:
            print("  没有发生交换，排序完成!")
            break
        print()


if __name__ == "__main__":
    print("=== 冒泡排序演示 ===")
    bubble_sort_demo()
    
    print("\n=== 逐步排序过程演示 ===")
    demo_array = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort_step_by_step(demo_array)
