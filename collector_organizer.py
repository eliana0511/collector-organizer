# 🧸 Collector Organizer v2
# Author: Ally
# Description: Advanced version with nested collections, multi-item input, and optional secrets.

import json
import os

FILENAME = "collections_v2.json"

def load_collections():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    else:
        # starter structure
        return {
            "Pop Mart": {
                "Labubu": [],
                "Skullpanda": []
            },
            "Miniso": {
                "Sanrio Character Candy Carnival Plush Pendants": []
            },
            "TopToy": {
                "Kuromi School Life Series": []
            },
            "Other": {}
        }

def save_collections(collections):
    with open(FILENAME, "w") as f:
        json.dump(collections, f, indent=4)
    print("💾 Collections saved successfully!")

def show_main_categories(collections):
    print("\n📦 Main Categories:")
    for name in collections.keys():
        print(f"- {name}")

def add_new_category(collections):
    name = input("Enter new main category name: ").title()
    if name not in collections:
        collections[name] = {}
        print(f"✅ Category '{name}' added!")
    else:
        print("⚠️ That category already exists.")
    save_collections(collections)

def add_new_subcollection(collections):
    main_cat = input("Enter main category (Pop Mart, Miniso, TopToy, Other): ").title()
    if main_cat not in collections:
        print("⚠️ Main category not found! Add it first.")
        return

    sub = input("Enter new sub-collection name: ")
    if sub not in collections[main_cat]:
        collections[main_cat][sub] = []
        print(f"✅ Sub-collection '{sub}' added under {main_cat}!")
    else:
        print("⚠️ That sub-collection already exists.")
    save_collections(collections)

def add_items_to_collection(collections):
    main_cat = input("Enter main category (Pop Mart, Miniso, TopToy, Other): ").title()
    if main_cat not in collections:
        print("⚠️ Category not found.")
        return

    sub = input("Enter sub-collection name (like Labubu, Skullpanda, etc.): ")
    if sub not in collections[main_cat]:
        print("⚠️ Sub-collection not found.")
        return

    set_name = input("Enter set name: ")

    try:
        count = int(input("How many figures to add in this set? "))
    except ValueError:
        print("❌ Invalid number.")
        return

    figures = []
    for i in range(count):
        print(f"\nAdding figure {i + 1}/{count}")
        fig_name = input("Figure name: ")
        have_it = input("Do you have it? (y/n): ").lower() == "y"
        figures.append({"name": fig_name, "have": have_it})

    secret_choice = input("Does this set have a secret figure? (y/n): ").lower()
    if secret_choice == "y":
        secret_name = input("Secret figure name: ")
        have_secret = input("Do you have it? (y/n): ").lower() == "y"
        figures.append({"name": f"{secret_name} (Secret)", "have": have_secret})

    collections[main_cat][sub].append({"set": set_name, "figures": figures})
    save_collections(collections)
    print(f"✅ Set '{set_name}' added successfully!")

    # Loop for adding more
    while True:
        again = input("\nDo you want to add more to this collection? (y) or go back to main menu (n): ").lower()
        if again == "y":
            add_items_to_collection(collections)
            return
        elif again == "n":
            return
        else:
            print("Please enter 'y' or 'n'.")

def view_collection(collections):
    main_cat = input("Enter main category: ").title()
    if main_cat not in collections:
        print("⚠️ Not found.")
        return

    sub = input("Enter sub-collection name: ")
    if sub not in collections[main_cat]:
        print("⚠️ Not found.")
        return

    print(f"\n🎀 Viewing {main_cat} → {sub}")
    for set_info in collections[main_cat][sub]:
        print(f"\n🧺 Set: {set_info['set']}")
        for fig in set_info["figures"]:
            mark = "✅" if fig["have"] else "❌"
            print(f"   {mark} {fig['name']}")

def main():
    collections = load_collections()

    while True:
        print("\n🌸 Collector Organizer Menu 🌸")
        print("1. Show main categories")
        print("2. Add main category")
        print("3. Add sub-collection")
        print("4. Add items to collection")
        print("5. View collection")
        print("6. Save and Exit")

        choice = input("Choose (1-6): ")

        if choice == "1":
            show_main_categories(collections)
        elif choice == "2":
            add_new_category(collections)
        elif choice == "3":
            add_new_subcollection(collections)
        elif choice == "4":
            add_items_to_collection(collections)
        elif choice == "5":
            view_collection(collections)
        elif choice == "6":
            save_collections(collections)
            print("👋 Goodbye! Keep collecting ✨")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()

