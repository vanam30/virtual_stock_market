
import Graph from "./components/Graph";
import Portfolio from "./components/Portfolio";
import Tform from "./components/Tform";
import OrderBook from "./components/OrderBook";
import Navbar from "./components/Navbar";
import Transaction from "./components/Transaction";
import Actions from "./components/Actions";
import store from "./store";
import "./App.css"

function App() {
  return (
    <>
      <Navbar />
      <div className="row">
        <div className="col-7 card">
          <div className="card-body">
            <h5 class="card-title">Graph</h5>
            <Graph />
          </div>
        </div>
        <div className="col-3 card">
          <div className="card-body">
            <h5 class="card-title">Transaction Form</h5>
            <Tform />
          </div>
        </div>
      </div>
      <div className="row">
        <div className="col-3 card">
          <div className="card-body">
            <h5 class="card-title">User Portfolio</h5>
            <Portfolio />
          </div>
        </div>
        <div className="col-7 card">
          <div className="card-body">
            <h5 class="card-title">Order Book</h5>
            <OrderBook />
          </div>
        </div>
      </div>
      <div className="col-8 card">
          <div className="card-body" style={{ height: "400px", overflow: "scroll" }}>
            <h5 class="card-title">Transaction History</h5>
            <Transaction />
          </div>
        </div>
    </>
  );
}

export default App;
