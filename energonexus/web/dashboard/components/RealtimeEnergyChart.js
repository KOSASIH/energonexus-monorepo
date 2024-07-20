import React, { useState, useEffect } from 'eact';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip } from 'echarts';
import WebSocket from 'ws';

const RealtimeEnergyChart = () => {
  const [data, setData] = useState([]);
  const [ws, setWs] = useState(null);

  useEffect(() => {
    setWs(new WebSocket('ws://localhost:8080/energy-stream'));

    ws.onmessage = (event) => {
      const newData = JSON.parse(event.data);
      setData((prevData) => [...prevData, newData]);
    };

    return () => {
      ws.close();
    };
  }, []);

  return (
    <LineChart width={800} height={400} data={data}>
      <Line type="monotone" dataKey="energy_consumption" stroke="#8884d8" />
      <XAxis dataKey="timestamp" />
      <YAxis />
      <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
      <Tooltip />
    </LineChart>
  );
};

export default RealtimeEnergyChart;
