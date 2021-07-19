from Gcoin import GCoinBlock
from visualizer import visualize


def main():
	block1 = GCoinBlock('Genesis', ['Mike', 'Joe', 4.5])
	block2 = GCoinBlock(block1.hash, ['Alex', 'Rick', 9.0])
	block3 = GCoinBlock(block2.hash, ['Romero', 'Mike', 4.5])
	block4 = GCoinBlock(block3.hash, ['Mike', 'Joe', 90.3])
	block5 = GCoinBlock(block4.hash, ['Rick', 'John', 100.5])


	visualizer =  visualize(block1, block2, block3, block4, block5)


if __name__ == '__main__':
	main()