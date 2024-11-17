**Lottery Simulator**\n
Welcome to the Lottery Simulator! This Python-based program allows you to simulate the lottery and track the outcomes of multiple lottery tickets over several weeks. You can customize the lottery rules, buy tickets, and observe the results of each weekly draw.

**Features**
Lottery Setup: Define the total number of available numbers, the number of numbers to be picked per ticket, the ticket price, and the prize tiers.
Ticket Purchase: Buy multiple lottery tickets. You can either manually select the numbers or have the program randomly generate them for you.
Lottery Draw: The program will randomize the winning numbers for each week and check them against your tickets.
Weekly Simulations: Simulate the lottery over multiple weeks, track your winnings, and get a total summary of the net outcome after all weeks.
Prize Tiers: Set up different prize tiers for different numbers of correct guesses, such as:
7 correct numbers: Jackpot prize.
6 correct numbers: Smaller prize.
5 correct numbers: Even smaller prize.
4 correct numbers: Smallest prize.

**Setup**
Prerequisites
You will need Python 3 to run this project. You can install it from the official website: python.org

Installing
Clone the repository or download the script:

bash
Copy code
git clone https://github.com/RA-Nayreed/lottery-simulator.git
Make sure all dependencies are installed (though for this basic version, there are no external libraries required beyond Python’s standard library).

Usage
Running the Program
Run the lottery_simulator.py script:

Copy code
python lottery_simulator.py
Follow the interactive prompts:

Enter the total number of available numbers.
Enter the number of numbers you want to pick per ticket.
Enter the ticket price.
Define the prize amounts for each tier (starting from 7 correct down to 4 correct).
Buy tickets: Choose between manually selecting numbers or having the program randomize them for you.
Simulate the lottery: You can simulate the lottery for as many weeks as you like.
Example
Here’s how a typical interaction with the program might look:

yaml
Copy code
Welcome to the Lottery Simulator!
Amount of numbers: 40
Selected numbers: 7
Prize tiers: 4
Enter the prize amounts for each tier, starting from 7 correct down to 4 correct:
Enter the prize for 7 correct numbers: 1000000
Enter the prize for 6 correct numbers: 5000
Enter the prize for 5 correct numbers: 100
Enter the prize for 4 correct numbers: 10

How many tickets would you like to buy? 2
Would you like to fill ticket 1 manually or randomize? (m/r): r
Would you like to fill ticket 2 manually or randomize? (m/r): r

Your tickets:
{1, 3, 5, 7, 10, 14, 21}
{2, 4, 6, 8, 9, 12, 15}

How many weeks would you like to simulate? 3

Week 1 results:
Winning numbers: {3, 5, 7, 8, 9, 10, 12}
Total winnings this week: 100 units
------------------------------
Week 2 results:
Winning numbers: {1, 2, 3, 4, 5, 6, 7}
Total winnings this week: 50 units
------------------------------
Week 3 results:
Winning numbers: {2, 4, 6, 8, 10, 12, 14}
Total winnings this week: 0 units

Total winnings after 3 week(s): 150 units
Total spent: 6 units
Net result after 3 week(s): 144 units

**Contributing**
If you would like to contribute to this project, feel free to fork the repository, create a branch, and submit a pull request with your proposed changes. If you encounter any issues, open an issue and I'll get back to you as soon as possible!



Coded by Nayreed
