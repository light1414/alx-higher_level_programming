#include "lists.h"

/**
 * insert_node - it inserts a numb to a sorted singly-linked list.
 * @head: Pointer the head of the linked list.
 * @number: Number to insert.
 * Return: 0 If the function fails or pointer to the new node.
 */
listinte_t *insert_node(listinte_t **head, int number)
{
	listinte_t *node = *head, *new;

	new = malloc(sizeof(listinte_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
