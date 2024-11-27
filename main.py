import numpy as np
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    broadcasters_inn = np.zeros((5, 8, 10))

    broadcasters_inn[1, 4, 7] = 42
    print(broadcasters_inn)

    rng = np.random.default_rng(seed=42)

    broadcasters_inn = rng.choice(
        400,
        size=(5, 8, 10),
        replace=False
    )

    print(broadcasters_inn)

    staff_cleaning = -1 * np.ones((5, 8, 10))

    print(staff_cleaning)

    cleaned_broadcasters_inn = broadcasters_inn * staff_cleaning

    print(cleaned_broadcasters_inn)

    # try again

    staff_cleaning = -1 * np.ones((8, 10))
    print(staff_cleaning)

    cleaned_broadcasters_inn = broadcasters_inn * staff_cleaning
    print(cleaned_broadcasters_inn)

    # try again

    staff_cleaning = -1 * np.ones((5, 8, 1))

    print(staff_cleaning)

    cleaned_broadcasters_inn = broadcasters_inn * staff_cleaning
    print(cleaned_broadcasters_inn)

    # try again

    staff_cleaning = -1 * np.ones((1, 8, 1))

    print(staff_cleaning)

    cleaned_broadcasters_inn = broadcasters_inn * staff_cleaning
    print(cleaned_broadcasters_inn)

    # try again

    staff_cleaning = -1 * np.ones((5, 1, 1))

    print(staff_cleaning)

    cleaned_broadcasters_inn = broadcasters_inn * staff_cleaning
    print(cleaned_broadcasters_inn)

    # try again

    staff_cleaning = -1

    print(staff_cleaning)

    cleaned_broadcasters_inn = broadcasters_inn * staff_cleaning
    print(cleaned_broadcasters_inn)


new_arrays = np.broadcast_arrays(
    np.ones((5, 8, 1)),
    np.ones((5, 8, 10)),
)

print(new_arrays[0].shape)
# Output: (5, 8, 10)
print(new_arrays[1].shape)
# Output: (5, 8, 10)
# Code Block #21

new_arrays = np.broadcast_arrays(
    np.ones((3, 1, 7)),
    np.ones((1, 5, 1)),
)

print(new_arrays[0].shape)
# Output: (3, 5, 7)
print(new_arrays[1].shape)
# Output: (3, 5, 7)
# Code Block #22

new_arrays = np.broadcast_arrays(
    np.ones((3, 1, 7)),
    np.ones((5, 1)),
)

print(new_arrays[0].shape)
# Output: (3, 5, 7)
print(new_arrays[1].shape)
# Output: (3, 5, 7)
# Code Block #23

'''
new_arrays = np.broadcast_arrays(
    np.ones((3, 1, 7)),
    np.ones((5, 4)),
)

print(new_arrays[0].shape)
print(new_arrays[1].shape)
'''
# Code Block #24

# next
new_arrays = np.broadcast_arrays(
    np.ones((3, 1, 7)),
    np.ones((5, 1)),
    np.ones((3, 5, 1))
)

print(new_arrays[0].shape)
# Output: (3, 5, 7)
print(new_arrays[1].shape)
# Output: (3, 5, 7)
print(new_arrays[2].shape)
# Output: (3, 5, 7)
# next

new_array = np.broadcast_to(
    np.zeros((8, 10)),
    shape=(5, 8, 10),
)

print(new_array.shape)
# Output: (5, 8, 10)
# next

new_shape = np.broadcast_shapes(
    (8, 10),
    (5, 8, 10),
)

print(new_shape)
# Output: (5, 8, 10)
