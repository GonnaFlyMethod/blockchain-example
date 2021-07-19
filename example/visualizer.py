def visualize(*blocks):

	block_separator = "_" * 80
	for indx, block in enumerate(blocks):
		print(block_separator)
		print("Block num:", indx)
		print("Block hash:", block.hash)
		print(block.block_data)
		print(block_separator)

		for i in range(3):
			print("|".rjust(40))

		print("V".rjust(40))

	print("...")