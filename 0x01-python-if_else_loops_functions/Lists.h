#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
/**
 * struct listint_s - the singly linked list
 * @n: the integer
 * @next: it points to the next node
 *
 * Description: singly linked list node struc
 *
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listinte_t;

size_t print_listint(const listinte_t *h);
listinte_t *add_nodeint_end(listinte_t **head, const int n);
void free_listint(listinte_t *head);

listinte_t *insert_node(listinte_t **head, int number);

#endif /* LISTS_H */
