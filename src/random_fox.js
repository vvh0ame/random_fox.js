class RandomFox {
	constructor() {
		this.api = "https://randomfox.ca"
		this.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	}

	async getRandomImageUrl() {
		const response = await fetch(
			`${this.api}/floof`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getRandomImagesUrl(count = 10) {
		const response = await fetch(
			`${this.api}/api/v1/getfoxes?count=${count}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}
}

module.exports = {RandomFox}
