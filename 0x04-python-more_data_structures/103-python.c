#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "listobject.h"
#include <object.h>
#include <bytesobject.h>
/**
 * print_python_bytes - Prints basic info on python bytes object
 * @p: Pointer to python object
 *
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	int i;
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == NULL)
		printf("[ERROR] Invalid Bytes Object\n");
	else
	{
		printf("size: %li\ntrying string:\
				%s\nfirst %li bytes: ", PyBytes_GET_SIZE(p), \
				PyBytes_AS_STRING(p), PyBytes_GET_SIZE(p) + 1);
		for (i = 0; i < PyBytes_GET_SIZE(p) + 1; i++)
			printf("%x", (p->ob_item)[i]);
		printf("\n");
	}
}
/**
 * print_python_list - Prints bsic info on python list
 * @p: Pointer to python object
 *
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	PyListObject *obj = (PyListObject *) p;
	int i;
	printf("[*] Python list info\n\
			[*] Size of Python List = %li\n\
			[*] Allocated = %li\n", PyList_Size(p), obj->allocated);
	for (i = 0; i < Py_SIZE(p); i++)
	{
		char *type =  PyTYPE((obj->ob_item)[i]);
		printf("Element %i: %s\n", i,);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes((obj->ob_item)[i])
	}
}
