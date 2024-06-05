// JavaScript Documentdocument.addEventListener("DOMContentLoaded", function() {
    var canvas = document.getElementById('signaturePad');
    var clearButton = document.getElementById('clear');
    var ctx = canvas.getContext('2d');
    var drawing = false;

    function startDrawing(e) {
        drawing = true;
        draw(e);
    }

    function endDrawing() {
        drawing = false;
        ctx.beginPath();
        document.getElementById('signature').value = canvas.toDataURL();
    }

    function draw(e) {
        if (!drawing) return;
        ctx.lineWidth = 2;
        ctx.lineCap = 'round';
        ctx.strokeStyle = 'black';

        ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    }

    canvas.addEventListener('mousedown', startDrawing);
    canvas.addEventListener('mouseup', endDrawing);
    canvas.addEventListener('mousemove', draw);
    clearButton.addEventListener('click', function() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    });

    document.getElementById('contractForm').addEventListener('submit', function(e) {
        document.getElementById('signature').value = canvas.toDataURL();
    });
});
