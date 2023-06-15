class AssemblyLine:
	def __init__(self, name: str, nodes: int) -> None:
		self.name = name
		self.nodes = nodes

	def __getitem__(self, index) -> str | None:
		if 0 <= index < self.nodes:
			return f'{self.name}_{index}'
		else:
			raise IndexError(f'Expected indices for {self.name}: [0, {self.nodes - 1}]; got {index}')


def _are_consecutive(numbers: list[int]) -> bool:
	if numbers == []:
		return True

	previous_n = numbers[0]
	for n in numbers[1:]:
		if n != previous_n + 1:
			return False
		# Defer:
		previous_n = n

	return True


class System:
	def __init__(self, assembly_lines: list[AssemblyLine]) -> None:
		self.assembly_lines = assembly_lines

		if not self._are_lines_of_the_same_length():
			raise DifferentNumberOfNodesError

	def _are_lines_of_the_same_length(self):
		if self.assembly_lines == []:
			return True

		previous_line = self.assembly_lines[0]
		for line in self.assembly_lines[1:]:
			if line.nodes != previous_line.nodes:
				return False
			# Defer:
			previous_line = line

		return True

	def is_valid(self, path: list[str]) -> bool:
		indices = []
		for string in path:
			index = string.split('_')[-1]
			index = int(index)
			indices.append(index)

		line_name_sequence = []
		for string in path:
			name = string.split('_')[0]
			line_name_sequence.append(name)

		line_index_sequence = []
		for name in line_name_sequence:
			assembly_line_names = [x.name for x in self.assembly_lines]
			index = assembly_line_names.index(name)
			line_index_sequence.append(index)

		if not self.are_jumps_adjacent(line_index_sequence):
			return False

		have_as_many_items_as_there_are_nodes = (len(path) == self.assembly_lines[0].nodes)
		if _are_consecutive(indices) and have_as_many_items_as_there_are_nodes:
			return True
		else:
			return False

	def are_jumps_adjacent(self, line_index_sequence):
		if line_index_sequence == []:
			return True

		previous_index = line_index_sequence[0]
		for index in line_index_sequence[1:]:
			if previous_index - 1 > index or index > previous_index + 1:
				return False
			# Defer:
			previous_index = index

		return True


class DifferentNumberOfNodesError(Exception):
	pass
