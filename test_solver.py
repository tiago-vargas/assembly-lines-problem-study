import pytest

from solver import AssemblyLine, System


class TestPathChecker:
	def test_system_single_line(self):
		a = AssemblyLine(name='A', n=3)
		path = [a[0], a[1], a[2]]
		system = System(assembly_lines=[a])

		assert system.is_valid(path)

	def test_raising_error_when_invalid_subscript(self):
		a = AssemblyLine(name='A', n=3)

		with pytest.raises(IndexError):
			path = [a[0], a[1], a[2], a[3]]

	def test_classifying_path_with_too_few_nodes_as_invalid(self):
		a = AssemblyLine(name='A', n=10)
		path = [a[0], a[1], a[2]]
		system = System(assembly_lines=[a])

		assert not system.is_valid(path)
