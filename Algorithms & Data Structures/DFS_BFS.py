# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 12:26:43 2020

@author: Geo
"""

graph={}
graph['A'] = ['B','C']
graph['B'] = ['A','D']
graph['C'] = ['A','G','H','I']
graph['D'] = ['B','E','F']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C','J']
graph['E'] = ['D']
graph['F'] = ['D']
graph['J'] = ['I']



def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited



dfs_res = dfs(graph, 'A')




def bfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited


bfs_res = bfs(graph, 'A')






