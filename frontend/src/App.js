
import Graph from "./components/Graph";
import Portfolio from "./components/Portfolio";
import Tform from "./components/Tform";
import OrderBook from "./components/OrderBook";
import Navbar from "./components/Navbar";

function App() {
  return (
    <div className="container">
      <Navbar />
      <div className="row">
        <div className="col-8"><Graph /></div>
        <div className="col-4"><Tform /></div>
      </div>
      <div className="row">
        <div className="col-4"><Portfolio /></div>
        <div className="col-8"><OrderBook /></div>
      </div>
    </div>
  );
}

export default App;
