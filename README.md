# Graph Valid Tree

**LeetCode Problem:** 261
**Language:** Python

## Problem

You are given `n` nodes and a list of undirected edges.

The task is to determine whether these edges form a valid tree.

A valid tree must satisfy two conditions:

1. It must contain exactly `n - 1` edges.
2. It must not contain a cycle.

All nodes must also belong to the same connected structure.

## Example

Input:

```text
n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
```

These edges connect all five nodes without creating a cycle.

Output:

```text
true
```

Another example:

```text
n = 5
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
```

This graph contains a cycle.

Output:

```text
false
```

## Approach

This solution uses the **Union-Find** technique, also called **Disjoint Set Union (DSU)**.

First, a tree with `n` nodes must have exactly `n - 1` edges.

So if:

```text
len(edges) != n - 1
```

the graph cannot be a tree.

Next, each node initially belongs to its own group.

For every edge `(a, b)`, we find the root of both nodes.

If both nodes already have the same root, connecting them would create a cycle, so we return `False`.

Otherwise, their groups are joined together.

If all edges are processed without finding a cycle, the graph is a valid tree.

## Union-Find

Union-Find is useful for keeping track of connected components.

The `find()` function determines the root of a node.

When two nodes have different roots, they can be connected safely.

When they have the same root, they are already connected, so adding another edge between them creates a cycle.

## Complexity

* **Time:** O(n α(n)), which is effectively O(n)
* **Space:** O(n)

The parent array stores the parent information for each node.

## Key Learning

This problem helped me practice:

* Graphs
* Trees
* Union-Find
* Cycle detection
* Connected components
* Path compression
* Graph validation

## Conclusion

The solution checks the number of edges and uses Union-Find to detect cycles. If the graph has exactly `n - 1` edges and no cycle is found, the given graph forms a valid tree.

**Author: T. Nandhini**
