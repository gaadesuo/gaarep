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
		printf("����񂯂�����܂��傤�I�����o���܂����H\n");
		printf("1 �O�[�A2 �`���L�A3 �p�[ 0��߂�\n");
		scanf_s("%d", &user);
		cpu = rand() % 3 + 1;
		if (cpu == 1)
		{
			if (user == 0)

			if (user == 1)
			{
				printf("���Ȃ��̓O�[�ł��B�����O�[�ł��B�������ɂȂ�܂����B\n");
			}
			else if (user == 2)
			{
				printf("���Ȃ��̓`���L�ł��B���̓O�[�ł��B���Ȃ��͕����܂����B\n");
			}
			else if (user == 3)
			{
				printf("���Ȃ��̓p�[�B���̓O�[�ł��B���Ȃ��̏����ł��I�I\n");
			}
		}
		else if (cpu == 2)
		{
			if (user == 1)
			{
				printf("���Ȃ��̓O�[�ł��B���̓`���L�ł��B���Ȃ��������܂����B\n");
			}
			else if (user == 2)
			{
				printf("���Ȃ��̓`���L�ł��B�����`���L�ł��B�������ɂȂ�܂����B\n");
			}
			else if (user == 3)
			{
				printf("���Ȃ��̓p�[�ł��B���̓`���L�ł��B���Ȃ��͕����܂����B\n");
			}
		}
		else if (cpu == 3)
		{
			if (user == 1)
			{
				printf("���Ȃ��̓O�[�ł��B���̓p�[�ł��B���Ȃ��͕����܂����B\n");
			}
			else if (user == 2)
			{
				printf("���Ȃ��̓`���L�ł��B���̓p�[�ł��B���Ȃ��������܂����B\n");
			}
			else if (user == 3)
			{
				printf("���Ȃ��̓p�[�ł��B�����p�[�ł��B�������ɂȂ�܂����B\n");
			}
		}
	}
	return 0;
}