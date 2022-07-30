import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Layout from './shared/layout';
import Hero from './hero/hero';
import MainSection from './main-section/main-section';
import FeaturedCollection from './featured-collection/featured-collection';
import SHOP_DATA from '../shop';

const HomePage = () => {
  const [products, setProducts] = useState(SHOP_DATA)

  const s = (object) => {
    console.log("object", object)
  }

  const url = "http://localhost:9466/api/v2/pages/?type=base.HomePage&fields=*";
  useEffect(() => {
    async function getProducts() {
      const config = {
        method: 'get',
        url: url,
        headers: { 
          'Content-type': 'application/json',
        }
      }
      await axios(config)
        .then(res => {
          // res.setHeader("Access-Control-Allow-Origin", "*")
          // res.setHeader("Access-Control-Allow-Methods", "*")
          // res.setHeader("Access-Control-Allow-Headers", "'Access-Control-Allow-Headers: Origin, Content-Type, X-Auth-Token'")
          console.log("res.data =========== ", res.data)
        })
    }
    getProducts();
  }, [])
  return (
    <>
      <Layout>
        <Hero />
        <MainSection />
        <FeaturedCollection products={products} />
      </Layout>
    </>
  );
}

export default HomePage;