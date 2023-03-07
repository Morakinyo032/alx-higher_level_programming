#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to head pointer
 * @number: New node data
 *
 * Return: The addrress of the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new, *ptr1;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	ptr = *head;
	if (ptr == NULL)
	{
		*head = new;
		return (new);
	}
	else
	{
		while (ptr != NULL)
		{
			if (ptr->n > new->n)
			{
				if (ptr1 == NULL)
				{
					new->next = ptr;
					*head = new;
					return (new);
				}
				else
				{
					new->next = ptr;
					if (ptr == *head)
						*head = new;
					else
						ptr1->next = new;
					return (new);
				}
			}
			ptr1 = ptr;
			ptr = ptr->next;
		}
		ptr1->next = new;
		return (new);
	}
}
