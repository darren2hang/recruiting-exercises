import copy


class InventoryAllocator:
    @staticmethod
    def get_cheapest_shipment(order, warehouses):
        original_order = copy.deepcopy(order)
        shipments = []
        num_of_items = len(order)
        num_of_satisfied_items = 0

        for warehouse in warehouses:
            inventory = warehouse.get("inventory")
            shipment = None
            warehouse_can_ship_entire_order = True
            single_shipment_covering_entire_order = {warehouse.get("name"): {}}
            for item in order:
                if item in inventory:
                    if original_order.get(item) < 0:
                        return []
                    elif order.get(item) > 0:
                        num_added = inventory[item]
                        order[item] -= num_added
                        if order[item] <= 0:
                            num_of_satisfied_items += 1
                        if order[item] < 0:
                            num_added += InventoryAllocator.combine_item_shipments(shipments, order.get(item), item)

                        if shipment is None:
                            shipment = {warehouse.get("name"): {item: num_added}}
                        else:
                            shipment[warehouse.get("name")][item] = num_added
                else:
                    warehouse_can_ship_entire_order = False

                if warehouse_can_ship_entire_order:
                    if inventory.get(item) >= original_order.get(item):
                        single_shipment_covering_entire_order[warehouse.get("name")][item] = original_order.get(item)
                    else:
                        warehouse_can_ship_entire_order = False

            if warehouse_can_ship_entire_order:
                return [single_shipment_covering_entire_order]
            if shipment is not None:
                shipments.append(shipment)
        if num_of_satisfied_items < num_of_items:
            return []
        else:
            InventoryAllocator.reduce_shipments(shipments, warehouses)
            return shipments

    @staticmethod
    def combine_item_shipments(shipments, count, item):
        if shipments is None:
            return
        i = len(shipments) - 1
        while i > -1 and count < 0:
            num_at_current_warehouse = InventoryAllocator.get_num_of(item, shipments[i])
            if num_at_current_warehouse is not None and num_at_current_warehouse <= abs(count):
                warehouse_name = list(shipments[i].keys())[0]
                current_inventory = shipments[i].get(warehouse_name)

                current_inventory.pop(item)
                count += num_at_current_warehouse

                if len(current_inventory) == 0:
                    shipments.pop(i)
            i -= 1
        return count

    @staticmethod
    def reduce_shipments(shipments, warehouses):
        for i in range(len(shipments)):
            shipment = shipments[i]
            warehouse_name = list(shipment.keys())[0]
            inventory = shipment.get(warehouse_name)
            new_locations = []
            can_move_all_items = True
            for item in inventory:
                location_to_move_to = InventoryAllocator.get_alt_shipment(shipment, item, inventory.get(item),
                                                                          shipments, warehouses)
                if location_to_move_to == False:
                    can_move_all_items = False
                else:
                    new_locations.append(location_to_move_to)

            if can_move_all_items:
                shipment[warehouse_name] = {}
                for new_loc_for_shipment in new_locations:
                    for j in range(len(new_loc_for_shipment)):
                        item = new_loc_for_shipment[j].get("item")
                        index_of_new_shipment = new_loc_for_shipment[j].get("index")
                        count = new_loc_for_shipment[j].get("count")
                        name_of_new_warehouse = list(shipments[index_of_new_shipment].keys())[0]

                        if new_loc_for_shipment[j].get("isNew"):
                            shipments[index_of_new_shipment][name_of_new_warehouse][item] = count
                        else:
                            shipments[index_of_new_shipment][name_of_new_warehouse][item] = \
                                shipments[index_of_new_shipment][name_of_new_warehouse].get(
                                item) + count
        shipments[:] = [shipment for shipment in shipments if len(shipment.get(list(shipment.keys())[0])) > 0]

    @staticmethod
    def get_alt_shipment(shipment, item, count, shipments, warehouses):
        locations = []
        warehouses_item_dict = InventoryAllocator.get_warehouse_item_dict(warehouses, item)
        for i in range(len(shipments)):
            other_shipment = shipments[i]
            if other_shipment is not shipment:
                warehouse_name = list(other_shipment.keys())[0]
                warehouse_item_count = warehouses_item_dict.get(warehouse_name)
                other_shipment_item_count = InventoryAllocator.get_num_of(item, other_shipment)
                if warehouse_item_count is not None:
                    if item not in other_shipment.get(warehouse_name):
                        locations.append(
                            {"index": i, "count": min(count, warehouse_item_count), "item": item,
                             "isNew": True})
                        count -= min(count, warehouse_item_count)
                    elif other_shipment_item_count is not None and other_shipment_item_count < warehouse_item_count:
                        locations.append(
                            {"index": i, "count": min(warehouse_item_count - other_shipment_item_count, count),
                             "item": item,
                             "isNew": False})
                        count -= min(warehouse_item_count - other_shipment_item_count, count)

            if count == 0:
                break
        if count > 0:
            return False
        if len(locations) > 0:
            return locations
        return False

    @staticmethod
    def get_warehouse_item_dict(warehouses, item):
        warehouse_name_item_dict = {}
        for warehouse in warehouses:
            if item in warehouse.get("inventory"):
                warehouse_name_item_dict[warehouse.get("name")] = warehouse.get("inventory").get(item)
        return warehouse_name_item_dict

    @staticmethod
    def get_num_of(item, shipment):
        warehouse_name = list(shipment.keys())[0]
        inventory = shipment.get(warehouse_name)
        return inventory.get(item)
