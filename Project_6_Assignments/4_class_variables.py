# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "XYZ Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display_bank_name(self):
        print(f"Bank Name: {self.bank_name}")

bank = Bank()
bank.display_bank_name()

Bank.change_bank_name("ABC Bank")
bank.display_bank_name()

bank2 = Bank()
bank2.display_bank_name()

# Output:
# Bank Name: XYZ Bank
# Bank Name: ABC Bank
# Bank Name: ABC Bank