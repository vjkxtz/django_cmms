import logo from './logo.svg';
import './App.css';
import React, { Component, Fragment } from 'react'
import Header from './components/header';
import Home from './components/home';

function App() {
  return (
    <Fragment>
      <Header />
      <Home />
      </Fragment>
  );
}

export default App;
