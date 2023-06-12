#include <Python.h>

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
    int list_size, allocated_size, i;
    PyObject *obj;

    list_size = Py_SIZE(p);
    allocated_size= ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", allocated_size);

    for (i = 0; i < size; i++)
    {
        printf("Element %d: ", i);

        obj = PyList_GetItem(p, i);
        printf("%s\n", Py_TYPE(obj)->tp_name);
    }
}