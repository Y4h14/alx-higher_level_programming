#ifndef LISTS_H
#define LISTS_H
#include <stddef.h>
typedef struct listint_t *nodeptr;
/**
* struct listint_t - a linked list implementation
* @n: the value of the node (int)
* @next: pointer to the next node
*/
struct listint_t
{
	int n;
	nodeptr next;
};
typedef struct listint_t listint_t;

int check_cycle(listint_t *list);

#endif
