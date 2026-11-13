from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    v = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        v[a].append(b)
        v[b].append(a)
    visited = [False]*(N+1)
    ans = 0
    for i in range(1, N+1):
        q = deque()
        if visited[i]:
            continue
        else:
            visited[i] = True
            for a in v[i]:
                q.append(a)
            while q:
                s = q.popleft()
                visited[s] = True
                for b in v[s]:
                    if visited[b]:
                        continue
                    else:
                        q.append(b)
            ans += 1

    print(f'#{tc} {ans}')