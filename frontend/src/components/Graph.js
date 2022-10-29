import React, { useState } from 'react';
import store from "../store";

import { Line } from "react-chartjs-2";
import { Chart as ChartJS, registerables } from 'chart.js';
import { Chart } from 'react-chartjs-2'
ChartJS.register(...registerables);

function Graph(){
    
    const [data,setData] = useState({
      labels: store.getState().marketPrices.map((item,idx) => item.date),
      datasets: [
        {
          label: "Plot",
          backgroundColor: "rgb(255, 99, 132)",
          borderColor: "rgb(255, 99, 132)",
          data: store.getState().marketPrices.map((item,idx) => item.price),
        },
      ],
    });
    
    // const [plot_data, update_data] = useState([
    //     {
    //         x: store.getState().marketPrices.map((u_data,idx) =>  idx),
    //         y: store.getState().marketPrices.map((u_data) => u_data.price),
    //         type: 'scatter',
    //         mode: 'lines+markers',
    //         marker: {color: 'red'},
    //     },
    // ]);
    store.subscribe(()=>{
        console.log("Graph.js: store.subscribe() called", store.getState().marketPrices);
        // update_data([{
        //     x: store.getState().marketPrices.map((u_data,idx) => idx),
        //     y: store.getState().marketPrices.map((u_data) => u_data.price),
        //     type: 'scatter',
        //     mode: 'lines+markers',
        //     marker: {color: 'red'},
        // }]);
        setData({
            labels:store.getState().marketPrices.map((item,idx) => item.date),
            datasets: [
              {
                label: "Plot",
                backgroundColor: "rgb(255, 99, 132)",
                borderColor: "rgb(255, 99, 132)",
                data: store.getState().marketPrices.map((item,idx) => item.price),
              },
            ],
          });
    });
    return (
        <Line data={data} />
    );
}


export default Graph;