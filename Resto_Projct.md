# Resto_Project

const prompt = require("prompt-sync")();
const chalk = require("chalk");

// =======================
//     RESTAURANT LOGO
// =======================
function displayLogo() {
  console.log(chalk.cyan.bold(`
███╗   ███╗██╗   ██╗ ██████╗ 
████╗ ████║██║   ██║██╔════╝ 
██╔████╔██║██║   ██║██║ ████╗
██║╚██╔╝██║██║   ██║██║   ██║
██║ ╚═╝ ██║╚██████╔╝╚██████╔╝
╚═╝     ╚═╝ ╚═════╝  ╚═════╝ 
     M U G _ R E S T O – 2025
`));
}

// =========================
//     MENU DATA
// =========================
const menu = {
  1: { name: "Pizza", price: 12 },
  2: { name: "Burger", price: 14 },
  3: { name: "Fries", price: 10 },
  4: { name: "2 Chicken-wings", price: 17 },
  5: { name: "1 Chicken-wing", price: 9 },
  6: { name: "Beef & Rice", price: 20 },
  7: { name: "Fish & Rice", price: 18 },
  8: { name: "Water", price: 2 },
  9: { name: "Soda", price: 6 },
  10: { name: "Milkshake (Strawberry)", price: 4.3 },
  11: { name: "Milkshake (Chocolate)", price: 4.5 },
  12: { name: "Milkshake (Vanilla)", price: 4.1 },
  13: { name: "Milkshake (Tropical Mix)", price: 4.7 },
  14: { name: "Black Coffee", price: 3 },
  15: { name: "Cappuccino", price: 3.5 },
  16: { name: "Latte", price: 3.5 },
  17: { name: "Espresso", price: 4 },
  18: { name: "Chocolate Coffee", price: 5 }
};

// =========================
//     SALES DATABASE
// =========================
let sales = [];
let totalRevenue = 0;

// =========================
//     SHOW MENU
// =========================
function showMenu() {
  console.log(chalk.yellow.bold("\n========= MENU ========="));
  for (let id in menu) {
    console.log(chalk.green(`${id}. ${menu[id].name} — 
$${menu[id].price}`));
  }
}

// =========================
//     ADMIN MODE
// =========================
let adminPassword = null;

function adminMode() {
  // First-time password creation
  if (!adminPassword) {
    console.log(chalk.yellow("\n=== Admin Password Setup ==="));
    while (true) {
      let input = prompt("Create your Admin password: ", { echo: "*" });
      if (input.trim() === "") {
        console.log(chalk.red("❌ Password cannot be empty! Try again."));
      } else {
        adminPassword = input;
        console.log(chalk.green("✅ Admin password created 
successfully!\n"));
        break;
      }
    }
  }

  // Password entry for login
  while (true) {
    let password = prompt(chalk.yellow("Enter Admin Password: "), { echo: 
"*" });

    if (password.trim() === "") {
      console.log(chalk.red("❌ Password cannot be empty! Try again."));
    } else if (password !== adminPassword) {
      console.log(chalk.red("❌ Wrong password! Access denied.\n"));
      return; // exit admin mode
    } else {
      break; // correct password
    }
  }

  console.log(chalk.red.bold("\n=== ADMIN MODE (MUGISHA) ==="));

  console.log(chalk.cyan(`Total Orders: ${sales.length}`));
  console.log(chalk.cyan(`Total Revenue: $${totalRevenue.toFixed(2)}`));

  let count = {};
  sales.forEach(item => {
    count[item.name] = (count[item.name] || 0) + 1;
  });

  console.log(chalk.yellow("\nItems Sold:"));
  console.log(count);

  if (sales.length > 0) {
    let mostOrdered = Object.keys(count).reduce((a, b) =>
      count[a] > count[b] ? a : b
    );
    console.log(chalk.magenta(`\nMost Ordered Item: ${mostOrdered}`));
  }

  console.log(chalk.green("\nAdmin Mode Closed.\n"));
}

// =========================
//     MAIN PROGRAM
// =========================
function main() {
  displayLogo();

  console.log(chalk.blue("Welcome to MUG RESTO!"));
  console.log(chalk.blue("Developed by: MUGISHA ❤️\n"));

  while (true) {
    console.log(chalk.yellow("\n1. Place Order"));
    console.log(chalk.yellow("2. Admin Mode"));
    console.log(chalk.yellow("3. Exit"));

    let action = prompt(chalk.green("\nChoose option: "));

    if (action === "1") {
      // PLACE ORDER
      let receipt = [];
      let orderTotal = 0;

      while (true) {
        showMenu();

        let choice = Number(prompt(chalk.cyan("\nEnter Item Number: ")));
        if (!menu[choice]) {
          console.log(chalk.red("❌ Invalid choice!"));
          continue;
        }

        let qty = Number(prompt("Enter Quantity: "));
        if (qty <= 0 || isNaN(qty)) {
          console.log(chalk.red("❌ Quantity must be a positive 
number!"));
          continue;
        }

        let cost = menu[choice].price * qty;
        orderTotal += cost;

        for (let i = 0; i < qty; i++) {
          sales.push({ name: menu[choice].name });
        }

        receipt.push({
          item: menu[choice].name,
          qty,
          price: menu[choice].price,
          total: cost
        });

        let more = prompt("Add more items? (y/n): ");
        if (more.toLowerCase() !== "y") break;
      }

      totalRevenue += orderTotal;

      // PRINT RECEIPT
      console.log(chalk.green.bold("\n===== RECEIPT ====="));
      receipt.forEach(r => {
        console.log(chalk.green(`${r.item} x${r.qty} — 
$${r.total.toFixed(2)}`));
      });
      console.log(chalk.blue.bold(`\nTOTAL: $${orderTotal.toFixed(2)}`));
      console.log(chalk.green("=====================\n"));

    } else if (action === "2") {
      adminMode();

    } else if (action === "3") {
      console.log(chalk.cyan("Thank you for visiting MUG RESTO!"));
      break;

    } else {
      console.log(chalk.red("❌ Invalid option!"));
    }
  }
}

// START PROGRAM
main();
