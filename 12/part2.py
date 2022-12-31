from string import ascii_lowercase as alpha

class Grid:
    def __init__(self, input):
        self.tiles = []
        self.grid = {}
        self.lowest = []
        self.shortest = None
        
        for y, row in enumerate(input):
            for x, char in enumerate(row):
                adj = []
                if y != 0 and self.height(input[y - 1][x]) - self.height(char) <= 1:
                    adj.append((x, y - 1))
                if y != len(input) - 1 and self.height(input[y + 1][x]) - self.height(char) <= 1:
                    adj.append((x, y + 1))
                if x != 0 and self.height(input[y][x - 1]) - self.height(char) <= 1:
                    adj.append((x - 1, y))
                if x != len(row) - 1 and self.height(input[y][x + 1]) - self.height(char) <= 1:
                    adj.append((x + 1, y))
                id = (x, y)
                if x == 0 and self.height(char) == 0:
                    self.lowest.append(id)
                if char == 'E':
                    self.end = id
                self.tiles.append(id)
                self.grid[id] = adj

    def loop_starts(self):
        for tile in self.lowest:
            path = self.dijkstra(tile)
            if self.shortest == None or path[self.end] < self.shortest[self.end]:
                self.shortest = path

    def dijkstra(self, start):
        unvisited = {tile: float('inf') for tile in self.tiles}
        unvisited[start] = 0
        visited = {}
        parents = {}
        while unvisited:
            tile_shortest = min(unvisited, key=unvisited.get)
            for neighbour in self.grid.get(tile_shortest, {}):
                if neighbour in visited:
                    continue
                new_distance = unvisited[tile_shortest] + 1
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    parents[neighbour] = tile_shortest
            visited[tile_shortest] = unvisited[tile_shortest]
            unvisited.pop(tile_shortest)
            if tile_shortest == self.end:
                break
        return visited

    def height(self, char):
        return 0 if char == 'S' else 25 if char == 'E' else alpha.index(char)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = [[char for char in line.strip('\n')] for line in f.readlines()]
    grid = Grid(input)
    grid.loop_starts()
    print(grid.shortest[grid.end])