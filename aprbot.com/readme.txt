Task 1.
Use English SpaCy lib, find all tokens with only digits and all proper nouns (PROPN, aka, personal nouns ) in the text, count it and output it right-aligned in the HTML.
For example, for the text "we need 2 tickets to Dublin, and 1/2 a spoon of milk" read from the stdin (use python myprogram.py < input.txt >output.html ) the program should output that "2" was found twice (output "2"), "1" was found once (output "1"), "Dublin" was found once (output "1").
������ 2.
�������� ��������� �� ������, �������� ��� ���������� �� stdout ��� ��������� ������������ N ���������� (0) � N ������ ����� (�� 1 �� N).
������ ��������� ������ ��������� ���: "python permute.py 5"
������, ��� N=5, ����� ��� ����� ����� 0 0 0 0 0 1 2 3 4 5 .
������� ����� ������������: 0000012345 ��� 5012034000
������ �������� ��� ����� ������������ ��� N=5 � ��������� �� � ����.
���������� � ������� wc ���������� ����� � ���� �����.
������� ����������?
���������� ������� �����, ������� ����� ��� �������� ��������� ��� N=7 (��� �� ������, ��� ��� �������� ������ ���� ����� ������ � �������, ������ ����� ������� ��������� ����� ���������� ������ ��� ������ ���������, ������ �� ������ ���������).
� ���� ������ ������� ��� ���������
��� ������ �2 ������� ���������� ����� ��� N=5
��� ������ �2 ������� ������������� ����� ��� N=7 � ������������ ��������� � ������������ ��������� ����� � �������� ��� N=7 ��� ������ ���������, � ����������, ��� �� �������� ��� ������.