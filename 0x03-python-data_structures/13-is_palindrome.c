#include "lists.h"
/**
 * is_palindrome - check is a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if its not a palindrome and 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	linstint_t *temp = *head, *next = *head, tail = *head;
	lisintint_t *alt = NULL;

	if(*head == NULL || (*head)->next == NULL)
		return (1);
	/* making an alternative list */
	while(1)
	{
		next = next->next->next;
		if (!next)
		{
			alt = tail->next;
			break;
		}
		if (!next->next)
		{
			alt = tail->next->next;
			break;
		}
		tail = tail->next;
	}
	reverse_listint(&alt);
	while(alt && temp)
	{
		if (temp->n == alt->n)
		{
			temp = tem->next;
			alt = alt->next;
		}
		else
			return (0);
	}
	if (!dup)
		return (1);

	return (0);
}
