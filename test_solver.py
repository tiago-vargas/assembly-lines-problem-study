from solver import IterativeSystem, RecursiveSystem


class TestIterativeSystem:
	def test_best_path_being_line_1(self):
		entries = [1, 1000]
		stations = [[1, 2, 3], [1000, 2000, 3000]]
		transitions = [[1000, 1000], [1000, 2000]]
		exits = [1, 1000]
		system = IterativeSystem(entries, stations, transitions, exits)

		optimal_time = system.get_optimal_time()

		assert optimal_time == 1 + 1 + 2 + 3 + 1

	def test_best_path_being_line_2(self):
		entries = [1000, 1]
		stations = [[1000, 2000, 3000], [1, 2, 3]]
		transitions = [[1000, 1000], [1000, 2000]]
		exits = [1000, 1]
		system = IterativeSystem(entries, stations, transitions, exits)

		optimal_time = system.get_optimal_time()

		assert optimal_time == 1 + 1 + 2 + 3 + 1

	def test_with_transitions(self):
		entries = [10, 1000]
		stations = [[1, 2000, 3], [1000, 2, 3000]]
		transitions = [[10, 20], [10, 20]]
		exits = [10, 1000]
		system = IterativeSystem(entries, stations, transitions, exits)

		optimal_time = system.get_optimal_time()

		assert optimal_time == 10 + 1 + 10 + 2 + 20 + 3 + 10

	def test_a_system_more_difficult_to_get_optimal_time(self):
		entries = [1, 1]
		stations = [[1, 2000, 3], [1000, 2, 3000]]
		transitions = [[10, 20], [10, 20]]
		exits = [10, 1000]
		system = IterativeSystem(entries, stations, transitions, exits)

		optimal_time = system.get_optimal_time()

		assert optimal_time == 1 + 1 + 10 + 2 + 20 + 3 + 10


class TestRecursiveSystem:
	def test_best_path_being_line_1(self):
		entries = [1, 1000]
		stations = [[1, 2, 3], [1000, 2000, 3000]]
		transitions = [[1000, 1000], [1000, 2000]]
		exits = [1, 1000]
		system = RecursiveSystem(entries, stations, transitions, exits)

		optimal_time = system.get_optimal_time()

		assert optimal_time == 1 + 1 + 2 + 3 + 1

	def test_best_path_being_line_2(self):
		entries = [1000, 1]
		stations = [[1000, 2000, 3000], [1, 2, 3]]
		transitions = [[1000, 1000], [1000, 2000]]
		exits = [1000, 1]
		system = RecursiveSystem(entries, stations, transitions, exits)

		optimal_time = system.get_optimal_time()

		assert optimal_time == 1 + 1 + 2 + 3 + 1

	def test_with_transitions(self):
		entries = [10, 1000]
		stations = [[1, 2000, 3], [1000, 2, 3000]]
		transitions = [[10, 20], [10, 20]]
		exits = [10, 1000]
		system = RecursiveSystem(entries, stations, transitions, exits)

		optimal_time = system.get_optimal_time()

		assert optimal_time == 10 + 1 + 10 + 2 + 20 + 3 + 10

	def test_a_system_more_difficult_to_get_optimal_time(self):
		entries = [1, 1]
		stations = [[1, 2000, 3], [1000, 2, 3000]]
		transitions = [[10, 20], [10, 20]]
		exits = [10, 1000]
		system = RecursiveSystem(entries, stations, transitions, exits)

		optimal_time = system.get_optimal_time()

		assert optimal_time == 1 + 1 + 10 + 2 + 20 + 3 + 10
