import random

# Intro message that appears at the start
print("\033[1;32;40m")  # This sets the text color to green (optional)
print("********** Welcome to the Boxer Game **********")
print("Here you will simulate the selection of winning boxes and cards.")
print("Let's start the simulation!\n")
print("\033[0m")  # Reset to default color

# کارڈز کی ڈیک تیار کرنے کا فنکشن
def create_deck():
    """کارڈز کی ڈیک تیار کریں"""
    suits = ['♠', '♥', '♦', '♣']  # ہر سوٹ کے لیے
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # ہر رینک کے لیے
    deck = [rank + suit for suit in suits for rank in ranks]  # سوٹ اور رینک کا مجموعہ بنائیں
    random.shuffle(deck)  # ڈیک کو مکس کریں
    return deck

# کارڈ کے رینک کا نمبر تبدیل کرنے کا فنکشن
def rank_to_value(rank):
    """کارڈ کے رینک کو ایک عددی قیمت میں تبدیل کریں"""
    if rank in ['J', 'Q', 'K', 'A']:
        return {'J': 11, 'Q': 12, 'K': 13, 'A': 14}[rank]
    return int(rank)

# اسکرپٹ کا مرکزی فنکشن
def simulate_game():
    """گیم کا سمیولیشن چلائیں"""
    
    # آپ سے پہلے سے جیتنے والے باکس کا انتخاب کریں
    print("Please tell which box has already won (1, 2, or 3):")
    predicted_winner_box = input("Enter the winning box number (1, 2, or 3): ")
    if predicted_winner_box not in ['1', '2', '3']:
        print("Invalid box number! Please enter 1, 2, or 3.")
        return
    
    print(f"\nYou predicted box {predicted_winner_box}. Now, here are all the 52 cards. Please select 3 cards from the winning box:")
    
    # ڈیک میں موجود تمام کارڈز دکھائیں
    deck = create_deck()
    show_cards_in_categories(deck)
    
    # آپ سے منتخب کردہ 3 کارڈز پوچھیں
    print("\nPlease enter the 3 cards you want to select (separate them by space):")
    
    # تین کارڈز کے انتخاب کے لیے ان پٹ لیں
    selected_cards_input = input("Enter 3 cards (e.g., '10♠ 9♠ A♦'): ").strip()
    
    # کارڈز کو اسپیس سے علیحدہ کریں
    selected_cards = selected_cards_input.split()
    
    if len(selected_cards) != 3:
        print("You must enter exactly 3 cards!")
        return
    
    # چیک کریں کہ منتخب کردہ کارڈز ڈیک میں سے ہیں یا نہیں
    for card in selected_cards:
        if card not in deck:
            print(f"Invalid card: {card}. Please enter a valid card from the deck.")
            return
    
    # اس بات کا یقین کریں کہ یہ جیتنے والے باکس ہیں
    print(f"\nYou have provided the following cards: {selected_cards}")
    
    # 10,000 ہاتھوں کی سمیولیشن چلائیں
    win_count = {1: 0, 2: 0, 3: 0}  # ہر باکس کی جیت گننے کے لیے
    winning_cards = {1: [], 2: [], 3: []}  # جیتنے والے باکس کے کارڈز ذخیرہ کرنے کے لیے
    
    # 10,000 ہاتھوں کی سمیولیشن
    for _ in range(10000):
        # تینوں باکسز میں سے ہر ایک میں 3 کارڈز کا انتخاب کریں
        box1 = random.sample(deck, 3)
        box2 = random.sample(deck, 3)
        box3 = random.sample(deck, 3)
        
        # منتخب کردہ کارڈز کی موجودگی کا چیک کریں
        if all(card in box1 for card in selected_cards):
            winning_box = 1
        elif all(card in box2 for card in selected_cards):
            winning_box = 2
        elif all(card in box3 for card in selected_cards):
            winning_box = 3
        else:
            # اگر منتخب کردہ کارڈز کسی بھی باکس میں نہ ہوں، تو تصادفی طور پر ایک باکس کا انتخاب کریں
            winning_box = random.choice([1, 2, 3])
        
        # جیتنے والے باکس کو شمار کریں
        win_count[winning_box] += 1
        winning_cards[winning_box] = box1 if winning_box == 1 else box2 if winning_box == 2 else box3
    
    # نتائج دکھائیں
    print(f"\nAfter 10,000 simulations:")
    print(f"Box 1 won {win_count[1]} times")
    print(f"Box 2 won {win_count[2]} times")
    print(f"Box 3 won {win_count[3]} times")
    
    # تمام باکسز اور ان کے کارڈز دکھائیں
    print("\nDetails of all the boxes and their cards:")
    show_all_boxes_with_cards([1, 2, 3], winning_cards)
    
    # جیتنے والے باکس اور اس کے کارڈز کی تفصیل دکھائیں
    print(f"\nThe winning box is Box {winning_box} with the following cards:")
    print(f"Winning cards: {', '.join(winning_cards[winning_box])}")

# جیتنے والے باکس کے کارڈز کو دکھانے کا فنکشن
def show_winning_cards(winning_cards):
    """ہر باکس کے جیتنے والے کارڈز دکھائیں"""
    for box in winning_cards:
        print(f"\nBox {box} winning cards: {', '.join(winning_cards[box])}")

# کارڈز کو سوٹ اور رینک کے حساب سے ایک لائن میں دکھائیں
def show_cards_in_categories(deck):
    """کارڈز کو سوٹ اور رینک کے حساب سے ایک لائن میں دکھائیں"""
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    # ہر سوٹ کے لئے کارڈز کو ترتیب سے ایک لائن میں دکھائیں
    for suit in suits:
        print(f"\nSuit: {suit}", end=" -> ")
        for rank in ranks:
            card = rank + suit
            print(card, end=" ")
        print()  # لائن کا وقفہ

# تمام باکسز اور ان کے کارڈز دکھانے کا فنکشن
def show_all_boxes_with_cards(boxes, winning_cards):
    """تمام باکسز اور ان کے کارڈز دکھائیں"""
    for box in boxes:
        print(f"\nBox {box}: {', '.join(winning_cards[box])}")

# گیم سمیولیشن چلائیں
simulate_game()
