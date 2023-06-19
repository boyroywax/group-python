# Organic Organization

Ancient Algorithms and Data Structures in Python

## Algorithms
An algorithm creates on demand hierarchical data structures, and then traverses them in a depth-first manner.

### Depth-First Traversal
The depth-first traversal algorithm is implemented in the `depth_first_traversal` function in the `algorithms` module.

The algorithm takes a `root` node as input, and returns a list of nodes in the order they were visited.

The algorithm is implemented using a stack, which is a LIFO (last-in-first-out) data structure. The stack is initialized with the root node. The algorithm then loops until the stack is empty. In each iteration, the algorithm pops a node from the stack, and adds it to the list of visited nodes. The algorithm then pushes the children of the node onto the stack, in reverse order.

### Hierarchical Data Structures
The hierarchical data structures are implemented in the `hierarchical_data_structures` module.

The `Node` class represents a node in a hierarchical data structure. The `Node` class has a `value` attribute, and a `children` attribute, which is a list of `Node` objects.

The `Tree` class represents a tree data structure. The `Tree` class has a `root` attribute, which is a `Node` object.

The `Tree` class has a `depth_first_traversal` method, which calls the `depth_first_traversal` function in the `algorithms` module, passing the `root` attribute as input.

## Data Structures
A data structure creates on demand hierarchical data structures, and then traverses them in a breadth-first manner.

### Breadth-First Traversal
The breadth-first traversal algorithm is implemented in the `breadth_first_traversal` function in the `data_structures` module.

The algorithm takes a `root` node as input, and returns a list of nodes in the order they were visited.

The algorithm is implemented using a queue, which is a FIFO (first-in-first-out) data structure. The queue is initialized with the root node. The algorithm then loops until the queue is empty. In each iteration, the algorithm dequeues a node from the queue, and adds it to the list of visited nodes. The algorithm then enqueues the children of the node.

