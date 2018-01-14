nodeChildren = dict()
nodeWeights = dict()
nodeParents = dict()
file = open('input.txt', 'r')
for line in file:
    parts = line.split('->')
    leftParts = parts[0].split()
    root = leftParts[0]
    weight = int(leftParts[1].strip('()'))
    children = []
    if len(parts) > 1:
        children = [x.strip() for x in parts[1].split(',')]
    nodeChildren[root] = children
    nodeWeights[root] = weight
    for child in children:
        nodeParents[child] = root
file.close()

current = next(iter(nodeParents.values()))
while current in nodeParents:
    current = nodeParents[current]
print(current)
nodeTotalWeights = dict()


def totalWeight(node):
    if node in nodeTotalWeights:
        return nodeTotalWeights[node]
    total = nodeWeights[node]
    for child in nodeChildren[node]:
        total += totalWeight(child)
    nodeTotalWeights[node] = total
    #print(node, total)
    return total


nodeTotalWeights[current] = totalWeight(current)


def correctWeight(node):
    totalWeights = sorted([nodeTotalWeights[x] for x in nodeChildren[node]])
    if totalWeights[0] != totalWeights[-1]:
        for child in nodeChildren[node]:
            if nodeTotalWeights[child] != totalWeights[1]:
                return correctWeight(child)
    siblingWeights = sorted([
        nodeTotalWeights[x] for x in nodeChildren[nodeParents[node]]
    ])
    return siblingWeights[1] - (nodeTotalWeights[node] - nodeWeights[node])


print(correctWeight(current))
