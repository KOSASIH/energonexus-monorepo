// node_red_flow.js
const NodeRED = require("node-red");

// Create a new Node-RED flow
const flow = new NodeRED();

// Add nodes to the flow
flow.addNode({
  id: "energy-usage",
  type: "mqtt in",
  topic: "energy/usage"
});

flow.addNode({
  id: "energy-production",
  type: "mqtt in",
  topic: "energy/production"
});

flow.addNode({
  id: "dashboard",
  type: "ui dashboard",
  nodes: ["energy-usage", "energy-production"]
});

// Deploy the flow
flow.deploy();
