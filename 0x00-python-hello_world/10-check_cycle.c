#include "lists.h"
/**
 * check_cycle - finds a loop in alinked list
 * @list: the first node in a list
 * Return: 1 if a cycle found
 */
int check_cycle(listint_t *list)
{
	listint_t *p1, *p2;

	if (list == NULL)
		return (0);
	p1 = list;
	p2 = list;
	while (p1 && p2 && p1->next && p2->next)
	{
		p1 = p1->next;
		p2 = (p2->next)->next;
		if (p1 == p2)
			return (1);
	}
	return (0);
}
