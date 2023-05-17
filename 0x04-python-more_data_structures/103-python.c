#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *strin;
	long int size, t, limits;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	strin = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying strin: %s\n", strin);

	if (size >= 10)
		limits = 10;
	else
		limits = size + 1;

	printf("  first %ld bytes:", limits);

	for (t = 0; t < limits; t++)
		if (strin[t] >= 0)
			printf(" %02x", strin[t]);
		else
			printf(" %02x", 256 + strin[t]);

	printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int size, t;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (t = 0; t < size; t++)
	{
		obj = ((PyListObject *)p)->ob_item[t];
		printf("Element %ld: %s\n", t, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
