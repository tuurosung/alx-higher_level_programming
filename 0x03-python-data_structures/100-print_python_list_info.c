#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - a function that prints the details
 * of a python list ie number of elements, mem allocated
 *
 * @p: the address of the PyObject
 *
 * Return: void.
*/
void print_python_list_info(PyObject *p)
{
    long int list_size = PyList_Size(p);
    int i;
    PyListObject *obj = (PyListObject *)p;

    printf("[*] Size of the Python List = %li\n", list_size);
    printf("[*] Allocated = %li\n", obj->allocated);
    for (i = 0; i < list_size; i++)
        printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}