class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg=[0]*numCourses
        graph=defaultdict(list)
        for course,dest in prerequisites:
            graph[dest].append(course)
            indeg[course]+=1
        q=[]
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)
        finish=[]
        while q:
            node=q.pop(0)
            finish.append(node)
            for nei in graph[node]:
                indeg[nei]-=1
                if indeg[nei]==0:
                    q.append(nei)
        if len(finish)==numCourses:
            return finish
        else:
            return []