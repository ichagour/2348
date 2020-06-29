from dataclasses import dataclass
from datetime import datetime


@dataclass
class InventoryItem:
    item_id: str
    item_name: str
    manufacturer: str
    damaged: bool
    price: int
    service_date: datetime

    @classmethod
    def from_manufacturer_list(cls, line):
        item_id, manufacturer, item_name, damaged = line.split(",")
        return cls(
            item_id=item_id,
            item_name=item_name,
            manufacturer=manufacturer,
            service_date=None,
            price=None,
            damaged=damaged == "damaged",
        )

    def __str__(self):
        return f"(Id: {self.item_id}, Manufacturer: {self.manufacturer}, Name: {self.item_name}, Price: {self.price})"

    @property
    def to_csv_row(self):
        return f"{self.item_id},{self.manufacturer},{self.item_name},{self.price},{'{dt.month}/{dt.day}/{dt.year}'.format(dt = self.service_date)},{'damaged'if self.damaged else ''}\n"

    @property
    def deliverable(self):
        return (not self.damaged) and self.service_date >= datetime.now()


inventory_item_id_map = {}
manufacturer_list = []
name_list = []


def build_mappings(manufacturer_list_file, price_list_file, service_list_file):
    with open(manufacturer_list_file) as f:
        lines = f.readlines()
        for line in lines:
            inventory_item = InventoryItem.from_manufacturer_list(line.strip())
            inventory_item_id_map[inventory_item.item_id] = inventory_item
            if inventory_item.item_name not in name_list:
                name_list.append(inventory_item.item_name)
            if inventory_item.manufacturer not in manufacturer_list:
                manufacturer_list.append(inventory_item.manufacturer)

    with open(price_list_file) as f:
        lines = f.readlines()
        for line in lines:
            item_id, price = line.strip().split(",")
            inventory_item = inventory_item_id_map[item_id]
            inventory_item.price = int(price)

    with open(service_list_file) as f:
        lines = f.readlines()
        for line in lines:
            item_id, service_date = line.strip().split(",")
            inventory_item = inventory_item_id_map[item_id]
            inventory_item.service_date = datetime.strptime(service_date, "%m/%d/%Y")


def find_items(search_query):
    item_manufacturer = []
    item_name = []
    for manufacturer in manufacturer_list:
        if manufacturer in search_query:
            item_manufacturer.append(manufacturer)
    if len(item_manufacturer) != 1:
        return False, None, None
    for name in name_list:
        if name in search_query:
            item_name.append(name)
    if len(item_name) != 1:
        return False, None, None
    manufacturer = item_manufacturer[0]
    name = item_name[0]
    for item in inventory_item_id_map.values():
        if (
            item.deliverable
            and item.manufacturer == manufacturer
            and item.item_name == name
        ):
            return True, item, find_related_item(item)
    return False, None, None


def find_related_item(item):
    cost_diff = 0
    related_item = None
    for i in inventory_item_id_map.values():
        if (
            i.deliverable
            and i.item_name == item.item_name
            and i.manufacturer != item.manufacturer
        ):
            if cost_diff == 0:
                cost_diff = item.price - i.price
                related_item = i
            if cost_diff < (item.price - i.price):
                cost_diff = item.price - i.price
                related_item = i
    return related_item


def build_full_inventory_report(filename):
    sorted_values = sorted(
        inventory_item_id_map.values(), key=lambda x: x.manufacturer + x.item_name
    )
    with open(filename, "w") as f:
        for item in sorted_values:
            f.write(item.to_csv_row)


def build_past_service_report(filename):
    sorted_values = sorted(inventory_item_id_map.values(), key=lambda x: x.service_date)
    with open(filename, "w") as f:
        for item in inventory_item_id_map.values():
            if item.service_date <= datetime.now():
                f.write(item.to_csv_row)


def build_damaged_inventory_report(filename):
    sorted_values = sorted(inventory_item_id_map.values(), key=lambda x: x.price)
    with open(filename, "w") as f:
        for item in sorted_values:
            if item.damaged:
                f.write(item.to_csv_row)


def build_itemwise_inventory_report():
    for item_name in name_list:
        sorted_values = sorted(inventory_item_id_map.values(), key=lambda x: x.item_id)
        with open(f"{item_name.capitalize()}Inventory.csv", "w") as f:
            for item in sorted_values:
                if item.item_name == item_name:
                    f.write(item.to_csv_row)


def interactive_input():
    another_search = "y"
    while another_search == "y":
        another_search = input("What would you like to search or press q to quit:")
        if another_search == "q":
            break
        found, inventory_item, related_item = find_items(another_search)

        if found:
            print(f"Your item is: {inventory_item}")
            if related_item:
                print(f"You may, also, consider: {related_item}")
        else:
            print("No such item in inventory")

        another_search = "y"


def main():
    build_mappings(
        manufacturer_list_file="ManufacturerList.csv",
        price_list_file="PriceList.csv",
        service_list_file="ServiceDatesList.csv",
    )
    build_full_inventory_report("FullInventory.csv")
    build_past_service_report("PastServiceDateInventory.csv")
    build_damaged_inventory_report("DamagedInventory.csv")
    build_itemwise_inventory_report()
    interactive_input()


if __name__ == "__main__":
    main()
