from solver import AssemblyLine, System


class TestPathChecker:
	def test_system_single_single_line(self):
		line_a = AssemblyLine(name='A', n=3)
		# path = 'A_0 -> A_1 -> A_2'
		path = ['A_0', 'A_1', 'A_2']

		system = System(assembly_lines=[line_a])

		assert system.is_valid(path)
