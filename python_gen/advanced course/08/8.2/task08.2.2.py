'''Книги на прочтение 
Ученики 10 класса онлайн-школы BEEGEEK получили задание прочесть на летних каникулах три книги:

"Что такое математика?";
"Математическая составляющая";
"100 гениальных идей по математике".
Оказалось, что n учеников прочитали первую книгу, m учеников — вторую, k учеников — третью. Также известно, что x учеников прочли первую или вторую, или обе эти книги, y учеников — вторую или третью, или обе, z учеников — первую и третью, или хотя бы одну из этих двух книг. Полностью выполнили задание только t учеников. Всего в 10 классе учится a учеников. Напишите программу, которая выводит сколько учеников:

прочитали только одну книгу
прочитали только две книги
не прочитали ни одной из рекомендованных книг
Формат входных данных
На вход программе подаются числа n,m,k,x,y,z,t,a, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести три числа в соответствии с условием задачи, каждое на отдельной строке.'''

n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
cross12=n+m-x-t
cross23=m+k-y-t
cross31=n+k-z-t
first_book_only=n-t-cross12-cross31
second_book_only=m-t-cross12-cross23
third_book_only=k-t-cross23-cross31
one_book_readers=first_book_only+second_book_only+third_book_only
print(one_book_readers)
two_books_readers=cross12+cross23+cross31
print(two_books_readers)
lazy_asses=a-t-one_book_readers-two_books_readers
print(lazy_asses)