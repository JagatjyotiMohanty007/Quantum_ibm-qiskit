# ============================================
# Mutable vs Immutable in Python
# ============================================

# Immutable
x = 10
x = x + 5  # creates new object

# Mutable
arr = [1, 2, 3]
arr[0] = 99  # modifies same object

print("Immutable:", x)
print("Mutable:", arr)