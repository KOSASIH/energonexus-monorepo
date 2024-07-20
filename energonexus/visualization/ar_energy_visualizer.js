import * as THREE from 'three';
import { ARButton } from 'three/examples/jsm/webxr/ARButton.js';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const controls = new OrbitControls(camera, renderer.domElement);

const loader = new GLTFLoader();
loader.load('energy_model.glb', (gltf) => {
    const energyModel = gltf.scene;
    scene.add(energyModel);
});

camera.position.z = 5;

function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}

animate();

const arButton = ARButton.createButton(renderer, {
    optionalFeatures: ['hit-test', 'dom-overlay'],
    domOverlay: { root: document.body }
});
document.body.appendChild(arButton);

arButton.addEventListener('click', () => {
    const geometry = new THREE.BoxGeometry(1, 1, 1);
    const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    const hitTestSource = renderer.xr.getHitTestSource(arButton);
    if (hitTestSource) {
        renderer.xr.setHitTestSource(hitTestSource);

        const frame = renderer.xr.getFrame();
        const hitTestResults = frame.getHitTestResults(hitTestSource);

        if (hitTestResults.length > 0) {
            const hit = hitTestResults[0];
            cube.position.copy(hit.getPose(camera).transform.position);
            cube.rotation.setFromQuaternion(hit.getPose(camera).transform.rotation);
        }
    }
});
