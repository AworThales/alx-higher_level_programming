#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints python list info
 *
 * @p: PyObject
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	long int sisez, t;
	PyListObject *list;
	PyObject *item;

	sisez = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", sisez);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (t = 0; t < sisez; t++)
	{
		item = PyList_GetItem(p, t);
		printf("Element %ld: %s\n", t, Py_TYPE(item)->tp_name);
	}
}
