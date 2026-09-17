from datetime import datetime
import csv
print("Hello World")
print("Hello OOPs World")
print("07 Sep. afternoon sesseion")

class PurchaseOrder:    
    def __init__(self, purchaseorder_number, supplier):
        self.purchaseorder_number= purchaseorder_number
        self.purchaseordertype = None
        self.supplier = supplier
        self.status = "Draft"
        self.line_items = []
        self.total_amount =0       
        self.grand_total = 0
        self.alerts = []
        self.tax_rate = 0.13
        self.tax_amount = 0
        self.discount = 0
        self.grand_total = 0
        self.currency = "CAD"
        self.conversion = 1.0
        self.converted_total = 0
        self.approval_history = []
        self.severity = "Low"
        self.creation_date = datetime.now()
        self.age_in_days = 0
        
       
    def add_items(self, itemnumber, itemdescription, quantity, unitprice):
        amount = unitprice*quantity
        self.line_items.append((itemnumber, itemdescription, quantity, unitprice, amount))
        self.total_amount += amount 
               
    def submit(self):
            if self.status=="Rejected":
                self.alerts.append("Cannot submit a Rejected PO")
                return
            if self.status =="Closed":
                self.alerts.append("Cannot submit a closed PO")
                return
            if len(self.line_items)==0:
                self.alerts.append("A submitted PO should have at least one item")
                return         
               
            self.status = "Submitted"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.approval_history.append(f"PO submitted on {timestamp}")
            
    def calculatetotal(self):
        return self.total_amount

           
    def approve(self):
        # Rule 1: Cannot approve a rejected PO
        if self.status == "Rejected":
            self.alerts.append("Cannot approve a rejected PO")
            return

        # Rule 2: Cannot approve a closed PO
        if self.status == "Closed":
            self.alerts.append("Cannot approve a closed PO")
            return

        # Rule 3: Cannot approve a zero-dollar PO
        if self.total_amount == 0:
            self.alerts.append("Cannot approve a zero dollar PO")
            return

        # Rule 4: Cannot approve a PO with no items
        if len(self.line_items) == 0:
            self.alerts.append("Cannot approve a PO with no items")
            return

        # If all rules pass → approve
        self.status = "Approved"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.approval_history.append(f"Approved on {timestamp}")
            
    def rejectPO(self, reason):
        self.status = "Rejected"
        self.alerts.append(reason)
    
    def close(self):
        if self.status != "Approved":
            self.alerts.append("Only approved POs can be closed")
        else:
            self.status = "Closed"
            
    def show_summary(self):
        print("----------------------------------------------------------------------------")
        print(f"PO number                       {self.purchaseorder_number}")
        print(f"Supplier                        {self.supplier}")
        print(f"Type                            {self.purchaseordertype}")
        print(f"Status                          {self.status}")
        print(f"Total amount                    {self.total_amount}")
        print(f"Grand Total                     {self.grand_total}")
        print(f"Converted Total                 {self.converted_total}")        
        print(f"Line items                      {len(self.line_items)}")
        print(f"Severity                        {self.severity}")
        print(f"PO age (days)                   {self.age_in_days}")
        print(f"Approval history:               {self.approval_history} ") 
        print(f"Alerts :                        {self.alerts} ")
        print("----------------------------------------------------------------------------")
                      
   
    def validate(self):
        if not self.supplier:
            self.alerts.append("Supplier name is missing")
        if len(self.line_items) ==0:
            self.alerts.append("There are no items")
        if self.total_amount < 0:
            self.alerts.append("Total amount cannot be less than zero") 
        
        for item in self.line_items:
            if item[3]<0:
               self.alerts.append("Item unit price cannot be negative")
               
    def update(self):
        self.validate()      
        self.tax_amount = self.total_amount * self.tax_rate

        if self.total_amount >= 10000:
            self.discount = self.total_amount * 0.05
        else:
            self.discount = 0

        self.grand_total = self.total_amount + self.tax_amount - self.discount
        
        if self.total_amount <= 5000:
            self.severity = "Low"
        elif self.total_amount < 10000:
            self.severity = "Medium"
        elif self.total_amount<20000:
            self.severity = "High"
        else:
            self.severity = "Critical"
            self.alerts.append("Critical PO: requires CFO's attention")
            
        current_time = datetime.now()
        time_difference = current_time - self.creation_date
        self.age_in_days = time_difference.days
        
        if self.status == "Submitted" and self.age_in_days>7:
            self.alerts.append("PO has been submitted for more than 7 days - overdue for approval")
        if self.status == "Approved" and self.age_in_days>30:
                    self.alerts.append("Approved PO is open for more than 30 days - overdue for closure")
                                        
        
    def convert_currency(self, new_currency):
        self.conversion = 1.0

        if new_currency == "USD":
            self.conversion = 0.75
        elif new_currency == "EUR":
            self.conversion = 0.68

        self.currency = new_currency
        self.converted_total = self.grand_total * self.conversion
        
    def status_update(self, new_status):
        allowed = ["Draft", "Submitted", "Approved", "Rejected", "Closed"]
        if new_status in allowed:
            self.status = new_status
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.approval_history.append(f"Status changed to {new_status} on {timestamp}")
        else:
            self.alerts.append(f"{new_status} is not in the allowed status list")

