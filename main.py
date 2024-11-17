import random

# Function to set up lottery rules
def set_lottery_rules():
    print("Welcome to the Lottery Simulator!")

    total_numbers = int(input("Amount of numbers: "))
    numbers_picked = int(input("Selected numbers: "))
    
    prize_tiers = int(input("Prize tiers: "))
    prizes = []
    ticket_price = float(input("Ticket price: "))
    
    print(f"Enter the prize amounts for the top {prize_tiers} prize tiers:")
    for i in range(prize_tiers):
        correct_numbers = numbers_picked - i  # Calculate the number of correct numbers for each tier
        prize_amount = int(input(f"Enter the prize for {correct_numbers} correct numbers: "))
        prizes.append(prize_amount)
    
    return total_numbers, numbers_picked, ticket_price, prizes


# Function to buy lottery tickets
def buy_tickets(total_numbers, numbers_picked, ticket_price):
    tickets = []
    
    num_tickets = int(input("How many tickets would you like to buy? "))
    
    for i in range(num_tickets):
        choice = input(f"Would you like to fill ticket {i+1} manually or randomize? (m/r): ").strip().lower()
        
        if choice == 'm':
            ticket = set_manual_ticket(total_numbers, numbers_picked)
        elif choice == 'r':
            ticket = set_random_ticket(total_numbers, numbers_picked, tickets)
        else:
            print("Invalid choice. Randomizing ticket by default.")
            ticket = set_random_ticket(total_numbers, numbers_picked, tickets)
        
        tickets.append(ticket)
    
    return tickets

# Function to set a manual ticket
def set_manual_ticket(total_numbers, numbers_picked):
    ticket = set()
    print(f"Pick {numbers_picked} numbers from 1 to {total_numbers}:")
    
    while len(ticket) < numbers_picked:
        number = int(input(f"Enter number {len(ticket)+1}: "))
        if number < 1 or number > total_numbers:
            print(f"Please enter a number between 1 and {total_numbers}.")
        elif number in ticket:
            print("You have already picked that number. Pick a different one.")
        else:
            ticket.add(number)
    
    return ticket

# Function to generate a random ticket
def set_random_ticket(total_numbers, numbers_picked, existing_tickets):
    while True:
        ticket = set(random.sample(range(1, total_numbers + 1), numbers_picked))
        if ticket not in existing_tickets:
            break
    return ticket

# Function to run the lottery draw
def run_lottery_draw(total_numbers, numbers_picked):
    return set(random.sample(range(1, total_numbers + 1), numbers_picked))

# Function to check ticket results
def check_results(tickets, winning_numbers, prizes):
    total_winnings = 0
    results = []
    
    for ticket in tickets:
        correct_count = len(ticket.intersection(winning_numbers))
        prize = 0
        if correct_count >= 4:
            prize = prizes[correct_count - 4]  # Adjust to prize tiers (4 correct -> 1st tier)
        
        total_winnings += prize
        results.append((ticket, correct_count, prize))
    
    return results, total_winnings

# Function to simulate multiple weeks of the lottery
def simulate_multiple_weeks(tickets, total_numbers, numbers_picked, prizes, weeks):
    weekly_winnings_list = []  # List to store winnings for each week
    
    for week in range(weeks):
        # Randomize the winning numbers
        winning_numbers = run_lottery_draw(total_numbers, numbers_picked)  # Use the function designed for the draw
        print(f"Week {week + 1} results:")
        print(f"Winning numbers: {winning_numbers}")
        
        # Check the results for all tickets
        results, weekly_winnings = check_results(tickets, winning_numbers, prizes)
        weekly_winnings_list.append(weekly_winnings)  # Store weekly winnings
        print(f"Total winnings this week: {weekly_winnings}")
        print("-" * 30)
    
    # Calculate total winnings at the end
    total_winnings = sum(weekly_winnings_list)
    return total_winnings, weekly_winnings_list


# Main function to tie everything together
def main():
    total_numbers, numbers_picked, ticket_price, prizes = set_lottery_rules()
    tickets = buy_tickets(total_numbers, numbers_picked, ticket_price)
    
    # Print the tickets purchased
    print("\nYour tickets:")
    for ticket in tickets:
        print(ticket)
    
    weeks = int(input("How many weeks would you like to simulate? "))
    
    # Simulate the lottery
    total_winnings, weekly_winnings_list = simulate_multiple_weeks(tickets, total_numbers, numbers_picked, prizes, weeks)
    
 
    
    print(f"\nTotal winnings after {weeks} week(s): {total_winnings} $")
    
    # Calculate net profit or loss
    total_spent = len(tickets) * ticket_price * weeks
    net_result = total_winnings - total_spent
    print(f"Total spent: {total_spent} $")
    print(f"Net result after {weeks} week(s): {net_result} $")

# Run the program
if __name__ == "__main__":
    main()


print("\nCoded by NAYREED")