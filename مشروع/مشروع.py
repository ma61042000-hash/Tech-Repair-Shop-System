
from abc import ABC, abstractmethod

#Requirement 1: Blueprint 
class RepairService(ABC):
    def __init__(self, service_name, labor_cost):
        self.__service_name = service_name
        self.__labor_cost = labor_cost


    def get_service_name(self):
        return self.__service_name

    def get_labor_cost(self):
        return self.__labor_cost

    
    def set_labor_cost(self, cost):
        if cost > 0:
            self.__labor_cost = cost
        else:
            print(" Invalid labor cost!")

    @abstractmethod
    def calculate_service_cost(self):
        pass

    @abstractmethod
    def display_service_info(self):
        pass


#Requirement 2: Specialization 
class HardwareRepair(RepairService):
    def __init__(self, service_name, labor_cost, part_cost):
        super().__init__(service_name, labor_cost)
        self.part_cost = part_cost

    def calculate_service_cost(self):
 # Hardware: labor + parts + 10% tax
        return self.get_labor_cost() + self.part_cost + (0.1 * self.part_cost)

    def display_service_info(self):
        print(f" {self.get_service_name()} | Labor: {self.get_labor_cost()} | Parts: {self.part_cost}")


class SoftwareRepair(RepairService):
    def __init__(self, service_name, labor_cost, license_fee=5):
        super().__init__(service_name, labor_cost)
        self.license_fee = license_fee

    def calculate_service_cost(self):
        # Software: labor + flat license fee
        return self.get_labor_cost() + self.license_fee

    def display_service_info(self):
        print(f" {self.get_service_name()} | Labor: {self.get_labor_cost()} | License Fee: {self.license_fee}")


#Requirement 4: Smart Behavior 
class CustomerInvoice:
    def __init__(self):
        self.repairs = []

    def add_repair(self, repair):
        self.repairs.append(repair)
        print(f" Added {repair.get_service_name()} to invoice.")

    def view_invoice(self):
        if not self.repairs:
            print(" Invoice is empty.")
        else:
            print("\n Current Invoice:")
            for idx, repair in enumerate(self.repairs, start=1):
                print(f"[{idx}] {repair.get_service_name()} - Base Labor: {repair.get_labor_cost()}")

    def print_final_bill(self):
        if not self.repairs:
            print(" No repairs added yet.")
            return
        total = 0
        print("\n Final Bill:")
        for repair in self.repairs:
            cost = repair.calculate_service_cost()
            print(f"- {repair.get_service_name()} → ${cost:.2f}")
            total += cost
        print(f"\n TOTAL: {total:.2f}")


#Requirement 5: Terminal Interaction 
def main():

    services = {
        "1": HardwareRepair("Screen Replacement", 50, 100),
        "2": HardwareRepair("Battery Replacement", 40, 80),
        "3": SoftwareRepair("OS Installation", 30),
        "4": SoftwareRepair("Virus Removal", 25)
    }

    invoice = CustomerInvoice()

    while True:
        print("\n=== Tech Repair Shop Menu ===")
        print("[1] View Services")
        print("[2] Add to Invoice")
        print("[3] View Invoice")
        print("[4] Print Final Bill")
        print("[5] Exit")

        choice = input(" Enter your choice: ")

        if choice == "1":
            print("\n Available Services:")
            for key, service in services.items():
                print(f"[{key}] ", end="")
                service.display_service_info()

        elif choice == "2":
            service_id = input(" Enter Service ID: ")
            if service_id in services:
                invoice.add_repair(services[service_id])
            else:
                print(" Invalid Service ID!")

        elif choice == "3":
            invoice.view_invoice()

        elif choice == "4":
            invoice.print_final_bill()

        elif choice == "5":
            print(" Exiting system. Goodbye!")
            break

        else:
            print(" Invalid input. Please enter a number between 1–5.")


if __name__ == "__main__":
    main()

