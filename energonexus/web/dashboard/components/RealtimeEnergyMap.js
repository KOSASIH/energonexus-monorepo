import React, { useState, useEffect } from 'eact';
import { Map, TileLayer, Marker } from 'leaflet-react';
import 'leaflet/dist/leaflet.css';
import mapboxgl from 'apbox-gl';

const RealtimeEnergyMap = () => {
  const [map, setMap] = useState(null);
  const [markers, setMarkers] = useState([]);

  useEffect(() => {
    const map = new mapboxgl.Map({
      container: 'ap',
      style: 'apbox://styles/mapbox/streets-v11',
      center: [37.7749, -122.4194],
      zoom: 12,
    });

    setMap(map);

    // fetch energy consumption data from API
    fetch('/api/energy-consumption')
     .then(response => response.json())
     .then(data => {
        const markers = data.map((item) => (
          <Marker position={[item.latitude, item.longitude]}>
            <div>
              <h2>{item.energy_consumption} kWh</h2>
            </div>
          </Marker>
        ));
        setMarkers(markers);
      });
  }, []);

  return (
    <div id="map" style={{ width: '100%', height: '100vh' }}>
      <Map center={[37.7749, -122.4194]} zoom={12}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution="&copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a>"
        />
        {markers}
      </Map>
    </div>
  );
};

export default RealtimeEnergyMap;
