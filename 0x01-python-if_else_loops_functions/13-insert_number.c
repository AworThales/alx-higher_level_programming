#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 *
 * @head: Double pointer to a singly linked list
 *
 * @number: Value of the new node.
 *
 * Return: The address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	int push = 0;
	listint_t *start_node = NULL, *real = NULL, *after = NULL;

	if (head == NULL)
		return (NULL);
	start_node = malloc(sizeof(listint_t));
	if (!start_node)
		return (NULL);
	start_node->n = number, start_node->next = NULL;
	if (*head == NULL)
	{
		*head = start_node;
		return (*head);
	}
	real = *head;
	if (number <= real->n)
	{
		start_node->next = real, *head = start_node;
		return (*head);
	}
	if (number > real->n && !real->next)
	{
		real->next = start_node;
		return (start_node);
	}
	after = real->next;
	while (real)
	{
		if (!after)
			real->next = start_node, push = 1;
		else if (after->n == number)
			real->next = start_node, start_node->next = after, push = 1;
		else if (after->n > number && real->n < number)
			real->next = start_node, start_node->next = after, push = 1;
		if (push)
			break;
		after = after->next, real = real->next;
	}
	return (start_node);
}
