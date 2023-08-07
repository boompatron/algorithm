def solution(info, edges):
    n = len(info)
    visited = [False for _ in range(n)]
    ans = []
    
    def dfs(sheep: int, wolf: int, v):
        if sheep > wolf:
            ans.append(sheep)
            # ans = max(ans, sheep)
        else:
            return
        
        for parent, child in edges:
            if v[parent] and not v[child]:
                v[child] = True
                
                if not info[child]:
                    dfs(sheep + 1, wolf, v)
                else:
                    dfs(sheep, wolf + 1, v)
                    
                v[child] = False
    
    
    visited[0] = True
    dfs(1, 0, visited)
    
    return max(ans)

    