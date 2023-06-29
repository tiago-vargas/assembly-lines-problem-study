from solver import IterativeSystem, RecursiveSystem
from solver import IterativeSystem3, RecursiveSystem3


class TestIterativeSystem:
	class TestTwoAssemblyLines:
		class TestGettingTime:
			def test_best_path_being_line_1(self):
				entries = [1, 1000]
				stations = [[1, 2, 3], [1000, 2000, 3000]]
				transitions = [[1000, 1000], [1000, 2000]]
				exits = [1, 1000]
				system = IterativeSystem(entries, stations, transitions, exits)

				(optimal_time, _) = system.get_optimal_time()

				assert optimal_time == 1 + 1 + 2 + 3 + 1

			def test_best_path_being_line_2(self):
				entries = [1000, 1]
				stations = [[1000, 2000, 3000], [1, 2, 3]]
				transitions = [[1000, 1000], [1000, 2000]]
				exits = [1000, 1]
				system = IterativeSystem(entries, stations, transitions, exits)

				(optimal_time, _) = system.get_optimal_time()

				assert optimal_time == 1 + 1 + 2 + 3 + 1

			def test_with_transitions(self):
				entries = [10, 1000]
				stations = [[1, 2000, 3], [1000, 2, 3000]]
				transitions = [[10, 20], [10, 20]]
				exits = [10, 1000]
				system = IterativeSystem(entries, stations, transitions, exits)

				(optimal_time, _) = system.get_optimal_time()

				assert optimal_time == 10 + 1 + 10 + 2 + 20 + 3 + 10

			def test_a_system_more_difficult_to_get_optimal_time(self):
				entries = [1, 1]
				stations = [[1, 2000, 3], [1000, 2, 3000]]
				transitions = [[10, 20], [10, 20]]
				exits = [10, 1000]
				system = IterativeSystem(entries, stations, transitions, exits)

				(optimal_time, _) = system.get_optimal_time()

				assert optimal_time == 1 + 1 + 10 + 2 + 20 + 3 + 10

		class TestGettingPath:
			def test_best_path_being_line_1(self):
				entries = [1, 1000]
				stations = [[1, 2, 3], [1000, 2000, 3000]]
				transitions = [[1000, 1000], [1000, 2000]]
				exits = [1, 1000]
				system = IterativeSystem(entries, stations, transitions, exits)

				(_, optimal_path) = system.get_optimal_time()

				assert optimal_path == [(0, 0), (0, 1), (0, 2)]

			def test_best_path_being_line_2(self):
				entries = [1000, 1]
				stations = [[1000, 2000, 3000], [1, 2, 3]]
				transitions = [[1000, 1000], [1000, 2000]]
				exits = [1000, 1]
				system = IterativeSystem(entries, stations, transitions, exits)

				(_, optimal_path) = system.get_optimal_time()

				assert optimal_path == [(1, 0), (1, 1), (1, 2)]

			def test_with_transitions(self):
				entries = [10, 1000]
				stations = [[1, 2000, 3000], [1000, 2, 3]]
				transitions = [[10, 20], [10, 20]]
				exits = [10, 1000]
				system = IterativeSystem(entries, stations, transitions, exits)

				(_, optimal_path) = system.get_optimal_time()

				assert optimal_path == [(0, 0), (1, 1), (1, 2)]

			def test_bigger_system(self):
				entries = [10, 12]
				stations = [[4, 5, 3, 2], [2, 10, 1, 4]]
				transitions = [[7, 4, 5], [9, 2, 8]]
				exits = [18, 7]
				system = IterativeSystem(entries, stations, transitions, exits)

				(_, optimal_path) = system.get_optimal_time()

				assert optimal_path == [(0, 0), (0, 1), (1, 2), (1, 3)]


	class TestThreeAssemblyLines:
		class TestGettingTime:
			def test_best_path_being_line_1(self):
				entries = [1, 1000, 1000]
				stations = [[   1,    2,    3,    4],
				            [1000, 2000, 3000, 4000],
				            [1000, 2000, 3000, 4000]]
				transitions_1_2 = [[1000, 2000, 3000],
				                   [1000, 2000, 3000],
				                   []]
				transitions_2_3 = [[],
				                   [1000, 2000, 3000],
				                   [1000, 2000, 3000]]
				exits = [1, 1000, 1000]
				system = IterativeSystem3(entries, stations, transitions_1_2, transitions_2_3, exits)

				(optimal_time, _) = system.get_optimal_time()

				assert optimal_time == 1 + 1 + 2 + 3 + 4 + 1


			def test_best_path_being_line_3(self):
				entries = [1000, 1000, 1]
				stations = [[1000, 2000, 3000, 4000],
				            [1000, 2000, 3000, 4000],
				            [   1,    2,    3,    4]]
				transitions_1_2 = [[1000, 2000, 3000],
				                   [1000, 2000, 3000],
				                   []]
				transitions_2_3 = [[],
				                   [1000, 2000, 3000],
				                   [1000, 2000, 3000]]
				exits = [1000, 1000, 1]
				system = IterativeSystem3(entries, stations, transitions_1_2, transitions_2_3, exits)

				(optimal_time, _) = system.get_optimal_time()

				assert optimal_time == 1 + 1 + 2 + 3 + 4 + 1

			def test_with_transitions(self):
				entries = [10, 1000, 1000]
				stations = [[   1, 2000, 3000, 4000],
				            [1000,    2, 3000,    4],
				            [1000, 2000,    3, 4000]]
				transitions_1_2 = [[10, 20, 30],
				                   [10, 20, 30],
				                   []]
				transitions_2_3 = [[],
				                   [10, 20, 30],
				                   [10, 20, 30]]
				exits = [1000, 10, 1000]
				system = IterativeSystem3(entries, stations, transitions_1_2, transitions_2_3, exits)

				(optimal_time, _) = system.get_optimal_time()

				assert optimal_time == 10 + 1 + 10 + 2 + 20 + 3 + 30 + 4 + 10

		class TestGettingPath:
			def test_best_path_being_line_1(self):
				entries = [1, 1000, 1000]
				stations = [[   1,    2,    3,    4],
				            [1000, 2000, 3000, 4000],
				            [1000, 2000, 3000, 4000]]
				transitions_1_2 = [[1000, 2000, 3000],
				                   [1000, 2000, 3000],
				                   []]
				transitions_2_3 = [[],
				                   [1000, 2000, 3000],
				                   [1000, 2000, 3000]]
				exits = [1, 1000, 1000]
				system = IterativeSystem3(entries, stations, transitions_1_2, transitions_2_3, exits)

				(_, optimal_path) = system.get_optimal_time()

				assert optimal_path == [(0, 0), (0, 1), (0, 2), (0, 3)]


			def test_best_path_being_line_3(self):
				entries = [1000, 1000, 1]
				stations = [[1000, 2000, 3000, 4000],
				            [1000, 2000, 3000, 4000],
				            [   1,    2,    3,    4]]
				transitions_1_2 = [[1000, 2000, 3000],
				                   [1000, 2000, 3000],
				                   []]
				transitions_2_3 = [[],
				                   [1000, 2000, 3000],
				                   [1000, 2000, 3000]]
				exits = [1000, 1000, 1]
				system = IterativeSystem3(entries, stations, transitions_1_2, transitions_2_3, exits)

				(_, optimal_path) = system.get_optimal_time()

				assert optimal_path == [(2, 0), (2, 1), (2, 2), (2, 3)]

			def test_with_transitions(self):
				entries = [10, 1000, 1000]
				stations = [[   1, 2000, 3000, 4000],
				            [1000,    2, 3000,    4],
				            [1000, 2000,    3, 4000]]
				transitions_1_2 = [[10, 20, 30],
				                   [10, 20, 30],
				                   []]
				transitions_2_3 = [[],
				                   [10, 20, 30],
				                   [10, 20, 30]]
				exits = [1000, 10, 1000]
				system = IterativeSystem3(entries, stations, transitions_1_2, transitions_2_3, exits)

				(_, optimal_path) = system.get_optimal_time()

				assert optimal_path == [(0, 0), (1, 1), (2, 2), (1, 3)]


