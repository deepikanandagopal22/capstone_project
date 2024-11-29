import React from 'react';
import ProductList from './components/ProductList';
import AddProduct from './components/AddProduct';

function App() {
  return (
    <div className="App">
      <h1>E-commerce App</h1>
      <AddProduct />
      <ProductList />
    </div>
  );
}

export default App;

