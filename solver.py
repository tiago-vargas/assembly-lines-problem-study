class AssemblyLine:
	def __init__(self, name: str, n: int) -> None:
		pass


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
		pass

	def is_valid(self, path: list[str]) -> bool:
		indices = []
		for string in path:
			index = string.split('_')[-1]
			index = int(index)
			indices.append(index)

		if _are_consecutive(indices):
			return True
		else:
			return False
