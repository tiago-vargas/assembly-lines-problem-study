import pytest

from solver import AssemblyLine, System


class TestPathValidator:
	class TestSystemWithSingleAssemblyLine:
		def test_system_single_line_with_consecutive_nodes(self):
			a = AssemblyLine(name='A', nodes=3)
			path = [a[0], a[1], a[2]]
			system = System(assembly_lines=[a])

			assert system.is_valid(path)

		def test_system_single_line_with_nodes_in_reverse_order(self):
			a = AssemblyLine(name='A', nodes=3)
			path = [a[2], a[1], a[0]]
			system = System(assembly_lines=[a])

			assert not system.is_valid(path)

		def test_system_single_line_with_nodes_in_wrong_order(self):
			a = AssemblyLine(name='A', nodes=5)
			path = [a[2], a[0], a[4], a[1], a[3]]
			system = System(assembly_lines=[a])

			assert not system.is_valid(path)

		def test_raising_error_when_invalid_subscript(self):
			a = AssemblyLine(name='A', nodes=3)

			with pytest.raises(IndexError):
				path = [a[0], a[1], a[2], a[3]]

		def test_classifying_path_with_too_few_nodes_as_invalid(self):
			a = AssemblyLine(name='A', nodes=10)
			path = [a[0], a[1], a[2]]
			system = System(assembly_lines=[a])

			assert not system.is_valid(path)

		def test_repeating_nodes_as_invalid(self):
			a = AssemblyLine(name='A', nodes=3)
			path = [a[0], a[0], a[1]]
			system = System(assembly_lines=[a])

			assert not system.is_valid(path)
