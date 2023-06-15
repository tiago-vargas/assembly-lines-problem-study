class AssemblyLine:
	def __init__(self, name: str, n: int) -> None:
		self.name = name
		self.n = n

	def __getitem__(self, index) -> str | None:
		if 0 <= index < self.n:
			return f'{self.name}_{index}'
		else:
			raise IndexError(f'Expected indices: [0, {self.n - 1}]; got {index}')


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

		are_in_bounds = (len(path) == self.assembly_lines[0].n)
		if _are_consecutive(indices) and are_in_bounds:
			return True
		else:
			return False
