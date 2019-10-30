# def cal(*nums):
# 	res = 0
# 	for i in nums:
# 		res += i
# 	return res
# # print(cal(*[1,2,23,4]))

# def person(name, age, *, money = 22):
# 	print("name:", name, "age:", age, "other:", money)
# # person("jason", 22, money = 2000)

# def product(x, *args):
# 	res = x
# 	for i in args:
# 		res *= i
# 	return res
# print(product(1,2,3,4))

# def trim(s):
# 	if len(s) == 0: return s
# 	if s[0] != ' ' and s[-1] != ' ': return s
# 	if s[0] == ' ' and s[-1] != ' ': return trim(s[1:])
# 	if s[0] != ' ' and s[-1] == ' ': return trim(s[:-1])
# 	if s[0] == ' ' and s[-1] == ' ': return trim(s[1:-1])
# print(trim("           f      "))

# from collections import Iterable
# print(isinstance(1213, Iterable))

# a = [(k, v) for k, v in enumerate(['a',"b"])]
# print(a)

# print([m + n for m in "ada" for n in "dadad"])

# L1 = ['Hello', 'World', 18, 'Apple', None]
# print([s.lower() for s in L1 if isinstance(s, str)])

# for i in (j * j for j in range(100)):
	# print(i)

# def fib(max):
# 	n, a, b = 0, 0, 1
# 	while n < max:
# 		yield(b)
# 		a, b = b, a + b
# 		n += 1
# for i in fib(10):
# 	print(i)

# def tri(m):
# 	i = 0
# 	a = [1]
# 	while i < m:
# 		yield a
# 		a = [1] + [a[i] + a[i + 1] for i in range(len(a) - 1)] + [1]
# 		i += 1
# for i in tri(10):
# 	print(i)

# def add(a, b, f):
# 	return f(a) + f(b)
# print(add(-1, -2, abs))

# print(list(map(lambda x: x * x, [1,2,3,4,5])))

# from functools import reduce
# def add(x, y):
# 	return x + y
# print(reduce(lambda x, y: x + y, [1,2,3,4,5,6,7]))

# def odd_iter():
# 	n = 1
# 	while True:
# 		n += 2
# 		yield n

# def prime():
# 	yield 2
# 	it = odd_iter()
# 	while True:
# 		n = next(it)
# 		yield n
# 		it = filter(lambda x: x % n != 0, it)
# for i in prime():
# 	print(i)
# 	if i >= 10000: break

# print(sorted([1,2,3,4,-1,1,-4,1000], key = abs, reverse = True))

# from collections import Counter
# c = Counter([1,2,3,4,5])
# print(c[6])

# def lazy_sum(*args):
# 	def sum():
# 		res = 0
# 		for i in args:
# 			res += i
# 		return res
# 	return sum
# f = lazy_sum(1,2,3,4,)
# print(f())

# def createCounter(n = [1]):
# 	def counter():
# 		n[0] += 1
# 		return n[0]
# 	return counter
# f = createCounter()
# print(f())

# def createCounter():
# 	n = 1
# 	def counter():
# 		nonlocal n 
# 		n += 1
# 		return n
# 	return counter
# f = createCounter()
# print(f(), f(), f())


import functools
# def log(func):
# 	@functools.wraps(func)
# 	def wrapper(*args, **kw):
# 		print("call %s()" %func.__name__)
# 		return func(*args, **kw)
# 	return wrapper
# @log
# def now():
# 	print("2019-01-16")
# now()

# import time
# def dec(func):
# 	@functools.wraps(func)
# 	def wrapper(*args, **kw):
# 		print("%s executed in %s ms" %(func.__name__, time.strftime('%H.%M.%S',time.localtime())))
# 		return func(*args, **kw)
# 	return wrapper
# @dec
# def now():
# 	time.sleep(0.1)
# 	return 0
# now()


# import test
# test.greeting()
# print(test.private1())

# class Student:
# 	__slots__ = ("age")
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
# s = Student("jason", "M")
# print(hasattr(s, "name"))
# s.height = 1


# class Student(object):
# 	"""docstring for Student"""
# 	__slots__ = ("age","gender")
# 	def __init__(self):
# 		pass
# s = Student()
# s.gender = "M"
# print(s.gender)

# class Screen(object):
# 	"""docstring for Screen"""
# 	def __init__(self, h, w):
# 		self._h = h
# 		self._w = w
# 	@property
# 	def h(self):
# 		return self._h
# 	@h.setter
# 	def h(self, h):
# 		self._h = h
# 	def __str__(self):
# 		return "w : " + str(self._w)
# 	__repr__ = __str__
# sc = Screen(1, 2)
# print(sc)

# class Fib:
# 	def __init__(self):
# 		self.a, self.b = 0, 1
# 	def __iter__(self):
# 		return self
# 	def __next__(self):
# 		self.a, self.b = self.b, self.a + self.b
# 		if self.a > 10000:
# 			raise StopIteration()
# 		return self.a
# for n in Fib():
# 	print(n)

# from enum import Enum
# Month = Enum("Month",("Jan","Feb"))
# for name, member in Month.__members__.items():
# 	print(name, "=>", member, ",", member.value)

# import logging
# logging.basicConfig(level=logging.INFO)

# def err(i):
# 	try:
# 		assert i != 0, "i is zero"
# 		i = 1 / i
# 	except BaseException as e:
# 		# logging.exception(e)
# 		print(e)
# 	finally:
# 		print("END")
# err(0)	

# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)
