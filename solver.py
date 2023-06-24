class IterativeSystem:
	def __init__(self, entries: list[int], stations: list[list[int]], transitions: list[list[int]], exits: list[int]) -> None:
		self.entries = entries
		self.stations = stations
		self.transitions = transitions
		self.exits = exits

		n = len(self.stations[0])
		self.memoire = [[-1] * n, [-1] * n]

	def get_optimal_time(self) -> int:
		n = len(self.stations[0])
		for index in range(0, n):
			for line in [0, 1]:
				self.memoire[line][index] = self.get_optimal_time_to_get_to_station(line, index)

		return min(self.memoire[0][n - 1] + self.exits[0],
				   self.memoire[1][n - 1] + self.exits[1])

	def get_optimal_time_to_get_to_station(self, line: int, index: int) -> int:
		if index == 0:
			return self.entries[line] + self.stations[line][index]
		else:
			other_line = 1 - line
			return min(self.memoire[line][index - 1], self.memoire[other_line][index - 1] + self.transitions[other_line][index - 1]) + self.stations[line][index]


class IterativeSystem3:
	def __init__(self, entries: list[int], stations: list[list[int]], transitions_1_2: list[list[int]], transitions_2_3: list[list[int]], exits: list[int]) -> None:
		self.entries = entries
		self.stations = stations
		self.transitions_1_2 = transitions_1_2
		self.transitions_2_3 = transitions_2_3
		self.exits = exits

		n = len(self.stations[0])
		self.memoire = [[-1] * n, [-1] * n, [-1] * n]

	def get_optimal_time(self) -> int:
		n = len(self.stations[0])
		for index in range(0, n):
			for line in [0, 1, 2]:
				self.memoire[line][index] = self.get_optimal_time_to_get_to_station(line, index)

		last_station_index = n - 1
		return min(self.memoire[0][last_station_index] + self.exits[0],
				   self.memoire[1][last_station_index] + self.exits[1],
				   self.memoire[2][last_station_index] + self.exits[2])

	def get_optimal_time_to_get_to_station(self, line: int, index: int) -> int:
		if index == 0:
			return self.entries[line] + self.stations[line][index]
		else:
			if line == 0:
				return min(self.memoire[line][index - 1],
				           self.memoire[1][index - 1] + self.transitions_1_2[1][index - 1]) \
				       + self.stations[line][index]
			elif line == 1:
				return min(self.memoire[0][index - 1] + self.transitions_1_2[0][index - 1],
				           self.memoire[line][index - 1],
				           self.memoire[2][index - 1] + self.transitions_2_3[2][index - 1]) \
				       + self.stations[line][index]
			else:
				return min(self.memoire[line][index - 1],
				           self.memoire[1][index - 1] + self.transitions_2_3[1][index - 1]) \
				       + self.stations[line][index]


class RecursiveSystem:
	def __init__(self, entries: list[int], stations: list[list[int]], transitions: list[list[int]], exits: list[int]) -> None:
		self.entries = entries
		self.stations = stations
		self.transitions = transitions
		self.exits = exits

		any_of_the_stations = self.stations[0]
		n = len(any_of_the_stations)
		self.memoire = [[-1] * n, [-1] * n]

	def get_optimal_time(self) -> int:
		n = len(self.stations[0])
		last_station_index = n - 1
		return min(self.optimal_time_to_get_to_station(0, last_station_index) + self.exits[0],
		           self.optimal_time_to_get_to_station(1, last_station_index) + self.exits[1])

	def optimal_time_to_get_to_station(self, line: int, index: int) -> int:
		if self.memoire[line][index] != -1:
			return self.memoire[line][index]

		is_first_station = (index == 0)
		if is_first_station:
			self.memoire[line][index] = self.entries[line] + self.stations[line][0]
		else:
			other_line = 1 - line
			self.memoire[line][index] = min(self.optimal_time_to_get_to_station(line, index - 1) + self.stations[line][index],
			                                self.optimal_time_to_get_to_station(other_line, index - 1) + self.transitions[other_line][index - 1] + self.stations[line][index])

		return self.memoire[line][index]


class RecursiveSystem3:
	def __init__(self, entries: list[int], stations: list[list[int]], transitions_1_2: list[list[int]], transitions_2_3: list[list[int]], exits: list[int]) -> None:
		self.entries = entries
		self.stations = stations
		self.transitions_1_2 = transitions_1_2
		self.transitions_2_3 = transitions_2_3
		self.exits = exits

		any_of_the_stations = self.stations[0]
		n = len(any_of_the_stations)
		self.memoire = [[-1] * n, [-1] * n, [-1] * n]

	def get_optimal_time(self) -> int:
		n = len(self.stations[0])
		last_station_index = n - 1
		return min(self.optimal_time_to_get_to_station(0, last_station_index) + self.exits[0],
		           self.optimal_time_to_get_to_station(1, last_station_index) + self.exits[1],
		           self.optimal_time_to_get_to_station(2, last_station_index) + self.exits[2])

	# TODO: FIX!
	def optimal_time_to_get_to_station(self, line: int, index: int) -> int:
		is_in_memoire = (self.memoire[line][index] != -1)
		if is_in_memoire:
			return self.memoire[line][index]

		is_first_station = (index == 0)
		if is_first_station:
			self.memoire[line][index] = self.entries[line] + self.stations[line][0]
		else:
			if line == 0:
				self.memoire[line][index] = min(self.optimal_time_to_get_to_station(line, index - 1),
				                                self.optimal_time_to_get_to_station(1, index - 1) + self.transitions_1_2[1][index - 1]) \
				                            + self.stations[line][index]
			elif line == 1:
				self.memoire[line][index] = min(self.optimal_time_to_get_to_station(0, index - 1) + self.transitions_1_2[0][index - 1],
				                                self.optimal_time_to_get_to_station(line, index - 1),
				                                self.optimal_time_to_get_to_station(2, index - 1) + self.transitions_2_3[2][index - 1]) \
				                            + self.stations[line][index]
			else:
				self.memoire[line][index] = min(self.optimal_time_to_get_to_station(line, index - 1),
				                                self.optimal_time_to_get_to_station(1, index - 1) + self.transitions_2_3[1][index - 1]) \
				                            + self.stations[line][index]

		return self.memoire[line][index]
