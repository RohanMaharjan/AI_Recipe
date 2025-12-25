async function uploadImage() {
    const fileInput = document.getElementById("imageInput");
    const output = document.getElementById("output");

    if (!fileInput.files.length) {
        alert("Please select an image");
        return;
    }

    const formData = new FormData();
    formData.append("image", fileInput.files[0]);

    const response = await fetch("/api/detect-food/", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    output.textContent = JSON.stringify(data, null, 2);
}
