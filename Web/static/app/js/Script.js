import * as THREE from 'Web/static/app/js/Three.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('model-viewer') });

const loader = new GLTFLoader();
let model;

loader.load('path/to/your/model.gltf', (gltf) => {
    model = gltf.scene;
    scene.add(model);
});

const animate = () => {
    requestAnimationFrame(animate);
    // Zde můžete přidat interaktivitu s modelem, jako je otáčení, přibližování, oddalování, atd.
    renderer.render(scene, camera);
};

animate();