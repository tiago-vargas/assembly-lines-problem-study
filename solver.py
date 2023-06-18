from typing import Callable, TypeVar


class AssemblyLine:
	def __init__(self, name: str, nodes: int) -> None:
		self.name = name
		self.nodes = nodes

	def __getitem__(self, index) -> str | None:
		if 0 <= index < self.nodes:
			return f'{self.name}_{index}'
		else:
			raise IndexError(f'Expected indices for {self.name}: [0, {self.nodes - 1}]; got {index}')


class System:
	def __init__(self, assembly_lines: list[AssemblyLine]) -> None:
		self.assembly_lines = assembly_lines

		assembly_lines_are_of_the_same_length = obeys_pattern(assembly_lines, lambda x, y: x.nodes == y.nodes)
		if not assembly_lines_are_of_the_same_length:
			raise DifferentNumberOfNodesError

	def is_valid(self, path: list[str]) -> bool:
		node_indices = []
		for string in path:
			index: str = string.split('_')[-1]
			index: int = int(index)
			node_indices.append(index)

		indices_are_in_succession = obeys_pattern(node_indices, lambda x, y: x == y + 1)
		if not indices_are_in_succession:
			return False

		# In which line are we now?
		line_name_sequence = []
		for string in path:
			name = string.split('_')[0]
			line_name_sequence.append(name)

		# The indices of each line in the system
		line_index_sequence = []
		for name in line_name_sequence:
			assembly_line_names = [x.name for x in self.assembly_lines]
			index: int = assembly_line_names.index(name)
			line_index_sequence.append(index)

		transitions_are_adjacent = obeys_pattern(line_index_sequence, lambda x, y: y - 1 <= x <= y + 1)
		transitions_are_valid = transitions_are_adjacent
		if not transitions_are_valid:
			return False

		some_assembly_line = self.assembly_lines[0]  # Could've been any other line
		have_as_many_items_as_there_are_nodes = (len(path) == some_assembly_line.nodes)
		if have_as_many_items_as_there_are_nodes:
			return True
		else:
			return False


T = TypeVar('T')


def obeys_pattern(sequence: list[T], criteria: Callable[[T, T], bool]) -> bool:
	if sequence == []:
		return True

	previous_value = sequence[0]
	for value in sequence[1:]:
		if not criteria(value, previous_value):
			return False
		# Defer:
		previous_value = value

	return True


class DifferentNumberOfNodesError(Exception):
	pass
