#### 그래프(Graph)

> 실제 세계의 현상이나 사물을 정점(Vertex) 또는 노드(Node)와 간선(Edge)로 표현하기 위해 사용

---

<div style="text-align: left;"><img style="max-height:20%; max-width:25%; " src="https://www.fun-coding.org/00_Images/graph.png"></div>



##### 그래프 관련 용어

- 노드(Node) : 위치를 말함, 정점(Vertex)라고도 함
- 간선 (Edge) : 위치 간의 관계를 표시한 선으로 노드를 연결한 선이라고 보면 됨 ( link 또는 branch )

- 인접 정점 (Adjacent Vertex): 간선으로 직접 연결된 정점(또는 노드)
  - 정점의 차수 (Degree) : 무방향 그래프에서 하나의 정점에 인접한 정점의 수
  - 진입 차수 ( In-Degree): 방향 그래프에서 외부에서 오는 간선수
  - 진출 차수 (Out - Degree): 방향 그래프에서 외부로 향하는 간선의 수
  - 경로 길이 (Path Length): 경로를 구성하기 위해 사용된 간선의 수
  - 단순 경로 (Simple Path): 처음 정점과 끝 정점을 제외하고 중복된 정점이 없는 경로 
  - 사이클 (Cycle): 단순 경로의 시작 정점과 종료 정점이 동일한 경우
