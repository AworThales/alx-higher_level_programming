#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *p5;
	listint_t *pre;

	p5 = list;
	pre = list;
	while (list && p5 && p5->next)
	{
		list = list->next;
		p5 = p5->next->next;

		if (list == p5)
		{
			list = pre;
			pre =  p5;
			while (1)
			{
				p5 = pre;
				while (p5->next != list && p5->next != pre)
				{
					p5 = p5->next;
				}
				if (p5->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
