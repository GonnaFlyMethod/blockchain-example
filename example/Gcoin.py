import hashlib


class GCoinBlock:

	def __init__(self, prev_block_hash, transaction_list):
		self.prev_block_hash = prev_block_hash
		self.transaction_list = transaction_list

		self.block_data = ''
		self.block_data += f"Sender: {self.transaction_list[0]}\n"
		self.block_data += f"Recevier: {self.transaction_list[1]}\n"
		self.block_data += f"Sum: {self.transaction_list[2]} G coin\n"
		self.block_data += f'Prev block hash: {self.prev_block_hash}'

		self.hash = hashlib.sha256(self.block_data.encode()).hexdigest()
