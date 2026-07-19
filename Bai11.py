import random

def game():
    human_score = 0
    computer_score = 0
    choices = ["b", "d", "k"]

    while True:
        human = input("Nhập ký tự (b-d-k), ký tự khác để thoát: ").strip().lower()

        if human not in choices:
            print("\n--- TRÒ CHƠI KẾT THÚC ---")
            print(f"Tỷ số chung cuộc (Human - Computer): {human_score} - {computer_score}")
            break
        
        computer = random.choice(choices)
        print(f"Computer: {computer}")
        
        if human == computer:
            print("Kết quả: Hòa lượt này!")
        elif (human == 'b' and computer == 'd') or \
             (human == 'd' and computer == 'k') or \
             (human == 'k' and computer == 'b'):
            print("Kết quả: Bạn THẮNG lượt này!")
            human_score += 1
        else:
            print("Kết quả: Máy THẮNG lượt này!")
            computer_score += 1
            
        print(f"Tỷ số hiện tại (Human - Computer): {human_score} - {computer_score}\n")

if __name__ == "__main__":
    game()