class TestRecursiveSystem:
	class TestTwoAssemblyLines:
		class TestGettingTime:
			def test_best_path_being_line_1(self):
				entries = [1, 1000]
				stations = [[1, 2, 3], [1000, 2000, 3000]]
				transitions = [[1000, 1000], [1000, 2000]]
				exits = [1, 1000]
				system = RecursiveSystem(entries, stations, transitions, exits)

				(optimal_time, _) = system.get_optimal_time()

				assert optimal_time == 1 + 1 + 2 + 3 + 1

			def test_best_path_being_line_2(self):
				entries = [1000, 1]
				stations = [[1000, 2000, 3000], [1, 2, 3]]
				transitions = [[1000, 1000], [1000, 2000]]
				exits = [1000, 1]
				system = RecursiveSystem(entries, stations, transitions, exits)

				(optimal_time, _) = system.get_optimal_time()

				assert optimal_time == 1 + 1 + 2 + 3 + 1

			def test_with_transitions(self):
				entries = [10, 1000]
				stations = [[1, 2000, 3], [1000, 2, 3000]]
				transitions = [[10, 20], [10, 20]]
				exits = [10, 1000]
				system = RecursiveSystem(entries, stations, transitions, exits)

				(optimal_time, _) = system.get_optimal_time()

				assert optimal_time == 10 + 1 + 10 + 2 + 20 + 3 + 10

			def test_a_system_more_difficult_to_get_optimal_time(self):
				entries = [1, 1]
				stations = [[1, 2000, 3], [1000, 2, 3000]]
				transitions = [[10, 20], [10, 20]]
				exits = [10, 1000]
				system = RecursiveSystem(entries, stations, transitions, exits)

				(optimal_time, _) = system.get_optimal_time()

				assert optimal_time == 1 + 1 + 10 + 2 + 20 + 3 + 10

		class TestGettingPath:
			def test_best_path_being_line_1(self):
				entries = [1, 1000]
				stations = [[1, 2, 3], [1000, 2000, 3000]]
				transitions = [[1000, 1000], [1000, 2000]]
				exits = [1, 1000]
				system = RecursiveSystem(entries, stations, transitions, exits)

				(_, optimal_path) = system.get_optimal_time()

				assert optimal_path == [(0, 0), (0, 1), (0, 2)]

			def test_best_path_being_line_2(self):
				entries = [1000, 1]
				stations = [[1000, 2000, 3000], [1, 2, 3]]
				transitions = [[1000, 1000], [1000, 2000]]
				exits = [1000, 1]
				system = RecursiveSystem(entries, stations, transitions, exits)

				(_, optimal_path) = system.get_optimal_time()

				assert optimal_path == [(1, 0), (1, 1), (1, 2)]

			def test_with_transitions(self):
				entries = [10, 1000]
				stations = [[1, 2000, 3000], [1000, 2, 3]]
				transitions = [[10, 20], [10, 20]]
				exits = [10, 1000]
				system = RecursiveSystem(entries, stations, transitions, exits)

				(_, optimal_path) = system.get_optimal_time()

				assert optimal_path == [(0, 0), (1, 1), (1, 2)]

			def test_bigger_system(self):
				entries = [10, 12]
				stations = [[4, 5, 3, 2], [2, 10, 1, 4]]
				transitions = [[7, 4, 5], [9, 2, 8]]
				exits = [18, 7]
				system = RecursiveSystem(entries, stations, transitions, exits)

				(_, optimal_path) = system.get_optimal_time()

				assert optimal_path == [(0, 0), (0, 1), (1, 2), (1, 3)]

	class TestThreeAssemblyLines:
		class TestGettingTime:
			def test_best_path_being_line_1(self):
				entries = [1, 1000, 1000]
				stations = [[   1,    2,    3,    4],
				            [1000, 2000, 3000, 4000],
				            [1000, 2000, 3000, 4000]]
				transitions_1_2 = [[1000, 2000, 3000],
				                   [1000, 2000, 3000],
				                   []]
				transitions_2_3 = [[],
				                   [1000, 2000, 3000],
				                   [1000, 2000, 3000]]
				exits = [1, 1000, 1000]
				system = RecursiveSystem3(entries, stations, transitions_1_2, transitions_2_3, exits)

				(optimal_time, _) = system.get_optimal_time()

				assert optimal_time == 1 + 1 + 2 + 3 + 4 + 1


			def test_best_path_being_line_3(self):
				entries = [1000, 1000, 1]
				stations = [[1000, 2000, 3000, 4000],
				            [1000, 2000, 3000, 4000],
				            [   1,    2,    3,    4]]
				transitions_1_2 = [[1000, 2000, 3000],
				                   [1000, 2000, 3000],
				                   []]
				transitions_2_3 = [[],
				                   [1000, 2000, 3000],
				                   [1000, 2000, 3000]]
				exits = [1000, 1000, 1]
				system = RecursiveSystem3(entries, stations, transitions_1_2, transitions_2_3, exits)

				(optimal_time, _) = system.get_optimal_time()

				assert optimal_time == 1 + 1 + 2 + 3 + 4 + 1

			def test_with_transitions(self):
				entries = [10, 1000, 1000]
				stations = [[   1, 2000, 3000, 4000],
				            [1000,    2, 3000,    4],
				            [1000, 2000,    3, 4000]]
				transitions_1_2 = [[10, 20, 30],
				                   [10, 20, 30],
				                   []]
				transitions_2_3 = [[],
				                   [10, 20, 30],
				                   [10, 20, 30]]
				exits = [1000, 10, 1000]
				system = RecursiveSystem3(entries, stations, transitions_1_2, transitions_2_3, exits)

				(optimal_time, _) = system.get_optimal_time()

				assert optimal_time == 10 + 1 + 10 + 2 + 20 + 3 + 30 + 4 + 10

		class TestGettingPath:
			def test_best_path_being_line_1(self):
				entries = [1, 1000, 1000]
				stations = [[   1,    2,    3,    4],
				            [1000, 2000, 3000, 4000],
				            [1000, 2000, 3000, 4000]]
				transitions_1_2 = [[1000, 2000, 3000],
				                   [1000, 2000, 3000],
				                   []]
				transitions_2_3 = [[],
				                   [1000, 2000, 3000],
				                   [1000, 2000, 3000]]
				exits = [1, 1000, 1000]
				system = RecursiveSystem3(entries, stations, transitions_1_2, transitions_2_3, exits)

				(_, optimal_path) = system.get_optimal_time()

				assert optimal_path == [(0, 0), (0, 1), (0, 2), (0, 3)]


			def test_best_path_being_line_3(self):
				entries = [1000, 1000, 1]
				stations = [[1000, 2000, 3000, 4000],
				            [1000, 2000, 3000, 4000],
				            [   1,    2,    3,    4]]
				transitions_1_2 = [[1000, 2000, 3000],
				                   [1000, 2000, 3000],
				                   []]
				transitions_2_3 = [[],
				                   [1000, 2000, 3000],
				                   [1000, 2000, 3000]]
				exits = [1000, 1000, 1]
				system = RecursiveSystem3(entries, stations, transitions_1_2, transitions_2_3, exits)

				(_, optimal_path) = system.get_optimal_time()

				assert optimal_path == [(2, 0), (2, 1), (2, 2), (2, 3)]

			def test_with_transitions(self):
				entries = [10, 1000, 1000]
				stations = [[   1, 2000, 3000, 4000],
				            [1000,    2, 3000,    4],
				            [1000, 2000,    3, 4000]]
				transitions_1_2 = [[10, 20, 30],
				                   [10, 20, 30],
				                   []]
				transitions_2_3 = [[],
				                   [10, 20, 30],
				                   [10, 20, 30]]
				exits = [1000, 10, 1000]
				system = RecursiveSystem3(entries, stations, transitions_1_2, transitions_2_3, exits)

				(_, optimal_path) = system.get_optimal_time()

				assert optimal_path == [(0, 0), (1, 1), (2, 2), (1, 3)]
