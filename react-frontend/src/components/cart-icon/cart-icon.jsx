import React, { useContext } from 'react';
import withRouter from '../../withRouter';
import shoppingBag from '../../assets/shopping-bag.png';
import { CartContext } from '../../context/cart-context';
import { useNavigate } from "react-router-dom";
import './cart-icon.styles.scss';

const CartIcon = () => {
  const { itemCount, cartItems } = useContext(CartContext);
  const navigate = useNavigate();
  console.log('CartItems:', cartItems);
  return (
    <div className='cart-container' onClick={() => navigate('/cart')}>
      <img src={shoppingBag} alt='shopping-cart-icon' />
      {
        itemCount > 0 ? <span className='cart-count'> { itemCount } </span> : null
      }
      
    </div>
  );
}

export default withRouter(CartIcon);