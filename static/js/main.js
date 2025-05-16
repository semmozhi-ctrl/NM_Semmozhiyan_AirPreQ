function previewFile() {
  const preview = document.getElementById('file-name');
  const file = document.querySelector('input[type=file]').files[0];
  preview.textContent = file ? file.name : 'No file selected';
}

