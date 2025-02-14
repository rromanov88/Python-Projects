# Enhanced Bank Account Management System

# 🏦 Data Structures to Store Information
account_holders = []  # Account names
balances = []         # Account balances
transaction_histories = []  # Account transaction logs
loans = []            # Account loan details

MAX_LOAN_AMOUNT = 10.000
INTEREST_RATE = 0.03

def display_menu():
    """Main menu for banking system."""
    print("\n🌟 Welcome to Enhanced Bank System 🌟")
    print("1️⃣ Create Account")
    print("2️⃣ Deposit Money")
    print("3️⃣ Withdraw Money")
    print("4️⃣ Check Balance")
    print("5️⃣ List All Accounts")
    print("6️⃣ Transfer Funds")
    print("7️⃣ View Transaction History")
    print("8️⃣ Apply for Loan")
    print("9️⃣ Repay Loan")
    print("🔟 Identify Credit Card Type")
    print("0️⃣ Exit")


def create_account():
    """Create a new account."""
    account_name = input("Enter your name:\n")
    if not account_name.isalpha():
        print("Invalid name. Please try again.")
    elif account_name in account_holders:
        print("Username already exists. Please choose a different username.")
    elif account_name not in account_holders:
        initial_balance = 0
        initial_loan = 0
        account_holders.append(account_name)
        balances.append(initial_balance)
        loans.append(initial_loan)


def deposit():
    """Deposit money into an account."""
    account_name = input("Enter the name associated with your account:\n")
    if account_name in account_holders:
        deposit_amount = int(input("Enter the amount to deposit:\n"))
        if deposit_amount <= 0:
            print("Invalid amount to deposit. Please try again.")
        else:
            balances[account_holders.index(account_name)] += deposit_amount
            transaction_histories.append(f"On this day - 14.02.2025, {account_name} deposited {deposit_amount}$.")
    else:
        print("Invalid account name. Please try again.")


def withdraw():
    """Withdraw money from an account."""
    account_name = input("Enter the name associated with your account:\n")
    if account_name in account_holders:
        withdraw_amount = int(input("Enter the amount to withdraw:\n"))
        if withdraw_amount <= 0:
            print("Invalid amount to withdraw. Please try again.")
        else:
            if withdraw_amount <= balances[account_holders.index(account_name)]:
                balances[account_holders.index(account_name)] -= withdraw_amount
                transaction_histories.append(f"On this day - 14.02.2025, {account_name} withdrawed {withdraw_amount}$.")
            else:
                print("Insufficient funds!")
    else:
        print("Invalid account name. Please try again.")


def check_balance():
    """Check balance of an account."""
    account_name = input("Enter the name associated with your account:\n")
    if account_name in account_holders:
        print(f"Balance for {account_name}: {balances[account_holders.index(account_name)]}$")
    else:
        print("Invalid account name. Please try again.")


def list_accounts():
    """List all account holders and details."""
    for account in account_holders:
        print(f"Account name - {account} : Account balance: + {balances[account_holders.index(account)]}$ : Account loan: - {loans[account_holders.index(account)]}$")


def transfer_funds():
    """Transfer funds between two accounts."""
    account_name = input("Enter the name associated with your account:\n")
    recipient_name = input("Enter the name of the recipient:\n")
    if account_name not in account_holders or recipient_name not in account_holders:
        return "Invalid account name. Please try again."
    money_to_transfers = int(input("Enter the amount you want to transfer:\n"))
    if money_to_transfers <= 0:
        return "Invalid amount to transfer. Please try again."
    elif money_to_transfers > balances[account_holders.index(account_name)]:
        return "Insufficient funds!"
    else:
        balances[account_holders.index(account_name)] -= money_to_transfers
        balances[account_holders.index(recipient_name)] += money_to_transfers
        transaction_histories.append(f"On this day - 14.02.2025, {account_name} transferred {money_to_transfers}$ to {recipient_name}.")
        print(f"{money_to_transfers}$ were transfered from the account of {account_name} to the account of {recipient_name}")


def view_transaction_history():
    """View transactions for an account."""
    name_in_question = input("Enter the name associated with your account, in order to see transaction history:\n")
    if name_in_question not in account_holders:
        print("Invalid account name. Please try again.")
    else:
        print(f"Transaction history for {name_in_question}:")
        for transaction in transaction_histories:
            if name_in_question in transaction:
                print(f"{transaction}")


def apply_for_loan():
    """Allow user to apply for a loan."""
    account_name = input("Enter the name associated with your account:\n")
    if account_name not in account_holders:
        return "Invalid account name. Please try again."
    print(f"The maximum loan amount that you can apply for is {MAX_LOAN_AMOUNT}$.")
    loan_amount = int(input("Enter the amount you want to apply for:\n"))
    if loan_amount > MAX_LOAN_AMOUNT:
        return f"The maximum loan amount that you can apply for is {MAX_LOAN_AMOUNT}$."
    loans[account_holders.index(account_name)] += loan_amount
    balances[account_holders.index(account_name)] += loan_amount
    transaction_histories.append(f"On this day - 14.02.2025, {account_name} applied for {loan_amount}$ and was approved.")
    print(f"Your application for loan - {loan_amount}$ was approved and the interest rate is: {loan_amount * INTEREST_RATE:.2f}$")


def repay_loan():
    """Allow user to repay a loan."""
    account_name = input("Enter the name associated with your account:\n")
    if account_name not in account_holders:
        return "Invalid account name. Please try again."
    repay_amount = int(input("Enter the amount you want to repay for your loan"))
    if repay_amount <= 0:
        return "Invalid amount to transfer. Please try again."
    loans[account_holders.index(account_name)] -= repay_amount
    balances[account_holders.index(account_name)] -= repay_amount
    transaction_histories.append(f"On this day - 14.02.2025, {account_name} repaid {repay_amount}$.")


def identify_card_type():
    """Identify type of credit card."""
    credit_card_number = input("Please enter the number of your Credit Card in format: xxxx xxxx xxxx xxxx\n")
    if 19 > len(credit_card_number) > 19:
        print("Invalid number provided!")
    elif credit_card_number.startswith('4'):
        print("Your credit card is - Visa")
    elif credit_card_number.startswith(('51', '52', '53', '54', '55')):
        print("Your credit card is - MasterCard")
    elif credit_card_number.startswith(('34', '37')):
        print("Your credit card is - American Express")
    else:
        print("Your credit card is - Other (unidentified)")


def main():
    """Run the banking system."""
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            # Map choices to functions
            if choice == 1:
                create_account()
            elif choice == 2:
                deposit()
            elif choice == 3:
                withdraw()
            elif choice == 4:
                check_balance()
            elif choice == 5:
                list_accounts()
            elif choice == 6:
                transfer_funds()
            elif choice == 7:
                view_transaction_history()
            elif choice == 8:
                apply_for_loan()
            elif choice == 9:
                repay_loan()
            elif choice == 10:
                identify_card_type()
            elif choice == 0:
                print("Goodbye! 👋")
                break

        except ValueError:
            print("❌ Invalid choice. Try again!")


if __name__ == "__main__":
    main()
