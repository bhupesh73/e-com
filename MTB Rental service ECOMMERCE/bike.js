<script>
  function addToCart(productId) {
    // Retrieve the cart items from local storage or initialize an empty array
    let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

    // Check if the product already exists in the cart
    const existingItem = cartItems.find(item => item.productId === productId);

    if (existingItem) {
      // If the product already exists, increment its quantity
      existingItem.quantity++;
    } else {
      // If the product does not exist, add it to the cart with a quantity of 1
      cartItems.push({ productId, quantity: 1 });
    }

    // Save the updated cart items back to local storage
    localStorage.setItem('cartItems', JSON.stringify(cartItems));

    // Provide feedback to the user (optional)
    alert('Item added to cart!');
  }
</script>