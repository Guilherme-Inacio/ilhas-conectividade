import unittest

from src.main import UnionFind


class TestUnionFind(unittest.TestCase):
    def test_initialization_sets_each_element_as_its_own_representative(self):
        union_find = UnionFind(5)

        self.assertEqual(union_find.components, 5)
        for element in range(1, 6):
            with self.subTest(element=element):
                self.assertEqual(union_find.find(element), element)

    def test_union_connects_two_elements_and_decreases_component_count(self):
        union_find = UnionFind(5)

        union_find.union(1, 2)

        self.assertEqual(union_find.find(1), union_find.find(2))
        self.assertEqual(union_find.components, 4)

    def test_repeated_union_does_not_decrease_component_count(self):
        union_find = UnionFind(5)
        union_find.union(1, 2)

        union_find.union(1, 2)

        self.assertEqual(union_find.components, 4)

    def test_indirect_unions_connect_all_elements_in_chain(self):
        union_find = UnionFind(5)

        union_find.union(1, 2)
        union_find.union(2, 3)

        representative = union_find.find(1)
        self.assertEqual(union_find.find(2), representative)
        self.assertEqual(union_find.find(3), representative)

    def test_union_by_size_keeps_larger_set_root(self):
        union_find = UnionFind(5)
        union_find.union(1, 2)
        union_find.union(1, 3)  # conjunto de tamanho 3, com raiz 1
        union_find.union(4, 5)  # conjunto de tamanho 2, com raiz 4

        union_find.union(4, 1)

        self.assertEqual(union_find.find(1), 1)
        self.assertEqual(union_find.find(4), 1)
        self.assertEqual(union_find.size[1], 5)

    def test_isolated_element_remains_its_own_representative(self):
        union_find = UnionFind(5)
        union_find.union(1, 2)
        union_find.union(2, 3)

        self.assertEqual(union_find.find(4), 4)

    def test_unioning_all_elements_leaves_one_component(self):
        union_find = UnionFind(5)
        for element in range(1, 5):
            union_find.union(element, element + 1)

        self.assertEqual(union_find.components, 1)
        representatives = {union_find.find(element) for element in range(1, 6)}
        self.assertEqual(len(representatives), 1)


if __name__ == "__main__":
    unittest.main()