class MaterialPO(PurchaseOrder):
    def __init__(self, purchaseorder_number, supplier):
        super().__init__(purchaseorder_number, supplier)
        self.purchaseordertype = "Material"
        
    def approve(self):
        if self.total_amount > 5000:
            self.alerts.append("Amount over 5000 and hence needs Director approval")
        else:
            self.status = "Approved"
        timestamp = datetime.now().strftime ("%Y-%m-%d %H:%M:%S")
        self.approval_history.append(f"Material PO is approved on {timestamp}")
        
    
class ServicePO(PurchaseOrder):
        
    def __init__(self, purchaseorder_number, supplier):
        super().__init__(purchaseorder_number, supplier)
        self.purchaseordertype = "Service"
        
    def approve(self):
        if len(self.line_items) ==0:
            self.alerts.append("Service PO must have at least one service line")
        else:
            self.status = "Approved"
        timestamp = datetime.now().strftime ("%Y-%m-%d %H:%M:%S")
        self.approval_history.append(f"Service PO is approved on {timestamp}")    
    
class CapitalPO(PurchaseOrder):

    def __init__(self, purchaseorder_number, supplier):
        super().__init__(purchaseorder_number, supplier)
        self.purchaseordertype = "Capital"
        
    def approve(self):
        if self.total_amount > 20000:
            self.alerts.append("The PO value is over 20000, needs CFO approval")
        else:
            self.status = "Approved"
        timestamp = datetime.now().strftime ("%Y-%m-%d %H:%M:%S")
        self.approval_history.append(f"Capital PO is approved on {timestamp}") 
            
class EmergencyPO(PurchaseOrder):
    def __init__(self, purchaseorder_number, supplier):
        super().__init__(purchaseorder_number, supplier)
        self.purchaseordertype = "Emergency"
        
    def approve(self):
        if len(self.line_items)==0:
            self.alerts.append("Emergency PO must have at least one item")
        else:
            self.status="Approved"
        timestamp = datetime.now().strftime ("%Y-%m-%d %H:%M:%S")
        self.approval_history.append(f"Emergency PO is approved on {timestamp}")
        
class POHub:
    def __init__(self):
        self.poslist = []
        
    def add_PO(self,po):
        self.poslist.append(po)
        
    def list_pos(self):
        for po in self.poslist:
            po.show_summary()
                
    def show_alerts(self):
            for thispo in self.poslist:
                for thealert in thispo.alerts:
                    print(f" For the {thispo.purchaseorder_number}: the alert is {thealert}")
    
    def run_updates(self):
        for thispo in self.poslist:
            thispo.update()
            
    def sort_by_severity(self):
        severity_rank = {"Critical":4, "High":3, "Medium":2, "Low":1}
        self.poslist.sort(
            key=lambda po: severity_rank.get(po.severity,0), reverse= True
        )
    
    def sort_by_age(self):
        self.poslist.sort(
            key=lambda po: po.age_in_days, 
            reverse=True
        )
        
    def sort_by_amount(self):
        self.poslist.sort(
            key=lambda po: po.total_amount, 
            reverse=True
        )
    def sort_by_supplier(self):
        self.poslist.sort(
            key=lambda po: po.supplier.lower()
        )
    
    def dashboard (self):
        print("\n=====================Purchase Order Dashboard====================")
        self.sort_by_severity()
        for thispo in self.poslist:            
            thispo.show_summary()
            if thispo.severity == "Critical":
                print("⚠️  CRITICAL PO — Immediate attention required!")

        print("=================================================================\n")
   
    
    def export_to_csv(self, filename):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            
            writer.writerow(["PO Number","Supplier","Type","Status","Total amount","Grand Total", "Severity", "Age in days", "Line Items", "Alerts", "Approval History"])
            
            for po in self.poslist:
                writer.writerow([
                po.purchaseorder_number,
                po.supplier,
                po.purchaseordertype,
                po.status, 
                po.total_amount, 
                po.grand_total, 
                po.severity,
                po.age_in_days,
                len(po.line_items),
                "; ".join(po.alerts), 
                "; ".join(po.approval_history)
            ])

            
