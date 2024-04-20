import React, { useState, useEffect } from 'react';

import axios from "axios"


function App() {
  const [cryptos, setCryptos] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await axios.get('http://127.0.0.1:8000/get_latest_data/');
      console.log(result.data)
      setCryptos(result.data);
    };

    fetchData();

    const interval = setInterval(() => {
      fetchData();
    }, 3000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h1>Cryptocurrency Dashboard</h1>
      <table border={5} cellPadding={15}>
        <thead>
          <tr>
            <th>Name</th>
            <th>Price</th>
            <th>1h%</th>
            <th>24h%</th>
            <th>7d%</th>
            <th>Market Cap</th>
            <th>Volume (24h)</th>
            <th>Circulating Supply</th>
          </tr>
        </thead>
        <tbody>
          {cryptos.map(crypto => (
            <tr key={crypto.id}>
              <td>{crypto.name}</td>
              <td>{crypto.price}</td>
              <td>{crypto.change_1h}</td>
              <td>{crypto.change_24h}</td>
              <td>{crypto.change_7d}</td>
              <td>{crypto.market_cap}</td>
              <td>{crypto.volume_24h}</td>
              <td>{crypto.circulating_supply}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
