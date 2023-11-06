#include <python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - print the info of a python list
 * @p: a python object
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	long int size = Pylist_size(s);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, PyType(obj->ob_item[i]->tp_name));
}