matpoobj = MaterialPO(1001, "ABC Suppliers")
servpoobj = ServicePO(2001, "BBC Services")
emerpoobj = EmergencyPO(3001, "CBC ExpressSuppliers") 
matpoobj2 = MaterialPO(1002, "XYZ Suppliers")
servpoobj2 = ServicePO(2002, "YYZ Services")
emerpoobj2 = EmergencyPO(3002, "XXY Suppliers") 
matpoobj.add_items(1, "Python Basics", 30, 5 )
matpoobj.add_items(2, "Java Programming Basics", 40, 6 )
matpoobj.add_items(3, "C++ Programming Basics", 50, 4 )
matpoobj.add_items(4, "AI Fundamentals ", 90, 10 )
matpoobj.add_items(5, "LLM Basics", 100, 5 )

matpoobj2.add_items(1, "Thermodynamics Text", 300, 10 )
matpoobj2.add_items(2, "Heat and Material Balance", 200, 6 )
matpoobj2.add_items(3, "Fluid Mechanics", 150, 4 )
matpoobj2.add_items(4, "Heat Transfer Fundamentals ", 190, 10 )
matpoobj2.add_items(5, "Mass Transfer Fundamentals", 300, 5 )

matpoobj.submit()
#matpoobj.show_summary()
matpoobj.approve()
matpoobj.validate()
#matpoobj.show_summary()

matpoobj2.submit()
#matpoobj2.show_summary()
matpoobj2.approve()
matpoobj2.validate()
#matpoobj2.show_summary()

servpoobj.add_items(1, "Catering", 30, 5 )
servpoobj.add_items(2, "Security", 40, 6 )
servpoobj.add_items(3, "Local Logistics", 5, 100 )
servpoobj.add_items(4, "Event Programming", 2, 1000 )
servpoobj.submit()
#servpoobj.show_summary()
servpoobj.approve()
servpoobj.validate()
#servpoobj.show_summary()

servpoobj2.add_items(1, "Jantorial", 30, 5 )
servpoobj2.add_items(2, "House Keeping ", 40, 6 )
servpoobj2.add_items(3, "Stationary", 5, 100 )
servpoobj2.add_items(4, "Event Lighting and Sound", 2, 1000 )
servpoobj2.submit()
#servpoobj2.show_summary()
servpoobj2.approve()
servpoobj2.validate()
#servpoobj2.show_summary()

emerpoobj2.add_items(1, "Statistics Text", 300, 1 )
emerpoobj2.add_items(2, "Business Math Text", 200, 2 )
emerpoobj2.add_items(3, "Finance Calculations", 150, 3 )
emerpoobj2.add_items(4, "Policy Analysis", 190, 2 )
emerpoobj2.add_items(5, "Marketing Fundamentals", 300, 1 )

emerpoobj.add_items(1, "Business Communications", 300, 1 )
emerpoobj.add_items(2, "Operations Theory Text", 200, 2 )
emerpoobj.add_items(3, "Firm and Its Finance", 150, 3 )
emerpoobj.add_items(4, "Firm and Its Ecconomics Analysis", 190, 2 )
emerpoobj.add_items(5, "Marketing Fundamentals", 300, 1 )

emerpoobj.submit()
#emerpoobj.show_summary()
emerpoobj.approve()
emerpoobj.validate()
#emerpoobj.show_summary()

emerpoobj2.submit()
#emerpoobj2.show_summary()
emerpoobj2.approve()
emerpoobj2.validate()
#emerpoobj2.show_summary()



mypohub = POHub()
mypohub.add_PO(matpoobj)
mypohub.add_PO(matpoobj2)
mypohub.add_PO(servpoobj)
mypohub.add_PO(servpoobj2)
mypohub.add_PO(emerpoobj)
mypohub.add_PO(emerpoobj2)
#mypohub.list_pos()
mypohub.show_alerts()
mypohub.run_updates()
mypohub.sort_by_severity()
#mypohub.dashboard()
mypohub.export_to_csv("myfile")
