function uploadImage() {
    const imageInput = document.getElementById('imageUpload');
    if (!imageInput.files[0]) {
        alert('Please select an image.');
        return;
    }

    const formData = new FormData();
    formData.append('image', imageInput.files[0]);

    fetch('/api/track-food', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        window.location.href = '/analysis';
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to analyze image.');
    });
}