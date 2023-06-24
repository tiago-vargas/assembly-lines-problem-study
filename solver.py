class RecursiveSystem:
	def __init__(self, entries: list[int], stations: list[list[int]], transitions: list[list[int]], exits: list[int]) -> None:
		self.entries = entries
		self.stations = stations
		self.transitions = transitions
		self.exits = exits

		any_of_the_stations = self.stations[0]
		n = len(any_of_the_stations)
		self.memoire = [[0] * n, [0] * n]

	def get_optimal_time(self) -> int:
		n = len(self.stations[0])
		last_station_index = n - 1
		return min(self.optimal_time_to_get_to_station(0, last_station_index) + self.exits[0],
		           self.optimal_time_to_get_to_station(1, last_station_index) + self.exits[1])

	def optimal_time_to_get_to_station(self, line: int, index: int) -> int:
		if self.memoire[line][index] != 0:
			return self.memoire[line][index]

		is_first_station = (index == 0)
		if is_first_station:
			self.memoire[line][index] = self.entries[line] + self.stations[line][0]
		else:
			other_line = 1 - line
			self.memoire[line][index] = min(self.optimal_time_to_get_to_station(line, index - 1) + self.stations[line][index],
			                                self.optimal_time_to_get_to_station(other_line, index - 1) + self.transitions[other_line][index - 1] + self.stations[line][index])

		return self.memoire[line][index]
