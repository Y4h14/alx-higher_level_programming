#include "lists.h"
#include <stdlib.h>
/**
 * reverse_listint - reverses a listint_t
 * @head: pointer the the header node
 * Return: pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{

	listint_t *next, *prev = NULL;

	if (head == NULL || *head == NULL)
		return (NULL);


	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = (*head);
		(*head) = next;
	}
	*head = prev;

	return (*head);
}
/**
 * is_palindrome - check is a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if its not a palindrome and 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *next = *head, *tail = *head;
	listint_t *alt = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	/* making an alternative list */
	while (1)
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
	while (alt && temp)
	{
		if (temp->n == alt->n)
		{
			temp = temp->next;
			alt = alt->next;
		}
		else
			return (0);
	}
	if (!alt)
		return (1);

	return (0);
}
