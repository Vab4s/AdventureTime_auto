import random

from URLs.episodes_names import episodes_dict

def random_episode() -> tuple:
    chosen_season = random.choice(list(episodes_dict.keys()))
    season_episodes_list = episodes_dict[chosen_season]
    chosen_episode = random.choice(season_episodes_list)
    return chosen_season, chosen_episode

# def random_episode_without_extreme_episodes() -> tuple:
#     chosen_season = random.choice(list(episodes_dict.keys())[1:-1])
#     season_episodes_list = episodes_dict[chosen_season]
#     chosen_episode = random.choice(season_episodes_list)
#     return chosen_season, chosen_episode

def random_episode_without_extreme_episodes(test_button) -> tuple:
    chosen_season = random.choice(list(episodes_dict.keys())[1:-1])
    season_episodes_list = episodes_dict[chosen_season]
    if test_button == 'next':
        chosen_episode = random.choice(season_episodes_list[:-1])
    elif test_button == 'back':
        chosen_episode = random.choice(season_episodes_list[1:])
    return chosen_season, chosen_episode
