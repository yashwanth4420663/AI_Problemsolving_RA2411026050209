import streamlit as st
from collections import deque

# BFS
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return "No Path Found"

# DFS
def dfs(graph, start, goal, path=[]):
    path = path + [start]

    if start == goal:
        return path

    for node in graph[start]:
        if node not in path:
            newpath = dfs(graph, node, goal, path)
            if newpath:
                return newpath

    return "No Path Found"

# UI
st.title("BFS vs DFS Navigation")

# Sample graph
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = st.selectbox("Start Node", list(graph.keys()))
goal = st.selectbox("Goal Node", list(graph.keys()))

if st.button("Find Path"):
    st.subheader("Results")
    st.write("BFS Path (Shortest):", bfs(graph, start, goal))
    st.write("DFS Path:", dfs(graph, start, goal))
