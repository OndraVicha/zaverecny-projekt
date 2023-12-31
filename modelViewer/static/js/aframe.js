 AFRAME.registerComponent('rotate-around-object', {
        schema: {
            speed: { default: 1 }
        },
        tick: function (time, timeDelta) {

            this.el.object3D.rotation.y += this.data.speed * (timeDelta / 1000);
        }
    });

    document.querySelector('#rotatingModel').setAttribute('rotate-around-object', { speed: 0.5 });