import numpy as np
def generate_random_sales(min_val, max_val, size):
    return np.random.randint(min_val, max_val + 1, size)
if __name__ == "__main__":
    print("Test 1: Product A (50-100 units, 12 months)")
    product_a = generate_random_sales(50, 100, 12)
    print(f"Generated data: {product_a}")
    print(f"Min value: {product_a.min()}, Max value: {product_a.max()}")
    print(f"Number of values: {len(product_a)}\n")