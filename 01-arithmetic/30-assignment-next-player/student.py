def next_player(player, player_count):
    return (player + 1) % player_count

print(next_player(9, 10))