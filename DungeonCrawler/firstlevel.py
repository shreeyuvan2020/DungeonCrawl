import curses
import time
import math
def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(False)
    stdscr.timeout(100)
    sh, sw = stdscr.getmaxyx()
    Dungeon = [
        "##############################################################################################",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "##                                                                                          ##",
        "#############################################################################################",
    ]
    character = [
        " O ",
        "/|\\",
        "/ \\"
    ]
    sy = max((sh - len(Dungeon))//2, 0)
    sx = max((sw - len(Dungeon[0]))//2, 0)
    ly = len(Dungeon) // 2 + sy
    lw = len(Dungeon[0]) // 2 + sx
    npc_x, npc_y = len(Dungeon[0])+5, len(Dungeon) - 5
    radius = 5
    while True:
        stdscr.clear()
        for i, row in enumerate(Dungeon):
            if sy + i < sh:
                stdscr.addstr(sy + i, sx, row[:sw])
        for i, line in enumerate(character):
            if 0 <= ly + i < sh:
                stdscr.addstr(ly+i, lw, line[:sw-lw])
        if 0 <= npc_y < len(Dungeon) and 0 <= npc_x < len(Dungeon[0]):
            stdscr.addstr(npc_y, npc_x, "@")
        if is_within_radius(ly, lw, npc_y, npc_x, radius):
            stdscr.addstr(0, 0, "You are within the radius of the NPC!")
        stdscr.refresh()
        try:
            key = stdscr.getch()
        except:
            key = -1
        new_y, new_x = ly, lw
        if key == ord('w') or key == ord('W'):
            new_y -= 1  # Up
        elif key == ord('s') or key == ord('S'):
            new_y += 1  # Down
        elif key == ord('a') or key == ord('A'):
            new_x -= 1  # Left
        elif key == ord('d') or key == ord('D'):
            new_x += 1  # Right
        elif key == ord('q') or key == ord('Q'):
            break  # Quit
        #This is the position in the dungeon
        my = new_y - sy
        mx = new_x - sx
        # Check boundaries
        if 0 <= my < len(Dungeon) and 0 <= mx < len(Dungeon[0]):
            if Dungeon[my][mx] == ' ':
                ly, lw = new_y, new_x
        npc = "@"

def is_within_radius(player_y, player_x, target_y, target_x, radius):
    distance = math.sqrt((player_y - target_y) ** 2 + (player_x - target_x) ** 2)
    return distance <= radius
curses.wrapper(main)