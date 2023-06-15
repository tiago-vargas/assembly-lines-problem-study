class AssemblyLine:
	def __init__(self, name: str, nodes: int) -> None:
		self.name = name
		self.nodes = nodes

	def __getitem__(self, index) -> str | None:
		if 0 <= index < self.nodes:
			return f'{self.name}_{index}'
		else:
			raise IndexError(f'Expected indices: [0, {self.nodes - 1}]; got {index}')


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

	def is_valid(self, path: list[str]) -> bool:
		indices = []
		for string in path:
			index = string.split('_')[-1]
			index = int(index)
			indices.append(index)

		have_as_many_items_as_there_are_nodes = (len(path) == self.assembly_lines[0].nodes)
		if _are_consecutive(indices) and have_as_many_items_as_there_are_nodes:
			return True
		else:
			return False
