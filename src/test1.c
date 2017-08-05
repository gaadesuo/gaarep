/*   program  name  mikan.c   */
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(void)
{
	int user, cpu;

	srand((unsigned)time(NULL));
	srand((unsigned)time(NULL));
	{
		printf("じゃんけんをしましょう！何を出しますか？\n");
		printf("1 グー、2 チョキ、3 パー 0やめる\n");
		scanf_s("%d", &user);
		cpu = rand() % 3 + 1;
		if (cpu == 1)
		{
			if (user == 0)

			if (user == 1)
			{
				printf("あなたはグーです。私もグーです。あいこになりました。\n");
			}
			else if (user == 2)
			{
				printf("あなたはチョキです。私はグーです。あなたは負けました。\n");
			}
			else if (user == 3)
			{
				printf("あなたはパー。私はグーです。あなたの勝ちです！！\n");
			}
		}
		else if (cpu == 2)
		{
			if (user == 1)
			{
				printf("あなたはグーです。私はチョキです。あなたが勝ちました。\n");
			}
			else if (user == 2)
			{
				printf("あなたはチョキです。私もチョキです。あいこになりました。\n");
			}
			else if (user == 3)
			{
				printf("あなたはパーです。私はチョキです。あなたは負けました。\n");
			}
		}
		else if (cpu == 3)
		{
			if (user == 1)
			{
				printf("あなたはグーです。私はパーです。あなたは負けました。\n");
			}
			else if (user == 2)
			{
				printf("あなたはチョキです。私はパーです。あなたが勝ちました。\n");
			}
			else if (user == 3)
			{
				printf("あなたはパーです。私もパーです。あいこになりました。\n");
			}
		}
	}
	return 0;
}