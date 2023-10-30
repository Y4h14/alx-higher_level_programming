#include "lists.h"
/**
 * find_listint_loop - finds a loop in alinked list
 * @head: the first node in a list
 * Return: the adress of the node where the loop start or NULL
 */
int check_cycle(listint_t *list)
{
	listint_t *p1, *p2;

	if (list == NULL)
		return (NULL);
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
