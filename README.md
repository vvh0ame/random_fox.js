# random_fox.js
Web-API for [randomfox.ca](https://randomfox.ca) to retrieve random fox images

## Example
```JavaScript
async function main() {
	const { RandomFox } = require("./random_fox.js")
	const randomFox = new RandomFox()
	const imageUrl = await randomFox.geRandomImageUrl()
	console.log(imageUrl)
}

main()
```
