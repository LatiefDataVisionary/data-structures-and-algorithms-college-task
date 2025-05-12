#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 5

void create_queue();
bool full_queue();
bool empty_queue();
void enQueue(int data);
void deQueue();
void editQueue(int index, int newData);
void printQueue();

int head, tail;
int queue[MAX];

int main()
{
    char choice;

    create_queue();

    do
    {
        printf("\n==== Tugas QUEUE 5231811022 ====\n");
        printf("Isi sementara queue: ");
        printQueue();
        printf("================================\n");
        printf("Menu:\n");
        printf("1. Tambahkan baru\n");
        printf("2. Hapus\n");
        printf("3. Edit\n");
        printf("4. Keluar\n");
        printf("Pilihan Anda: ");
        scanf(" %c", &choice);

        switch (choice)
        {
            case '1':
            {
                char addMore;
                do
                {
                    if (!full_queue())
                    {
                        int data;
                        printf("\nInput data: ");
                        scanf("%d", &data);
                        enQueue(data);
                        printf("Data berhasil ditambahkan ke dalam queue.\n");
                    }
                    else
                    {
                        printf("queue sudah penuh, silahkan ketik N untuk keluar.\n");
                    }

                    printf("Ingin menambah data lagi? (Y/N): ");
                    scanf(" %c", &addMore);
                } while (addMore == 'Y' || addMore == 'y');
                break;
            }
            case '2':
                if (!empty_queue())
                {
                    deQueue();
                    printf("Data pertama berhasil dihapus dari queue.\n");
                }
                else
                {
                    printf("queue sudah kosong.\n");
                }
                break;
            case '3':
                if (!empty_queue())
                {
                    int index, newData;
                    printf("Masukkan indeks data yang ingin diubah (0-%d): ", tail);
                    scanf("%d", &index);
                    if (index >= 0 && index <= tail)
                    {
                        printf("Masukkan data baru: ");
                        scanf("%d", &newData);
                        editQueue(index, newData);
                        printf("Data berhasil diubah.\n");
                    }
                    else
                    {
                        printf("Indeks tdk valid.\n");
                    }
                }
                else
                {
                    printf("queue kosong, tdk ada yang bisa diubah.\n");
                }
                break;
            case '4':
                printf("Keluar dari program.\n");
                break;
            default:
                printf("Pilihan tdk valid. Silakan pilih 1-4.\n");
        }
    } while (choice != '4');

    return 0;
}

void create_queue()
{
    head = -1;
    tail = -1;
}

bool full_queue()
{
    return (tail == MAX - 1);
}

bool empty_queue()
{
    return (head == -1);
}

void enQueue(int data)
{
    if (full_queue())
    {
        printf("queue penuh, tdk bisa menambahkan data.\n");
    }
    else
    {
        if (head == -1)
        {
            head = 0;
        }
        tail++;
        queue[tail] = data;
    }
}

void deQueue()
{
    if (empty_queue())
    {
        printf("queue kosong, tdk ada yg bisa dihapus.\n");
    }
    else
    {
        printf("Elemen yg dihapus: %d\n", queue[head]);
        for (int i = head; i < tail; i++)
        {
            queue[i] = queue[i + 1];
        }
        tail--;
        if (tail == -1)
        {
            head = -1;
        }
    }
}

void editQueue(int index, int newData)
{
    if (index >= head && index <= tail)
    {
        queue[index] = newData;
    }
    else
    {
        printf("Indeks tak valid.\n");
    }
}

void printQueue()
{
    if (empty_queue())
    {
        printf("queue lagi kosong nih.\n");
    }
    else
    {
        for (int i = head; i <= tail; i++)
        {
            printf("%d ", queue[i]);
        }
        printf("\n");
    }
}
