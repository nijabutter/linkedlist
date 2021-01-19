#pragma once
#include <stdlib.h>
#include <stdio.h>

typedef struct Node {
    int value;
    struct Node* next;
} Node;

Node* NewNode(int value) {
    Node* new_node = malloc(sizeof(Node));    
    new_node->value = value;
    new_node->next = NULL;
    return new_node;
}

void printList(Node* head) {
    while (head != NULL) {
        printf("%d", head->value);
        if (head->next != NULL) {
            printf("->");
        }
        head = head->next;
    }
    printf("\n");
}

void genList(Node* head, int count) {
    Node* current = head;
    for (int i = head->value+1; i < head->value+count; i++) {
        current->next = NewNode(i);
        current = current->next;
    }
}
