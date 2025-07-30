from datetime import datetime

# Store ledger data
accounts = {}


# Get year from user
def get_year():
    while True:
        year = input("Enter the accounting year (e.g., 2024): ").strip()
        if year.isdigit() and len(year) == 4:
            return year
        print("❌ Please enter a valid 4-digit year.")


# Function to get user input for one side of an account
def get_entries(side_name):
    entries = []
    print(f"\nEnter {side_name} entries (type 'done' as date to finish):")
    while True:
        date = input("  Date (e.g. Jan 8): ").strip()
        if date.lower() == "done":
            break
        desc = input("  Description: ").strip()
        try:
            amount = float(input("  Amount: ").strip())
        except ValueError:
            print("  ❌ Invalid amount. Try again.")
            continue
        entries.append((date, desc, amount))
    return entries


def format_account_latex(name, debits, credits, year):
    # Pad shorter side with empty rows
    max_rows = max(len(debits), len(credits))
    debits += [("", "", 0)] * (max_rows - len(debits))
    credits += [("", "", 0)] * (max_rows - len(credits))

    rows = ""
    for i in range(max_rows):
        d_date, d_desc, d_amt = debits[i]
        c_date, c_desc, c_amt = credits[i]

        d_amt_str = f"{d_amt:,.0f}" if d_amt != 0 else ""
        c_amt_str = f"{c_amt:,.0f}" if c_amt != 0 else ""

        rows += f"{d_date} & {d_desc} & {d_amt_str} & {c_date} & {c_desc} & {c_amt_str} \\\\\n"

    total_debit = sum(a[2] for a in debits)
    total_credit = sum(a[2] for a in credits)

    # Find the last non-zero debit and credit amounts for single underline
    last_debit_amount = ""
    for _, _, amt in reversed(debits):
        if amt != 0:
            last_debit_amount = f"\\underline{{{amt:,.0f}}}"
            break

    last_credit_amount = ""
    for _, _, amt in reversed(credits):
        if amt != 0:
            last_credit_amount = f"\\underline{{{amt:,.0f}}}"
            break

    # Construct the total line with double underlines
    total_line = (
        f"& & {last_debit_amount} & & & {last_credit_amount} \\\\\n"
        f"& & \\underline{{\\underline{{{total_debit:,.0f}}}}} & & & \\underline{{\\underline{{{total_credit:,.0f}}}}} \\\\\n"
    )

    return f"""
\\noindent
\\begin{{tabular}}{{@{{}}p{{2cm}}p{{4cm}}r|p{{2cm}}p{{4cm}}r@{{}}}}
\\multicolumn{{6}}{{c}}{{\\textbf{{{name}}}}} \\\\ \\addlinespace[1ex]
\\toprule
\\textbf{{{year}}} & \\multicolumn{{1}}{{l}}{{\\textbf{{}}}} & \\textbf{{£}} & \\textbf{{{year}}} & \\multicolumn{{1}}{{l}}{{\\textbf{{}}}} & \\textbf{{£}} \\\\
{rows}{total_line}
\\end{{tabular}}
"""


# Main function to collect and generate the LaTeX file
def main():
    print("📘 Ledger Entry Generator\n")

    year = get_year()

    while True:
        name = input("\nEnter account name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        debits = get_entries("DEBIT (left side)")
        credits = get_entries("CREDIT (right side)")
        accounts[name] = (debits, credits)

    filename = input("\nEnter LaTeX filename (no extension): ").strip()
    latex_content = f"""
"""

    for acc, (debits, credits) in accounts.items():
        latex_content += (
            format_account_latex(acc, debits, credits, year) + "\n\\vspace{1.5cm}\n"
        )

    with open(f"{filename}.tex", "w") as f:
        f.write(latex_content)

    print(f"\n✅ Ledger saved as {filename}.tex")


if __name__ == "__main__":
    main()
