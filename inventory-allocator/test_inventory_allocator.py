import unittest
from inventory_allocator import InventoryAllocator


class TestInventoryAllocator(unittest.TestCase):

    def test_case_1(self):
        # Order can be shipped using multiple warehouses
        order = {"apple": 5, "banana": 5, "orange": 5}
        warehouses = [
            {
                "name": "owd",
                "inventory": {"apple": 5, "orange": 10}},
            {
                "name": "dm",
                "inventory": {"banana": 5, "orange": 10}
            }
        ]
        self.assertEqual(InventoryAllocator.get_cheapest_shipment(order, warehouses),
                         [{"owd": {"apple": 5, "orange": 5}}, {"dm": {"banana": 5}}])

    def test_case_2(self):
        # Order can be shipped using multiple warehouses
        order = {
            "apple": 5,
            "banana": 5,
            "orange": 7
        }
        warehouses = [
            {
                "name": "owd",
                "inventory": {"apple": 5, "orange": 1}
            },
            {
                "name": "dm",
                "inventory": {"banana": 5, "orange": 10}
            }
        ]
        self.assertEqual(InventoryAllocator.get_cheapest_shipment(order, warehouses),
                         [{"owd": {"apple": 5}}, {"dm": {"banana": 5, "orange": 7}}])

    def test_case_3(self):
        # Order can't be shipped because there is not enough inventory
        order = {"apple": 2}
        warehouses = [
            {
                "name": "owd",
                "inventory": {"apple": 1, "orange": 10}
            },
            {
                "name": "dm",
                "inventory": {"banana": 5, "orange": 10}
            }
        ]
        self.assertEqual(InventoryAllocator.get_cheapest_shipment(order, warehouses), [])

    def test_case_4(self):
        # Order can't be shipped because there is not enough inventory for one of the items
        order = {
            "apple": 2,
            "banana": 6
        }
        warehouses = [
            {
                "name": "owd",
                "inventory": {"apple": 5, "orange": 10}
            },
            {
                "name": "dm",
                "inventory": {"banana": 5, "orange": 10}
            }
        ]
        self.assertEqual(InventoryAllocator.get_cheapest_shipment(order, warehouses), [])

    def test_case_5(self):
        # Order can be shipped using multiple warehouses that aren't adjacent
        order = {"apple": 5,
                 "orange": 5,
                 "banana": 10
                 }
        warehouses = [
            {
                "name": "owd",
                "inventory": {"apple": 1, "orange": 10}
            },
            {
                "name": "dm",
                "inventory": {"banana": 5, "watermelon": 10}
            },
            {
                "name": "wsn",
                "inventory": {"apple": 4, "banana": 10}
            }
        ]
        self.assertEqual(InventoryAllocator.get_cheapest_shipment(order, warehouses),
                         [{"owd": {"apple": 1, "orange": 5}}, {"wsn": {"apple": 4, "banana": 10}}])

    def test_case_6(self):
        # Single shipment at the end is cheaper than multiple shipments from beginning of list. Also, testing on a larger size of warehouses.
        order = {"apple": 25,
                 "orange": 39,
                 "banana": 41,
                 "pineapple": 25,
                 "kiwi": 62,
                 "blueberries": 42,
                 "peaches": 65,
                 "mangoes": 43,
                 "watermelon": 42
                 }
        warehouses = [
            {
                "name": "owd",
                "inventory": {"apple": 15, "orange": 10}
            },
            {
                "name": "dm",
                "inventory": {"pineapple": 5, "watermelon": 10}
            },
            {
                "name": "wsn",
                "inventory": {"blueberries": 14, "banana": 10}
            },
            {
                "name": "awt",
                "inventory": {"kiwi": 21, "orange": 12}
            },
            {
                "name": "dom",
                "inventory": {"pineapple": 25, "peaches": 10}
            },
            {
                "name": "ent",
                "inventory": {"kiwi": 14, "apple": 10}
            },
            {
                "name": "wrn",
                "inventory": {"watermelon": 21, "orange": 10}
            },
            {
                "name": "ty",
                "inventory": {"mangoes": 5, "watermelon": 10}
            },
            {
                "name": "pwm",
                "inventory": {"banana": 24, "mangoes": 19}
            },
            {
                "name": "knm",
                "inventory": {"apple": 41, "orange": 10}
            },
            {
                "name": "gtn",
                "inventory": {"pineapple": 5, "watermelon": 10}
            },
            {
                "name": "rwx",
                "inventory": {"blueberries": 24, "banana": 10}
            },
            {
                "name": "swn",
                "inventory": {"kiwi": 21, "orange": 10, "mangoes": 19}
            },
            {
                "name": "yrn",
                "inventory": {"pineapple": 15, "watermelon": 10}
            },
            {
                "name": "tnu",
                "inventory": {"peaches": 14, "banana": 10}
            },
            {
                "name": "jin",
                "inventory": {"pineapple": 11, "orange": 10}
            },
            {
                "name": "mni",
                "inventory": {"pineapple": 5, "watermelon": 10}
            },
            {
                "name": "nnl",
                "inventory": {"kiwi": 4, "banana": 10}
            },
            {
                "name": "ont",
                "inventory": {"peaches": 21, "pineapple": 16, "mangoes": 23}
            },
            {
                "name": "poj",
                "inventory": {"pineapple": 5, "watermelon": 10}
            },
            {
                "name": "xer",
                "inventory": {"watermelon": 14, "banana": 10}
            },
            {
                "name": "zas",
                "inventory": {"blueberries": 9, "peaches": 10}
            },
            {
                "name": "dzs",
                "inventory": {"mangoes": 15, "watermelon": 10}
            },
            {
                "name": "wbe",
                "inventory": {"kiwi": 14, "banana": 10}
            },
            {
                "name": "uxs",
                "inventory": {"banana": 19, "orange": 10}
            },
            {
                "name": "lax",
                "inventory": {"pineapple": 5, "watermelon": 10}
            },
            {
                "name": "slx",
                "inventory": {"peaches": 14, "banana": 10}
            },
            {
                "name": "gxm",
                "inventory": {"peaches": 11, "orange": 10}
            },
            {
                "name": "nty",
                "inventory": {"pineapple": 5, "watermelon": 10}
            },
            {
                "name": "zwz",
                "inventory": {"peaches": 12, "kiwi": 10}
            },
            {
                "name": "last",
                "inventory": {"apple": 29,
                              "orange": 49,
                              "banana": 45,
                              "pineapple": 25,
                              "kiwi": 63,
                              "blueberries": 42,
                              "peaches": 65,
                              "mangoes": 44,
                              "watermelon": 42}
            }
        ]
        self.assertEqual(InventoryAllocator.get_cheapest_shipment(order, warehouses), [{"last": {"apple": 25,
                                                                                                 "orange": 39,
                                                                                                 "banana": 41,
                                                                                                 "pineapple": 25,
                                                                                                 "kiwi": 62,
                                                                                                 "blueberries": 42,
                                                                                                 "peaches": 65,
                                                                                                 "mangoes": 43,
                                                                                                 "watermelon": 42}}])

    def test_case_7(self):
        # Order can be shipped from less warehouses than if just choosing cheapest warehouses to ship from
        # for each individual item. Instead of shipping apples from the first 2 warehouses and shipping bananas from
        # the last 3 warehouses, it"s better to ship apples from the first and last so that we can have 2 shipments
        # instead of 3 shipments.
        order = {
            "apple": 5,
            "banana": 8
        }
        warehouses = [
            {
                "name": "jku",
                "inventory": {"apple": 3, "orange": 10}
            },
            {
                "name": "dm",
                "inventory": {"apple": 3, "banana": 1}
            },
            {
                "name": "ftr",
                "inventory": {"apple": 4, "banana": 10}
            }
        ]
        self.assertEqual(InventoryAllocator.get_cheapest_shipment(order, warehouses),
                         [{"jku": {"apple": 3}}, {"ftr": {"banana": 8, "apple": 2}}])

    def test_case_8(self):
        # Order can be shipped from less warehouses than if just choosing cheapest shipments for each
        # individual item: similar scenario as test case 7.
        order = {
            "apple": 16,
            "peach": 16
        }
        warehouses = [
            {
                "name": "jku",
                "inventory": {"apple": 10, "peach": 2}
            },
            {
                "name": "dm",
                "inventory": {"apple": 10, "peach": 4}
            },
            {
                "name": "ftr",
                "inventory": {"apple": 6, "peach": 8}
            },
            {
                "name": "gbm",
                "inventory": {"apple": 4, "peach": 8}
            }
        ]
        self.assertEqual(InventoryAllocator.get_cheapest_shipment(order, warehouses),
                         [{"jku": {"apple": 10}}, {"ftr": {"peach": 8, "apple": 6}}, {"gbm": {"peach": 8}}])

    def test_case_9(self):
        # Order can be shipped from less warehouses if we move one shipment into a shipment from a different warehouse
        # that must be shipped from due to inventory shortages of other items in other warehouses (banana in this case).
        # If only looking at individual items, apples would be shipped from the first 2 warehouses and banana would be
        # shipped from the first and last warehouse. However, moving the apple shipment from the 2nd warehouse to the
        # 3rd warehouse allows the number of shipments to be 2 rather than 3.
        order = {
            "apple": 5,
            "banana": 8
        }
        warehouses = [
            {
                "name": "jku",
                "inventory": {"apple": 2, "banana": 5}
            },
            {
                "name": "dm",
                "inventory": {"apple": 5, "banana": 1}
            },
            {
                "name": "ftr",
                "inventory": {"apple": 4, "banana": 5}
            }
        ]
        self.assertEqual(InventoryAllocator.get_cheapest_shipment(order, warehouses),
                         [{"jku": {"banana": 5, "apple": 2}}, {"ftr": {"banana": 3, "apple": 3}}])

    def test_case_10(self):
        # Order can be shipped from less warehouses by combining multiple shipments from different warehouses
        # into one shipment from a warehouse instead of shipping based on individual item available in inventories
        order = {
            "pear": 8,
            "kiwi": 6
        }
        warehouses = [
            {
                "name": "jku",
                "inventory": {"pear": 2, "kiwi": 1}
            },
            {
                "name": "dm",
                "inventory": {"pear": 2, "kiwi": 2}
            },
            {
                "name": "ftr",
                "inventory": {"pear": 3, "kiwi": 3}
            },
            {
                "name": "hye",
                "inventory": {"pear": 5, "kiwi": 3}
            }
        ]
        self.assertEqual(InventoryAllocator.get_cheapest_shipment(order, warehouses),
                         [{"jku": {"pear": 2, "kiwi": 1}}, {"dm": {"kiwi": 2, "pear": 2}},
                          {"hye": {"pear": 4, "kiwi": 3}}])

    def test_case_12(self):
        # Number of shipments is reduced from if shipments were just allocated from the first warehouse and down.
        # Instead of shipping 1, 3, 2 apples from the first, second, and third warehouses, respectively, shipping
        # 3 apples from the second and 3 apples from the third warehouse reduces cost by reducing the number of
        # shipments needed from 3 to 2.
        order = {"apple": 6}
        warehouses = [
            {"name": "owd", "inventory": {"apple": 1, "orange": 4}},
            {"name": "abc", "inventory": {"apple": 3, "orange": 2}},
            {"name": "jht", "inventory": {"apple": 4, "orange": 5}},
        ]
        self.assertEqual(InventoryAllocator.get_cheapest_shipment(order, warehouses),
                         [{"abc": {"apple": 3}}, {"jht": {"apple": 3}}])

    def test_case_12(self):
        # If an order contains a negative amount, it should return []
        order = {"apple": -3}
        warehouses = [{"name": "owd", "inventory": {"apple": 5, "orange": 2}}]
        self.assertEqual(InventoryAllocator.get_cheapest_shipment(order, warehouses), [])


if __name__ == "__main__":
    unittest.main()
