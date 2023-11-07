def solution(numbers, target):
    result = 0
    def dfs(num, level):
        nonlocal result

        if level == len(numbers):
            if num == target:
                result += 1
            return

        dfs(num + numbers[level], level + 1)
        dfs(num - numbers[level], level + 1)

    dfs(0, 0)
    return result