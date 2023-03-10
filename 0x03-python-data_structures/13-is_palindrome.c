#include <stddef.h>
#include "lists.h"
/**
 * list_len - Finds the number of node in a singly linked list
 * @head: Head pointer
 *
 * Return: Number of nodes
 */
int list_len(listint_t *head)
{
	listint_t *ptr;
	int len;

	len = 0;
	ptr = head;
	while (ptr != NULL)
	{
		len += 1;
		ptr = ptr->next;
	}
	return (len);
}
/**
 * is_palindrome - checks if a singly linked list is palindrome
 * @head: Pointer to head pointer
 *
 * Return: 1 if true, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *ptr1;
	int len, i, j;

	len = list_len(*head);
	if (len == 1)
		return (1);
	if (*head == NULL)
		return (1);
	ptr = *head;
	for (i = 1; i <= len / 2; i++)
	{
		ptr1 = ptr;
		for (j = i; j <= len - i; j++)
		{
			ptr1 = ptr1->next;
		}
		if (ptr->n != ptr1->n)
			return (0);
		ptr = ptr->next;
	}
	return (1);
}
