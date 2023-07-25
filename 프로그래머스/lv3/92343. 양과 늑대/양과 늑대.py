def solution(info, edges):
    n = len(info)
    visited = [False for _ in range(n)]
    ans = []
    
    def dfs(sheep: int, wolf: int):
        if sheep > wolf:
            ans.append(sheep)
        else:
            return
        
        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = True
                
                if not info[child]:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                    
                visited[child] = False
    
    
    visited[0] = True
    dfs(1, 0)
    
    return max(ans)

    