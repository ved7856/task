def test_three_equal(A, B, C):
  result= set([A, B, C])
  if len(result)==3:
    return 0
  else:
    return (4 - len(result))

print(test_three_equal(1, 1, 1))
print(test_three_equal(1, 2, 2))
print(test_three_equal(-1, -2, -3))
print(test_three_equal(-1, -1, -1))
