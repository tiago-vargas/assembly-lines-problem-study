import pytest

from solver import AssemblyLine, System


class TestPathValidator:
	class TestSystemWithSingleAssemblyLine:
		def test_system_single_line_with_consecutive_nodes(self):
			a = AssemblyLine(name='A', nodes=3)
			system = System(assembly_lines=[a])

			path = [a[0], a[1], a[2]]

			assert system.is_valid(path)

		def test_system_single_line_with_nodes_in_reverse_order(self):
			a = AssemblyLine(name='A', nodes=3)
			system = System(assembly_lines=[a])

			path = [a[2], a[1], a[0]]

			assert not system.is_valid(path)

		def test_system_single_line_with_nodes_in_wrong_order(self):
			a = AssemblyLine(name='A', nodes=5)
			system = System(assembly_lines=[a])

			path = [a[2], a[0], a[4], a[1], a[3]]

			assert not system.is_valid(path)

		def test_raising_error_when_invalid_subscript(self):
			a = AssemblyLine(name='A', nodes=3)

			with pytest.raises(IndexError):
				path = [a[0], a[1], a[2], a[3]]

		def test_classifying_path_with_too_few_nodes_as_invalid(self):
			a = AssemblyLine(name='A', nodes=10)
			system = System(assembly_lines=[a])

			path = [a[0], a[1], a[2]]

			assert not system.is_valid(path)

		def test_repeating_nodes_as_invalid(self):
			a = AssemblyLine(name='A', nodes=3)
			system = System(assembly_lines=[a])

			path = [a[0], a[0], a[1]]

			assert not system.is_valid(path)

	class TestSystemWithTwoAssemblyLines:
		def test_if_nodes_are_consecutive(self):
			a = AssemblyLine(name='A', nodes=4)
			b = AssemblyLine(name='B', nodes=4)
			system = System(assembly_lines=[a, b])

			path = [a[0], b[1], b[2], a[3]]

			assert system.is_valid(path)
