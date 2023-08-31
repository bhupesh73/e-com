// Install the necessary dependencies: express and body-parser
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// Parse incoming request bodies as JSON
app.use(bodyParser.json());

// Handle the "Add to Cart" request
app.post('/api/cart', (req, res) => {
  const { productId } = req.body;

  // Perform any necessary validation or business logic here
  // Add the product ID to the cart in your database

  // Return a response indicating the successful addition of the item to the cart
  res.json({ message: 'Item added to cart' });
});

// Start the server
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
