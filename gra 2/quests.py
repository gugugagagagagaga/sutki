from utils import display_message
from Minigame import space_travel_game

class SideQuest:
    def __init__(self, title, description, reward, quest_function):
        self.title = title
        self.description = description
        self.reward = reward
        self.quest_function = quest_function

    def start(self, player):
        self.quest_function()
        player.receive_reward(self.reward)

class QuestManager:
    def __init__(self, available_quests):
        self.available_quests = available_quests

    def start_side_quest(self, player):
        for index, quest in enumerate(self.available_quests, 1):
            print(f"{index}. {quest.title}: {quest.description} (Reward: {quest.reward})")
        while True:
            try:
                choice = int(input("Choose a quest by number: ").strip())
                if 1 <= choice <= len(self.available_quests):
                    self.available_quests[choice - 1].start(player)
                    return True
                else:
                    print("Invalid choice. Please enter a number corresponding to the quest.")
            except ValueError:
                print("Invalid input. Please enter a number.")
