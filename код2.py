import tkinter as tk
from tkinter import messagebox, ttk
import random

# Головне вікно програми
root = tk.Tk()
root.title("Камінь, ножиці, папір")
root.geometry("400x300")

# Глобальні змінні
user_score = 0
computer_score = 0
player1_score = 0
player2_score = 0
current_mode = None
choices = ["камінь", "ножиці", "папір"]

# Функція для створення головного меню
def create_main_menu():
    clear_window()
    
    tk.Label(root, text="Оберіть режим гри:", font=("Arial", 14)).pack(pady=20)
    
    tk.Button(root, text="Грати проти комп'ютера", 
              command=lambda: start_game("computer"), width=20).pack(pady=10)
    tk.Button(root, text="Грати вдвох", 
              command=lambda: start_game("two_players"), width=20).pack(pady=10)
    tk.Button(root, text="Вийти", command=root.quit, width=20).pack(pady=10)

# Функція для початку гри
def start_game(mode):
    global current_mode
    current_mode = mode
    clear_window()
    
    if mode == "computer":
        create_computer_mode()
    else:
        create_two_players_mode()

# Функція гри проти комп'ютера
def play_vs_computer(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "Нічия!"
    elif (user_choice == "камінь" and computer_choice == "ножиці") or \
         (user_choice == "ножиці" and computer_choice == "папір") or \
         (user_choice == "папір" and computer_choice == "камінь"):
        result = "Ви перемогли!"
        user_score += 1
    else:
        result = "Комп'ютер переміг!"
        computer_score += 1

    update_score_display()
    
    messagebox.showinfo("Результат", 
                       f"Ви обрали: {user_choice}\n"
                       f"Комп'ютер обрав: {computer_choice}\n\n"
                       f"{result}")

# Функція гри для двох гравців
def play_vs_player(player, choice):
    global player1_choice, player2_choice, player1_score, player2_score
    
    if player == 1:
        player1_choice = choice
        choices_frame1.pack_forget()
        choices_frame2.pack()
        turn_label.config(text="Гравець 2, оберіть свій хід:")
    else:
        player2_choice = choice
        determine_two_players_winner()

# Визначення переможця для двох гравців
def determine_two_players_winner():
    global player1_score, player2_score
    
    if player1_choice == player2_choice:
        result = "Нічия!"
    elif (player1_choice == "камінь" and player2_choice == "ножиці") or \
         (player1_choice == "ножиці" and player2_choice == "папір") or \
         (player1_choice == "папір" and player2_choice == "камінь"):
        result = "Гравець 1 переміг!"
        player1_score += 1
    else:
        result = "Гравець 2 переміг!"
        player2_score += 1

    update_score_display()
    
    messagebox.showinfo("Результат", 
                       f"Гравець 1 обрав: {player1_choice}\n"
                       f"Гравець 2 обрав: {player2_choice}\n\n"
                       f"{result}")
    
    # Повертаємо інтерфейс до початкового стану
    reset_two_players_round()

# Оновлення відображення рахунку
def update_score_display():
    if current_mode == "computer":
        score_label.config(text=f"Ви: {user_score}  Комп'ютер: {computer_score}")
    else:
        score_label.config(text=f"Гравець 1: {player1_score}  Гравець 2: {player2_score}")

# Скидання раунду для двох гравців
def reset_two_players_round():
    choices_frame2.pack_forget()
    choices_frame1.pack()
    turn_label.config(text="Гравець 1, оберіть свій хід:")

# Очищення вікна
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Створення інтерфейсу для гри з комп'ютером
def create_computer_mode():
    tk.Label(root, text="Гра проти комп'ютера", font=("Arial", 12)).pack(pady=10)
    
    tk.Label(root, text="Оберіть свій хід:").pack(pady=5)
    
    tk.Button(root, text="Камінь", command=lambda: play_vs_computer("камінь")).pack(fill=tk.X, padx=50, pady=2)
    tk.Button(root, text="Ножиці", command=lambda: play_vs_computer("ножиці")).pack(fill=tk.X, padx=50, pady=2)
    tk.Button(root, text="Папір", command=lambda: play_vs_computer("папір")).pack(fill=tk.X, padx=50, pady=2)
    
    global score_label
    score_label = tk.Label(root, text=f"Ви: {user_score}  Комп'ютер: {computer_score}", font=("Arial", 10))
    score_label.pack(pady=10)
    
    tk.Button(root, text="Головне меню", command=create_main_menu).pack(pady=10)

# Створення інтерфейсу для гри двох гравців
def create_two_players_mode():
    global choices_frame1, choices_frame2, turn_label
    
    tk.Label(root, text="Гра для двох гравців", font=("Arial", 12)).pack(pady=10)
    
    turn_label = tk.Label(root, text="Гравець 1, оберіть свій хід:", font=("Arial", 10))
    turn_label.pack(pady=5)
    
    # Вибір для гравця 1
    choices_frame1 = tk.Frame(root)
    choices_frame1.pack()
    
    tk.Button(choices_frame1, text="Камінь", command=lambda: play_vs_player(1, "камінь")).pack(side=tk.LEFT, padx=5)
    tk.Button(choices_frame1, text="Ножиці", command=lambda: play_vs_player(1, "ножиці")).pack(side=tk.LEFT, padx=5)
    tk.Button(choices_frame1, text="Папір", command=lambda: play_vs_player(1, "папір")).pack(side=tk.LEFT, padx=5)
    
    # Вибір для гравця 2 (спочатку прихований)
    choices_frame2 = tk.Frame(root)
    
    tk.Button(choices_frame2, text="Камінь", command=lambda: play_vs_player(2, "камінь")).pack(side=tk.LEFT, padx=5)
    tk.Button(choices_frame2, text="Ножиці", command=lambda: play_vs_player(2, "ножиці")).pack(side=tk.LEFT, padx=5)
    tk.Button(choices_frame2, text="Папір", command=lambda: play_vs_player(2, "папір")).pack(side=tk.LEFT, padx=5)
    
    global score_label
    score_label = tk.Label(root, text=f"Гравець 1: {player1_score}  Гравець 2: {player2_score}", font=("Arial", 10))
    score_label.pack(pady=10)
    
    tk.Button(root, text="Головне меню", command=create_main_menu).pack(pady=10)

# Запуск програми
create_main_menu()
root.mainloop()