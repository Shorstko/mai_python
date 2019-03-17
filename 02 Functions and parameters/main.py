# аргументы функции
# *args
def fn_args(*args):
  for arg in args:
    print(arg)

parameters = ("test.py", "in.txt", "out.csv")
fn_args(*parameters)

# **kwargs
def fn_kwargs(**kwargs):
  for k,v in kwargs.items():
    print(f"{k} {v}")

fn_kwargs(script_name="test.py", input_file="in.txt", output_file="out.csv")

# присваивание функции
def fn_to_delete():
  print("Эта функция - на удаление")

# присваиваем функцию переменной
fn_spare = fn_to_delete
print(type(fn_spare))
# функцию можно удалить так же, как и элемент списка
del fn_to_delete
# вызываем "запасную" функцию
print(fn_spare())
# здесь будет исключение, т.к. исходная функция уже не существует
fn_to_delete()