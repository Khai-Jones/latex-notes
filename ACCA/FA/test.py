current_assets = {}
non_current_assets = {}
current_liabilities = {}
non_current_liabilities = {}
capital = {}


def choosing_dict():
    name = ""
    dictionary = {}

    print("1. Current Assets")
    print("2. Non-current Assets")
    print("3. Current Liability")
    print("4. Non-current Liability")
    print("5. Capital")

    while True:
        print("\n")
        decision = input("Type (1,2,3,4,5): ").strip()
        if decision == "1":
            dictionary = current_assets
            name = "current assets"
            break
        elif decision == "2":
            dictionary = non_current_assets
            name = "non current assets"
            break
        elif decision == "3":
            dictionary = current_liabilities
            name = "current liabilites"
            break
        elif decision == "4":
            dictionary = non_current_liabilities
            name = "non current liabilties"
            break
        elif decision == "5":
            dictionary = capital
            name = "capital"
            break
        else:
            print("Choose a valid choice")

    return dictionary, name


def section_input(dictionary, name):
    """
    Prompt user to input asset names and values until 'done' is entered.
    Stores the input into the global 'assets' dictionary with integer values.
    """
    print(f"{name} section ")
    while True:
        outer_key = input("Enter current asset name: ").strip().lower()
        if outer_key.strip().lower() == "done":
            break
        try:
            dictionary[outer_key] = {}
            dictionary[outer_key]["less"] = {}

            value = input(f"Enter {name} value: ")
            dictionary[outer_key]["value"] = int(value)

            while True:
                choice = input("Exter a less item (y/n): ").strip().lower()
                if choice == "n":
                    break
                less_name = input(f"Enter less item for {name}: ")
                less_value = input("Enter less value for the item: ")

                dictionary[outer_key]["less"][less_name] = int(less_value)

        except ValueError:
            print("Enter a valid number")
    while True:
        decision = input(
            "Do you want to enter records for another section (y/n)?:  "
        ).strip()
        if decision == "n":
            break
        choosing_dict()
        section_input(dictionary, name)


def process_input():
    """
    Processes asset, liability, and equity dictionaries into LaTeX tabular format.
    Returns a string of LaTeX code representing the Statement of Financial Position.
    """
    current_ass_row = ""
    ncurrent_ass_row = ""
    current_liab_row = ""
    ncurrent_liab_row = ""
    capital_row = ""

    current_asset_total = 0
    ncurrent_asset_total = sum(non_current_assets.values())
    current_liab_total = sum(current_liabilities.values())
    ncurrent_liab_total = sum(non_current_liabilities.values())
    capital_total = sum(capital.values())

    def helper_func(dictionary):
        component_row = " "
        value_total = 0
        less_value_total = 0

        for name, data in dictionary.items():
            component_row += f"{name} & \\ & \\ & \\${data['value']} \\\\ \n"
            value_total += data["value"]
            for less_name, less_value in data["less"].items():
                component_row += f"{less_name} & \\ & (\\${less_value})\\ & \\ \\\\ \n"
                less_value_total += less_value
        return component_row, value_total, less_value_total

    current_ass_row, current_asset_total, current_asset_less_total = helper_func(
        current_assets
    )
    print(current_ass_row, current_asset_total, current_asset_less_total)


dictionary, name = choosing_dict()
section_input(dictionary, name)
process_input()
