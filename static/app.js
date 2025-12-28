async function uploadVideo() {
  const input = document.getElementById("videoInput");
  const status = document.getElementById("status");
  const video = document.getElementById("resultVideo");
  const download = document.getElementById("downloadBtn");

  if (!input.files.length) {
    alert("Please select a video");
    return;
  }

  status.innerText = "Running inference... ⏳ This may take time.";

  const formData = new FormData();
  formData.append("file", input.files[0]);

  const response = await fetch("http://127.0.0.1:8000/predict/video", {
    method: "POST",
    body: formData,
  });

  const data = await response.json();

  status.innerText = "Inference complete ✅";

  const videoUrl = data.output_video;
  video.src = videoUrl;
  video.hidden = false;
  video.load();

  download.href = videoUrl;
  download.hidden = false;

}
