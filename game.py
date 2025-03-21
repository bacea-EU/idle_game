import time
import math
import os
import threading

class ExponentialIdle:
    def __init__(self):
        self.knowledge = 1.0  # Initial knowledge
        self.growth_rate = 0.1  # Base growth rate
        self.upgrade_cost = 10.0  # Cost to upgrade growth rate
        self.auto_upgrade = False  # Automation toggle
        self.prestige_points = 0  # Prestige system
        self.running = True
        
    def gain_knowledge(self):
        self.knowledge *= math.exp(self.growth_rate)
    
    def upgrade_growth(self):
        if self.knowledge >= self.upgrade_cost:
            self.knowledge -= self.upgrade_cost
            self.growth_rate *= 1.1  # Increase growth rate
            self.upgrade_cost *= 1.5  # Increase cost exponentially
            print(f"Upgraded! New growth rate: {self.growth_rate:.5f}, Next upgrade cost: {self.upgrade_cost:.2f}")
        else:
            print("Not enough knowledge to upgrade.")

    def toggle_automation(self):
        self.auto_upgrade = not self.auto_upgrade
        print(f"Automation {'enabled' if self.auto_upgrade else 'disabled'}.")

    def check_prestige(self):
        if self.knowledge >= 10000:  # Arbitrary prestige threshold
            self.prestige_points += 1
            self.knowledge = 1.0
            self.growth_rate = 0.01 * (1 + self.prestige_points * 0.5)  # Boost from prestige
            self.upgrade_cost = 10.0
            print(f"Prestige activated! Prestige Points: {self.prestige_points}, New Growth Rate: {self.growth_rate:.5f}")

    def display_stats(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
        print(f"Knowledge: {self.knowledge:.2f}, Growth Rate: {self.growth_rate:.5f}, Prestige Points: {self.prestige_points}")
    
    def update_loop(self):
        while self.running:
            time.sleep(1)
            self.gain_knowledge()
            self.check_prestige()
            if self.auto_upgrade and self.knowledge >= self.upgrade_cost:
                self.upgrade_growth()
            self.display_stats()
    
    def start(self):
        update_thread = threading.Thread(target=self.update_loop)
        update_thread.daemon = True
        update_thread.start()
        
        while True:
            action = input("Press 'u' to upgrade, 'a' to toggle automation, 'q' to quit: ")
            if action.lower() == 'u':
                self.upgrade_growth()
            elif action.lower() == 'a':
                self.toggle_automation()
            elif action.lower() == 'q':
                self.running = False
                break

if __name__ == "__main__":
    game = ExponentialIdle()
    game.start()
