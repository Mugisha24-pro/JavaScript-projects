# =============================================
# Full Restaurant System GUI with View Receipts
# =============================================

import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
from datetime import datetime, date
import os

DB_NAME = "restaurant.db"

# ----------------- DATABASE FUNCTIONS -----------------
def connect_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    return conn, cursor

def setup_db():
    conn, cursor = connect_db()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            price REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            item_name TEXT,
            price REAL,
            quantity INTEGER,
            subtotal REAL,
            order_time TEXT
        )
    """)
    # Insert menu if empty
    cursor.execute("SELECT COUNT(*) FROM menu")
    if cursor.fetchone()[0] == 0:
        foods = [
            ('Burger 🍔','Food',100), ('Pizza 🍕','Food',150), ('Fried Chicken 🍗','Food',200),
            ('Spaghetti 🍝','Food',170), ('Grilled Fish 🐟','Food',250), ('Rice and Beans 🍛','Food',240),
            ('Beef Steak 🥩','Food',180), ('Chicken Sandwich 🥪','Food',140),
            ('French Fries 🍟','Food',100), ('Vegetable Salad 🥗','Food',210)
        ]
        drinks = [
            ('Water 💧','Drink',20), ('Soda 🥤','Drink',70), ('Orange Juice 🍊','Drink',60),
            ('Mango Juice 🥭','Drink',55), ('Pineapple Juice 🍍','Drink',65), ('Coffee ☕','Drink',74),
            ('Tea 🍵','Drink',80), ('Milkshake 🥛','Drink',54), ('Lemonade 🍋','Drink',90),
            ('Iced Tea 🧊🍵','Drink',70)
        ]
        cursor.executemany("INSERT INTO menu (name, category, price) VALUES (?, ?, ?)", foods + drinks)
    conn.commit()
    conn.close()

def get_menu(category=None):
    conn, cursor = connect_db()
    if category:
        cursor.execute("SELECT id, name, price FROM menu WHERE category=?", (category,))
    else:
        cursor.execute("SELECT id, name, price, category FROM menu")
    items = cursor.fetchall()
    conn.close()
    return items

def add_order(customer_name, item_name, price, quantity):
    subtotal = price * quantity
    order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn, cursor = connect_db()
    cursor.execute("""
        INSERT INTO orders(customer_name, item_name, price, quantity, subtotal, order_time)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (customer_name, item_name, price, quantity, subtotal, order_time))
    conn.commit()
    conn.close()
    return subtotal

def get_orders_by_date(date_str):
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM orders WHERE order_time LIKE ?", (f"{date_str}%",))
    orders = cursor.fetchall()
    conn.close()
    return orders

