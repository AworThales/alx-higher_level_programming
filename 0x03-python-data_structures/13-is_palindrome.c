#include "lists.h"

/**
 * reverse - reverses the second half of the list
 *
 * @h_r: head of the second half
 * Return: no return
 */
void reverse(listint_t **h_r)
{
	listint_t *previ;
	listint_t *curre;
	listint_t *move;

	previ = NULL;
	curre = *h_r;

	while (curre != NULL)
	{
		move = curre->next;
		curre->next = previ;
		previ = curre;
		curre = move;
	}

	*h_r = previ;
}

/**
 * compare - compares each int of the list
 *
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if are equals, 0 if not
 */
int compare(listint_t *h1, listint_t *h2)
{
	listint_t *tmp_one;
	listint_t *tmp_two;

	tmp_one = h1;
	tmp_two = h2;

	while (tmp_one != NULL && tmp_two != NULL)
	{
		if (tmp_one->n == tmp_two->n)
		{
			tmp_one = tmp_one->next;
			tmp_two = tmp_two->next;
		}
		else
		{
			return (0);
		}
	}

	if (tmp_one == NULL && tmp_two == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slows, *moving, *slo_pre;
	listint_t *scn_half, *center;
	int ispir;

	slows = moving = slo_pre = *head;
	center = NULL;
	ispir = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (moving != NULL && moving->next != NULL)
		{
			moving = moving->next->next;
			slo_pre = slows;
			slows = slows->next;
		}

		if (moving != NULL)
		{
			center = slows;
			slows = slows->next;
		}

		scn_half = slows;
		slo_pre->next = NULL;
		reverse(&scn_half);
		ispir = compare(*head, scn_half);

		if (center != NULL)
		{
			slo_pre->next = center;
			center->next = scn_half;
		}
		else
		{
			slo_pre->next = scn_half;
		}
	}

	return (ispir);
}
