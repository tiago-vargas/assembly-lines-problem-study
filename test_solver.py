from solver import AssemblyLine, System


class TestPathChecker:
	def test_system_single_single_line(self):
		a = AssemblyLine(name='A', n=3)
		path = [a[0], a[1], a[2]]
		system = System(assembly_lines=[a])

		assert system.is_valid(path)