# ----------------- MAIN GUI CLASS -----------------
class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Appetite Restaurant")
        self.cart = []
        self.customer_name = ""
        setup_db()
        self.login_screen()

    # -------- Customer Login --------
    def login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Enter Customer Name:").pack(pady=10)
        name_entry = tk.Entry(self.root)
        name_entry.pack(pady=5)

        # Pass the entry value using lambda
        tk.Button(
            self.root,
            text="Continue",
            command=lambda: self.main_menu(name_entry.get())
        ).pack(pady=10)
        tk.Button(self.root, text="Admin Login", command=self.admin_login_screen).pack(pady=5)

    # -------- Admin Login --------
    def admin_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Enter Admin Password:").pack(pady=10)
        admin_pass_entry = tk.Entry(self.root, show="*")
        admin_pass_entry.pack(pady=5)
        tk.Button(
            self.root,
            text="Login",
            command=lambda: self.admin_dashboard(admin_pass_entry.get())
        ).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.login_screen).pack(pady=5)

    def admin_dashboard(self, password):
        if password != "admin123":
            messagebox.showerror("Error", "Incorrect password")
            self.admin_login_screen()
            return
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Admin Dashboard").pack(pady=10)
        today = date.today().strftime("%Y-%m-%d")
        orders = get_orders_by_date(today)
        total_sales = sum([o[5] for o in orders])
        tk.Label(self.root, text=f"Today's Date: {today}").pack()
        tk.Label(self.root, text=f"Total Orders Today: {len(orders)}").pack()
        tk.Label(self.root, text=f"Total Sales Today: ${total_sales}").pack(pady=10)
        tk.Button(self.root, text="View All Receipts", command=self.view_receipts).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.login_screen).pack(pady=5)

    # -------- Main Menu --------
    def main_menu(self, customer_name):
        if not customer_name:
            messagebox.showerror("Error", "Please enter your name")
            return
        self.customer_name = customer_name  # store in self

        # Destroy previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Welcome {self.customer_name}").pack(pady=10)
        tk.Button(self.root, text="Order Food", command=lambda: self.order_screen("Food")).pack(pady=5)
        tk.Button(self.root, text="Order Drinks", command=lambda: self.order_screen("Drink")).pack(pady=5)
        tk.Button(self.root, text="View Cart / Finish Order", command=self.view_cart).pack(pady=5)
        tk.Button(self.root, text="View Previous Receipts", command=self.view_receipts).pack(pady=5)

    # -------- Ordering Screen --------
    def order_screen(self, category):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text=f"{category} Menu").pack(pady=10)
        items = get_menu(category)
        for item in items:
            frame = tk.Frame(self.root)
            frame.pack(pady=2)
            tk.Label(frame, text=f"{item[1]} - ${item[2]}").pack(side=tk.LEFT)
            qty_entry = tk.Entry(frame, width=5)
            qty_entry.pack(side=tk.LEFT, padx=5)
            tk.Button(frame, text="Add", command=lambda i=item, q=qty_entry: self.add_to_cart(i, q)).pack(side=tk.LEFT)
        tk.Button(self.root, text="Back", command=lambda: self.main_menu(self.customer_name)).pack(pady=10)

    # -------- Add to Cart --------
    def add_to_cart(self, item, qty_entry):
        try:
            quantity = int(qty_entry.get())
            if quantity <= 0:
                raise ValueError
            subtotal = add_order(self.customer_name, item[1], item[2], quantity)
            self.cart.append((item[1], quantity, subtotal))
            messagebox.showinfo("Added", f"{item[1]} x{quantity} added to cart!")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid quantity")

    # -------- View Cart --------
    def view_cart(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Cart").pack(pady=10)
        total = 0
        for c in self.cart:
            tk.Label(self.root, text=f"{c[0]} x{c[1]} = ${c[2]}").pack()
            total += c[2]
        total = self.apply_discount(total)
        tk.Label(self.root, text=f"TOTAL = ${total}").pack(pady=10)
        tk.Button(self.root, text="Back", command=lambda: self.main_menu(self.customer_name)).pack(pady=5)
        tk.Button(self.root, text="Finish & Save Receipt", command=lambda: self.finish_order(total)).pack(pady=5)

    # -------- Discount System --------
    def apply_discount(self, total):
        if total >= 500:
            discount = 0.10
            total *= (1-discount)
            tk.Label(self.root, text=f"💸 10% Discount Applied! New Total: ${total}").pack()
        return total

    # -------- Finish Order --------
    def finish_order(self, total):
        os.makedirs("Receipts", exist_ok=True)
        file_name = f"Receipts/receipt_{self.customer_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
        with open(file_name, "w") as f:
            f.write(f"Customer: {self.customer_name}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            for c in self.cart:
                f.write(f"{c[0]} x{c[1]} = ${c[2]}\n")
            f.write("-----------------------\n")
            f.write(f"TOTAL = ${total}\n")
        messagebox.showinfo("Receipt Saved", f"Receipt saved to {file_name}")
        self.cart.clear()
        self.main_menu(self.customer_name)

    # -------- View Receipts --------
    def view_receipts(self):
        os.makedirs("Receipts", exist_ok=True)
        receipts = os.listdir("Receipts")
        if not receipts:
            messagebox.showinfo("No Receipts", "No receipt files found.")
            return
        # New window
        win = tk.Toplevel(self.root)
        win.title("View Receipts")
        tk.Label(win, text="Saved Receipts").pack(pady=10)
        listbox = tk.Listbox(win, width=60)
        listbox.pack(padx=10, pady=5)
        for r in receipts:
            listbox.insert(tk.END, r)

        def open_receipt():
            selected = listbox.curselection()
            if not selected:
                messagebox.showwarning("Select", "Please select a receipt")
                return
            file_path = os.path.join("Receipts", listbox.get(selected[0]))
            os.system(f'open "{file_path}"')  # MacOS. Use 'start' on Windows

        tk.Button(win, text="Open Selected Receipt", command=open_receipt).pack(pady=5)
        tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

# ----------------- RUN APP -----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()
