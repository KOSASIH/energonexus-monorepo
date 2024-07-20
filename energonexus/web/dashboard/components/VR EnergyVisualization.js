import React, { useState, useEffect } from 'react';
import { Entity, Scene } from 'aframe-react';

const VREnergyVisualization = () => {
  const [scene, setScene] = useState(null);
  const [entities, setEntities] = useState([]);

  useEffect(() => {
    const scene = (
      <Scene>
        <Entity geometry="primitive: box" material="color: #ff0000" scale="1 1 1" />
        <Entity geometry="primitive: sphere" material="color: #00ff00" scale="0.5 0.5 0.5" />
      </Scene>
    );

    setScene(scene);
  }, []);

  return (
    <div style={{ width: '100%', height: '100vh' }}>
      {scene}
    </div>
  );
};

export default VREnergyVisualization;
