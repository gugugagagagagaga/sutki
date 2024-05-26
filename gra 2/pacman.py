import time
class PacmanGame:
    def __init__(self):
        self.levels = self.create_levels()
        self.current_level = 0
        self.score = 0
        self.lives = 3
        self.player_x, self.player_y = 1, 1
        self.player_icon = '@'
        self.enemy_icon = 'E'
        self.exit_icon = 'X'
        self.enemies = []
        self.load_level()

    def create_levels(self):
        level1 = [
            "####################",
            "#........#....E....#",
            "#.##.###.#.###.##..#",
            "#.##.###.#.###.##..#",
            "#.................X#",
            "#.##.#.#####.#.##..#",
            "#.##.#..###..#.##..#",
            "#.....#.###.#......#",
            "####################"
        ]
        level2 = [
            "####################",
            "#..........#....E..#",
            "#.####.###...###.##.#",
            "#..................#",
            "#.####.###.###.####.#",
            "#.####.###.###.####.#",
            "#..........###..X..#",
            "#.####.####...####.#",
            "####################"
        ]
        level3 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level4 = [
            "####################",
            "#..........#....E..#",
            "#.####.###...###.##.#",
            "#..................#",
            "#.####.###.###.####.#",
            "#.####.###.###.####.#",
            "#..........###..X..#",
            "#.####.####...####.#",
            "####################"
        ]
        level5 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level6 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level7 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level8 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level9 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level10 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level11 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level12 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level13 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level14 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level15 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level16 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level17 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level18 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level19 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        level20 = [
            "####################",
            "#.....#.......E...##",
            "#.###.#.###.#####.##",
            "#.....#.........#..#",
            "#.#####.#####.###..#",
            "#.....#.......#...##",
            "#.###.##..###.###.##",
            "#........#.....X...#",
            "####################"
        ]
        return [level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, 
                level11, level12, level13, level14, level15, level16, level17, level18, level19, level20]

    def load_level(self):
        self.map = [list(row) for row in self.levels[self.current_level]]
        self.player_x, self.player_y = 1, 1
        self.enemies = []
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if cell == self.enemy_icon:
                    self.enemies.append([x, y])
                    self.map[y][x] = ' '
        self.map[self.player_y][self.player_x] = self.player_icon
        self.score += 10 * self.current_leveld
        
    def display(self):
        print("\n" * 5)
        for row in self.map:
            print("".join(row))
        print(f'Score: {self.score} Lives: {self.lives}')

    def move_player(self, direction):
        new_x, new_y = self.player_x, self.player_y
        if direction == 'w':
            new_y -= 1
        elif direction == 's':
            new_y += 1
        elif direction == 'a':
            new_x -= 1
        elif direction == 'd':
            new_x += 1

        if self.map[new_y][new_x] in ' .':
            self.map[self.player_y][self.player_x] = ' '
            self.player_x, self.player_y = new_x, new_y
            self.map[self.player_y][self.player_x] = self.player_icon
            if self.map[new_y][new_x] == '.':
                self.map[new_y][new_x] = ' '
                self.score += 1
        elif self.map[new_y][new_x] == self.exit_icon:
            self.next_level()

    def move_enemies(self):
        for enemy in self.enemies:
            ex, ey = enemy
            new_ex, new_ey = ex, ey

            if ex < self.player_x:
                new_ex = ex + 1
            elif ex > self.player_x:
                new_ex = ex - 1

            if ey < self.player_y:
                new_ey = ey + 1
            elif ey > self.player_y:
                new_ey = ey - 1

            if self.map[new_ey][new_ex] in ' .':
                self.map[ey][ex] = ' '
                enemy[0], enemy[1] = new_ex, new_ey
                self.map[new_ey][new_ex] = self.enemy_icon

            if new_ex == self.player_x and new_ey == self.player_y:
                self.lives -= 1
                self.load_level()

    def check_level_complete(self):
        for row in self.map:
            if '.' in row:
                return False
        return True

    def next_level(self):
        self.current_level += 1
        if self.current_level >= len(self.levels):
            self.current_level = 0  
        self.load_level()

    def play(self):
        while self.lives > 0:
            self.display()
            move = input("Move (w/a/s/d): ")
            if move in ['w', 'a', 's', 'd']:
                self.move_player(move)
            self.move_enemies()
            if self.check_level_complete():
                self.next_level()
            time.sleep(0.1)
        print("Game Over!")

if __name__ == "__main__":
    game = PacmanGame()
    game.play()