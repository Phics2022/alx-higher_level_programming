#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
  *insert_node - insert a node
  *@head: head pointer
  *@number: number
  *
  *Return: NULL or address
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = malloc(sizeof(listint_t));
	listint_t *temp2;
	if (temp == NULL)
		return (NULL);
	temp->n = number;
	temp->next = NULL;
	if (*head == NULL)
	{
		*head = temp;
		return (temp);
	}
	temp2 = *head;
	while (temp2->next != NULL)
	{
		temp2 = temp2->next;
	}
	temp2->next = temp;
	return (temp);
}
