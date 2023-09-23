def linearseachproduct(productlist, tergetproduct):
  indices = []
  for index, product in enumerate(productlist):
    if product == tergetproduct:
      indices.append(index)
  return indices
# example usage:
products = ["shoes", "boot", "lofer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'
result = linearseachproduct(products, target)
print(result)