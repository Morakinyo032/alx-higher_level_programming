#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to singly linked list
 * Return: 1 if true or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, j, list_size;
	listint_t **buffer;

	current = *head;
	list_size = 0;
	while (current != NULL)
	{
		list_size = list_size + 1;
		current = current->next;
	}
	buffer = malloc(sizeof(listint_t *) * (list_size));
	if (buffer == NULL)
	{
		printf("malloc() error");
		return (-1);
	}
	current = *head;
	i = 0;
	while (current != NULL)
	{
		buffer[i] = current;
		current = current->next;
		i = i + 1;
	}
	for (j = 0; j < i / 2; j++)
	{
		if (buffer[j]->n != buffer[i - j - 1]->n)
			return (0);
	}
	return (1);
}
