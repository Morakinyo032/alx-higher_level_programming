#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * list_len - Finds the number of nodes in a singly linked list
 * @list: Pointer to the head node
 *
 * Return: Number of nodes in the list
 */
size_t list_len(listint_t *list)
{
	listint_t *ptr;
	size_t len;

	if (list == NULL)
		return (0);
	len = 0;
	ptr = list;
	while (ptr != NULL)
	{
		len++;
		ptr = ptr->next;
	}
	return (len);
}
/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: Pointer to head node
 *
 * Return: 0 if there is no cycle or 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr, *ptr1;

	if (list == NULL)
		return (0);
	ptr = list;
	ptr1 = list;
	while (ptr != NULL)
	{
		ptr = ptr->next;
		if (ptr == ptr1)
			return (1);
	}
	return (0);
}
