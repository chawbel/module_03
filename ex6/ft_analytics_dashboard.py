if __name__ == "__main__":
    game_data = {
    "players": {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "sessions_played": 13,
            "favorite_mode": "ranked",
            "achievements_count": 5,
            "region": "north",
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "sessions_played": 27,
            "favorite_mode": "ranked",
            "achievements_count": 2,
            "region": "east",
        },
        "charlie": {
            "level": 44,
            "total_score": 9935,
            "sessions_played": 21,
            "favorite_mode": "ranked",
            "achievements_count": 7,
            "region": "central",
        },
        "diana": {
            "level": 3,
            "total_score": 1488,
            "sessions_played": 21,
            "favorite_mode": "casual",
            "achievements_count": 4,
            "region": "north",
        },
        "eve": {
            "level": 33,
            "total_score": 1434,
            "sessions_played": 81,
            "favorite_mode": "casual",
            "achievements_count": 7,
            "region": "east",
        }
    },

    "sessions": [
        {"player": "bob", "duration_minutes": 94, "score": 1831, "mode": "competitive", "completed": False},
        {"player": "alice", "duration_minutes": 98, "score": 1981, "mode": "ranked", "completed": True},
        {"player": "diana", "duration_minutes": 39, "score": 2721, "mode": "ranked", "completed": True},
        {"player": "eve", "duration_minutes": 29, "score": 2985, "mode": "casual", "completed": True},
        {"player": "charlie", "duration_minutes": 56, "score": 1196, "mode": "casual", "completed": True},
        {"player": "alice", "duration_minutes": 53, "score": 1238, "mode": "competitive", "completed": False},
        {"player": "bob", "duration_minutes": 52, "score": 1555, "mode": "casual", "completed": False},
        {"player": "eve", "duration_minutes": 46, "score": 2101, "mode": "casual", "completed": True},
        {"player": "charlie", "duration_minutes": 22, "score": 1110, "mode": "ranked", "completed": False},
        {"player": "alice", "duration_minutes": 42, "score": 1880, "mode": "casual", "completed": False}
        ],

    "game_modes": [
        "casual",
        "competitive",
        "ranked"
        ],

    "achievements": [
        "first_blood",
        "level_master",
        "speed_runner",
        "treasure_seeker",
        "boss_hunter",
        "first_blood",
        "speed_runner",
        ]
    }


    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    print("High scorers (>2000): "
          f"{[player for player in game_data['players'] if game_data['players'][player]['total_score'] > 2000]}")
    print("Scores doubled: "
        f"{[data['total_score'] * 2 for data in game_data['players'].values()]}")
    print("Active players: "
          f"{[player for player, data in game_data['players'].items() if data['sessions_played'] > 20]}")
    print("")

    print("=== Dict Comprehension Example ===")
    print("Player scores:", {player: data['total_score'] for player, data in game_data['players'].items()})
    score_categories = {
        "high": sum(1 for data in game_data['players'].values() if data['total_score'] > 4000),
        "medium": sum(1 for data in game_data['players'].values() if data['total_score'] > 2500 and data['total_score'] <= 4000),
        "low": sum(1 for data in game_data['players'].values() if data['total_score'] >= 2500) 
    }
    print("Score Categories:", score_categories)
    achievement_counts = {player: data['achievements_count'] for player, data in game_data['players'].items()}
    print(f"Achievement counts: {achievement_counts}")
    print("")

    print("Set Comprehension Examples ===")
    unique_players = {player for player in game_data['players'].keys()}
    print(f"Unique players: {unique_players}")
    unique_achievments = {achievement for achievement in game_data['achievements']}
    print(f"Unique achivements: {unique_achievments}")
    active_regions = {data['region'] for data in game_data['players'].values()}
    print(f"Active regions: {active_regions}")
    print("")

    print("=== Combined Analysis ===")
    total_players = len([player for player in game_data['players'].keys()])
    print(f"Total players: {total_players}")
    print(f"Total unique achivements: {len(unique_achievments)}")
    total_score = sum([data['total_score'] for data in game_data['players'].values()])
    print(f"Average score: {total_score / total_players:.1f}")
    max_score = max(
        data['total_score'] for data in game_data['players'].values()
    )
    top_name = [
        player
        for player, data in game_data['players'].items()
        if data['total_score'] == max_score
    ][0]
    top_achievement = [
        data['achievements_count']
        for data in game_data['players'].values()
        if data['total_score'] == max_score
    ][0]
    top_performer = {
        "name": top_name,
        "score": max_score,
        "achievements": top_achievement,
    }
    print(f"Top performer: {top_performer['name']}"
          f" ({top_performer['score']} points, "
          f"{top_performer['achievements']} achievements)")

