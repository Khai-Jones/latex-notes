assets = {}
liabilities = {}

# Get user input for financial statement name
Name1 = input(
    "Enter the name of the Financial Statement (e.g., Company, Balance Sheet, As of...): "
)


# Create formatted header
def name_financialstatement(name):
    output = name.split(",")
    formatted = ""
    for i in range(len(output)):
        if i != len(output) - 1:
            formatted += f"{output[i].strip()} \\\\\n"
        else:
            formatted += f"\\textit{{{output[i].strip()}}}\n"
    return formatted


# Enter Assets
def enter_assets():
    print("\nEnter assets (type 'done' to finish):")
    while True:
        key = input("Enter Asset: ")
        if key.lower().strip() == "done":
            break
        try:
            value = float(input("Enter Value: "))
            assets[key] = value
        except ValueError:
            print("Please enter a valid number.")


# Enter Liabilities
def enter_liabilities():
    print("\nEnter liabilities/equity (type 'done' to finish):")
    while True:
        key = input("Enter Liability or Equity: ")
        if key.lower().strip() == "done":
            break
        try:
            value = float(input("Enter Value: "))
            liabilities[key] = value
        except ValueError:
            print("Please enter a valid number.")


# Generate LaTeX document
def generate_latex(header, assets, liabilities):
    total_assets = sum(assets.values())
    total_liabilities = sum(liabilities.values())

    asset_rows = "".join([f"{k} & \\${v:,.2f} \\\\\n" for k, v in assets.items()])
    liability_rows = "".join(
        [f"{k} & \\${v:,.2f} \\\\\n" for k, v in liabilities.items()]
    )

    return f"""
\\begin{{center}}
\\begin{{tabular}}{{ |p{{7cm}}||p{{7cm}}|  }}
    \\hline
    \\multicolumn{{2}}{{|c|}}{{%
        \\begin{{tabular}}{{c}}
{header}
        \\end{{tabular}}
    }} \\\\
    \\hline
    \\\\
    Resources (Assets) & Claims (Liabilities and Equity) \\\\ \\\\ 
    \\begin{{tabular}}{{p{{4cm}} r r}}
{asset_rows}
        & & \\textbf{{\\${total_assets:,.2f}}}
    \\end{{tabular}}
    &
    \\begin{{tabular}}{{p{{4cm}} r r}}
{liability_rows}
        & & \\textbf{{\\${total_liabilities:,.2f}}}
    \\end{{tabular}} \\\\
    \\hline
\\end{{tabular}}
\\end{{center}}
"""


# Main
def main():
    header = name_financialstatement(Name1)
    enter_assets()
    enter_liabilities()
    file_name = input("\nEnter filename (without extension): ")
    output = generate_latex(header, assets, liabilities)

    with open(f"{file_name}.tex", "w") as file:
        file.write(output)

    print(f"\n✅ LaTeX file '{file_name}.tex' has been created successfully.")


main()
