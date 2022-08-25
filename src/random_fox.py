from os import getcwd
from time import time
from pathlib import Path
from requests import get

class RandomFox:
	def __init__(self):
		self.api = "https://randomfox.ca"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}

	def save_file(
			self,
			content: bytes,
			location: str = getcwd()):
		with open(
			Path(location).joinpath(f"{time() * 1000}.jpg"),
		mode="wb+",
		) as file:
			file.write(content)
			file.close()
		return True

	def get_random_image_url(self):
		return get(
			f"{self.api}/floof",
			headers=self.headers).json()

	def get_images_url(self, count: int = 10):
		return get(
			f"{self.api}/api/v1/getfoxes?count={count}",
			headers=self.headers).json()

	def get_image_by_id(self, image_id: int):
		return self.save_file(get(
				f"{self.api}/images/{image_id}.jpg",
				headers=self.headers).content)
