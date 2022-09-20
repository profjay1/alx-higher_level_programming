#include "lists.h"

/**
 * kd
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;
	if (temp == NULL || new->n <= temp->n)
	{
		new->next = temp;
		return (*head = new);
	}
	while (temp)
	{
		if (temp->next == NULL || new->n <= temp->next->n)
		{
			new->next = temp->next;
			temp->next = new;
			return (temp);
		}
		temp = temp->next;
	}
	return (NULL);
}
