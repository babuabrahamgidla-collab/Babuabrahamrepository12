print("Hello World")
print("Hello OOPs World 10sep")
import datetime
import csv

class PurchaseOrder:
    def __init__(self, po_number, supplier):
        self.po_number = po_number
        self.supplier = supplier
        self.purchaseorder_type = None
        self.items = {}
        self.status = "Draft"

        self.supplier_list = ["ABC", "EFG", "PQR", "XYZ", "123books"]
        self.reject_reasons = []

        self.grand_total = 0
        self.tax_component = 0
        self.po_value = 0
        self.age_in_days =0

        self.status_List = [
            "Draft", "Submitted", "Routed up",
            "Auto Approved", "Manager Approved", "Closed"
        ]

        self.message_to_manager = []
        self.alerts = []
        self.age_in_days = 0

        self.approval_history = {}

        self.check_supplier_flag = False
        self.check_items_flag = False
        self.check_delivery_date_flag = False
        self.all_items_received = False
        self.invoice_paid = False
        
        self.po_severity_lelve = None
        self.manager_override = False
        self.constraints_violated = False
        


    # -----------------------------
    # ITEM MANAGEMENT
    # -----------------------------
    def add_or_update_items(self, item_number, description, quantity, unit_price, currency, delivery_date):
        # Convert delivery_date string to datetime.date
        if isinstance(delivery_date, str):
            delivery_date = datetime.datetime.strptime(delivery_date, "%Y-%m-%d").date()
        self.items[item_number] = {
            "Item_description": description,
            "Quantity": quantity,
            "Unit Price": unit_price,
            "Currency": currency,
            "Line Total": quantity * unit_price,
            "Delivery Date": delivery_date
        }
        print(f"{item_number}: is added successfully")

    def remove_items(self, item_number):
        if item_number in self.items:
            del self.items[item_number]
            print(f"Item {item_number} removed successfully.")
        else:
            print(f"Item {item_number} does not exist.")


    # -----------------------------
    # VALIDATION CHECKS
    # -----------------------------
    def check_supplier(self):
        self.check_supplier_flag = True
        if self.supplier not in self.supplier_list:
            self.status = "Rejected"
            self.reject_reasons.append("Supplier is not in the Supplier list")
            print("Supplier is not in the supplier list, PO cannot be submitted")
            self.check_supplier_flag = False

    def check_items(self):
        self.check_items_flag = True
        for item_number, item_data in self.items.items():
            if item_data["Line Total"] < 0:
                print(f"For {item_number} the line total is negative")
                self.check_items_flag = False
                return

    def check_delivery_date(self):
        today = datetime.date.today()
        self.check_delivery_date_flag = True
        for item_number, item_data in self.items.items():
            if item_data["Delivery Date"] < today:
                print(f"For {item_number} the delivery date is in the past")
                self.check_delivery_date_flag = False
                return


    # -----------------------------
    # SUBMIT WORKFLOW
    # -----------------------------
    def submit_PO(self):
        # Run validations
        self.check_items()
        self.check_supplier()
        self.check_delivery_date()

        if not self.check_supplier_flag:
            print("Supplier is not in the approved supplier list")
            return

        if not self.check_items_flag:
            print("Item total is negative")
            return

        if not self.check_delivery_date_flag:
            print("Item delivery date is in the past")
            return

        if len(self.items) == 0:
            print("There are no item lines in the PO, hence cannot be submitted")
            return

        # All checks passed
        self.status = "Submitted"
        timestamp_submitted = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.approval_history["Submitted"] = timestamp_submitted
        print("PO submitted successfully.")


    # -----------------------------
    # CALCULATIONS
    # -----------------------------
    def grand_total_calculation(self):
        self.grand_total = 0
        for mykey, myvalue in self.items.items():
            line_total = myvalue["Line Total"]

            # Currency conversion (USD/EUR → CAD)
            if myvalue["Currency"] == "USD":
                line_total = line_total * (1 / 0.78)
            elif myvalue["Currency"] == "EUR":
                line_total = line_total * (1 / 0.68)

            self.grand_total += line_total

        # Discount if >= 100
        if self.grand_total >= 1000:
            self.grand_total *= 0.95
        print(f"Grand total of the PO is calculated as {self.grand_total:.2f}")    
        if self.grand_total<=1000:
            self.po_severity_lelve = "Low"            
        elif self.grand_total<=2000:
                self.po_severity_lelve = "Normal"
        elif self.grand_total<=5000:
                self.po_severity_lelve = "High"
        else:           
            self.po_severity_lelve = "Super"
     
    def calculation_value_of_po(self):
        tax_rate = 13
        self.tax_component = self.grand_total * (tax_rate / 100)
        self.po_value = self.grand_total + self.tax_component
        print(f"PO value is calculated as {self.po_value:.2f}")
        


    # -----------------------------
    # ROUTING & APPROVAL WORKFLOW
    # -----------------------------
    def send_reminder_to_manager(self):
        if self.status == "Routed up":
            self.message_to_manager.append("Please review and approve the PO")
            
    def override_constraints(self):
        self.manager_override = True
        print("Manager override activated — constraints will be ignored.")
    
    def Manager_review(self):
        self.constraints_violated = False       

        # Check item-level constraints
        for mykey, myvalue in self.items.items():
            if myvalue["Quantity"] > 100 or myvalue["Line Total"] > 1000:
                print("Warning: Item constraints violated (quantity or line total too high).")
                self.constraints_violated = True

        # Check grand total constraint
        if self.grand_total >= 10000:
            print("Warning: Grand total exceeds manager approval limit.")
            self.constraints_violated = True

        # If constraints violated AND no override → do NOT approve yet
        if self.constraints_violated and not self.manager_override:
            print("Manager review completed. PO requires override to approve.")
            return

        # If override is ON → approve
        self.status = "Manager Approved"
        print("The PO is Approved by the manager.")
        timestamp_manager_approved = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.approval_history["Manager Approved"] = timestamp_manager_approved
    
    def approvepo(self):
        if self.status not in self.status_List:
            return

        if self.status == "Submitted" and self.po_value <= 10000:
            self.status = "Auto Approved"
            print("PO is Auto Approved")
            self.approval_history["Auto Approved"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        elif self.status == "Submitted" and self.po_value > 10000:
            self.status = "Routed up"
            self.send_reminder_to_manager()
            
    def pay_invoice(self):# in simulation the user should execute this method before he can execute close method to close the PO
        self.all_items_received = True
        self.invoice_paid = True

    def close(self):
            if self.status not in ["Auto Approved", "Manager Approved"]:                
                self.alerts.append("Only approved POs can be closed")
                return
            if self.all_items_received == True and self.invoice_paid == True:                
                self.status = "Closed"
                self.approval_history["Closed"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
            else:
                return
    # -----------------------------
    # SUMMARY
    # -----------------------------
    def summary_po(self):
        print(
            f"PO Number: {self.po_number}\n"
            f"Supplier: {self.supplier}\n"
            f"Items: {len(self.items)}\n"
            f"Status: {self.status}\n"
            f"PO Value: {self.po_value}\n"
            f"Age (days): {self.age_in_days}"
        )


class MatPO(PurchaseOrder):
    def __init__(self, po_number, supplier):
        super().__init__(po_number, supplier)
        self.purchaseorder_type = None
    def show_details(self):
        print(f"PO number is {self.po_number}, the supplier is {self.supplier}, purchase order type is {self.purchaseorder_type} the status of po is {self.status}")


class ServicePO(PurchaseOrder):
    def __init__(self, po_number, supplier):
        super().__init__(po_number, supplier)
        self.purchaseorder_type = None
    def show_details(self):
        print(f"PO number is {self.po_number}, the supplier is {self.supplier}, purchase order type is {self.purchaseorder_type} the status of po is {self.status}")


class EmergencyPO(PurchaseOrder):
    def __init__(self, po_number, supplier):
        super().__init__(po_number, supplier)
        self.purchaseorder_type = None
    def show_details(self):
        print(f"PO number is {self.po_number}, the supplier is {self.supplier}, purchase order type is {self.purchaseorder_type} the status of po is {self.status}")

class CapitalPO(PurchaseOrder):
    def __init__(self, po_number, supplier):
        super().__init__(po_number, supplier)
        self.purchaseorder_type = None
    def show_details(self):
        print(f"PO number is {self.po_number}, the supplier is {self.supplier}, purchase order type is {self.purchaseorder_type} the status of po is {self.status}")        
        
       
class POHub2:
    def __init__(self):
        self.po_list=[]
        
    def add_po_to_hub(self, po):
        self.po_list.append(po)
        
    def list_pos_in_hub(self):
        for po in self.po_list:
            print(f"{po}")
    def show_po_details(self):
        for po in self.po_list:
            po.summary_po()
            
    def sort_by_value(self):
        self.po_list.sort(
            key=lambda po: po.po_value, 
            reverse=True
        )

         
    def sort_by_severity_lelve(self):
           self.po_list.sort(
               key=lambda ko:ko.ko_severity_level,
               reverse=True
           )
            
materialpo1 = MatPO("MPO001", "ABC")
materialpo1.add_or_update_items(1, "New Short Stories", 10, 12, "CAD", "2026-10-11")
materialpo1.add_or_update_items(2, "New Novels", 10, 30, "CAD", "2026-10-11")
materialpo1.add_or_update_items(3, "New Social Stories", 10, 22, "USD", "2026-10-11")
materialpo1.add_or_update_items(4, "New Ethinic Stories", 10, 40, "EUR", "2026-10-11")
materialpo1.add_or_update_items(5, "New Mythology Stories", 10, 50, "EUR", "2026-10-11")

servicepo1 = ServicePO("SPO001", "XYZ")
servicepo1.add_or_update_items(1, "Security Services", 1, 1200, "CAD", "2026-10-11")
servicepo1.add_or_update_items(2, "Catering Services", 30, 1000, "CAD", "2026-10-11")
servicepo1.add_or_update_items(3, "Logistics Services", 8, 500, "USD", "2026-10-11")
servicepo1.add_or_update_items(4, "New Event Management Services", 1, 10000,"EUR", "2026-10-11")
servicepo1.add_or_update_items(5, "New Audit Services", 2, 5000, "EUR", "2026-11-11")

materialpo1.submit_PO()
materialpo1.grand_total_calculation()
materialpo1.calculation_value_of_po()
materialpo1.approvepo()
servicepo1.submit_PO()
servicepo1.grand_total_calculation() 
servicepo1.calculation_value_of_po()
servicepo1.approvepo()
servicepo1.Manager_review()


newhub = POHub2()

            
            
