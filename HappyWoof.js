const BASE_URL = window.location.hostname === '127.0.0.1'
    ? 'http://127.0.0.1:5000'
    : 'https://happywoof.onrender.com';

// buttons on page
const fileButton = document.getElementById("fileButton")
const submitButton = document.getElementById("submitButton")

// variables for where dog photos go in html file - 3 columns, 2 rows, left to right, top to bottom.
const photo1 = document.getElementById("photo1")
const photo2 = document.getElementById("photo2")
const photo3 = document.getElementById("pPhoto3")
const photo4 = document.getElementById("photo4")
const photo5 = document.getElementById("photo5")
const photo6 = document.getElementById("photo6")

// titles

const dogTitle1 = document.getElementById("dogEmotion1")

//progress bars

const angry1 = document.getElementById("angry1")
const happy1 = document.getElementById("happy1")
const relaxed1 = document.getElementById("relaxed1")
const sad1 = document.getElementById("sad1")

// submitbutton false unless file provided
fileButton.addEventListener('change', () => {
    submitButton.disabled = !fileButton.files.length;
});

submitButton.addEventListener('click', async () => {
    const formData = new FormData();
    formData.append('image', fileButton.files[0]);

    const response = await fetch('/predictDog', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    console.log(result);

    // change photo and progress bars

    photo1.src = URL.createObjectURL(fileButton.files[0]);
    photo1.style.maxWidth = '300px';
    photo1.style.maxHeight = '300px';
    photo1.style.paddingTop = '10px';
    photo1.style.objectFit = 'contain';

    dogTitle1.textContent = `Your dog seems to be ${result.prediction}!`

    // find a way to make this more efficient
    angry1.value = result.angry
    happy1.value = result.happy
    relaxed1.value = result.relaxed
    sad1.value = result.sad 
});

