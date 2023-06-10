#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
void add_nodeint_front(listint_t **head, const int n);
/**
  *is_palindrome - check if a lis is a palindrome
  *@head: head pointer
  *
  *Return: 0 or 1
  */
int is_palindrome(listint_t **head)
{
	listint_t *temp =  *head;
	listint_t *temp2;
	listint_t *new = NULL;
	int length = 0;
	int itr = 0;

	/*return if list is empty*/
	if (*head == NULL)
		return (0);
	/*create a reverse copy of the list and get the length*/
	while (temp != NULL)
	{
		add_nodeint_front(&new, temp->n);
		length++;
		temp = temp->next;
	}
	/*compare the two list*/
	temp = *head;
	temp2 = new;
	while (temp != NULL && temp2 != NULL)
	{
		if (temp->n == temp2->n)
		itr++;
		temp = temp->next;
		temp2 = temp2->next;
	}
	/*free the new list*/
	free_listint(new);
	/*now return the values*/
	if (itr == length)
		return (1);
	else
		return (0);
}

/**
  *add_nodeint_front - add node at the beginning
  *@head: head pointer
  *@n: value
  *
  *Return: void
  */
void add_nodeint_front(listint_t **head, const int n)
{
	listint_t *temp = malloc(sizeof(listint_t));

	temp->n = n;
	if (*head == NULL)
	{
		*head = temp;
		return;
	}
	temp->next = *head;
	*head = temp;
}
