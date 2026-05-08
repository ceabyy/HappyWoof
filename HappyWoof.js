const BASE_URL = window.location.hostname === '127.0.0.1'
    ? 'http://127.0.0.1:5000'
    : 'https://ceaby-happywoof.hf.space';

// buttons on page
const fileButton = document.getElementById("fileButton")
const submitButton = document.getElementById("submitButton")

// variables for where dog photos go in html file - 3 columns, 2 rows, left to right, top to bottom.
const photo1 = document.getElementById("photo1")
const photo2 = document.getElementById("photo2")
const photo3 = document.getElementById("photo3")
const photo4 = document.getElementById("photo4")
const photo5 = document.getElementById("photo5")
const photo6 = document.getElementById("photo6")

// for handling photos

const dogPhotos = [];
const dogData = [];
let currentPhotoAmount = 0;

//progress bars

const moods = ['angry', 'happy', 'relaxed', 'sad'];
const bars = {};

for (let i = 1; i <= 6; i++) {
    bars[i] = {};
    for (const mood of moods) {
        bars[i][mood] = document.getElementById(`${mood}${i}`);
    }
};

// submitbutton false unless file provided
fileButton.addEventListener('change', () => {
    submitButton.disabled = !fileButton.files.length;
});

submitButton.addEventListener('click', async () => {
    const formData = new FormData();
    formData.append('image', fileButton.files[0]);

    const response = await fetch(`${BASE_URL}/predictDog`, {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    console.log(result);
    console.log(dogPhotos);
    console.log(dogData);

    // check if there are 6 photos already
    if (currentPhotoAmount >= 6) {
        dogPhotos.pop();
        dogData.pop();
        currentPhotoAmount -= 1;
    };

    dogPhotos.unshift(URL.createObjectURL(fileButton.files[0]));
    dogData.unshift(result);

    currentPhotoAmount += 1; // increment amount of photos tracked  
    
    // adjust all data to reflect the new indices
    for (let i=0; i<currentPhotoAmount; i++) {
        const photo = document.getElementById(`photo${i+1}`)
        photo.src = dogPhotos[i];

        photo.style.maxWidth = '300px';
        photo.style.maxHeight = '300px';
        photo.style.paddingTop = '10px';
        photo.style.objectFit = 'contain';

        document.getElementById(`dogEmotion${i+1}`).textContent = `Your dog seems to be ${dogData[i].prediction}!`;

        for (const mood of moods) {
            document.getElementById(`${mood}${i+1}`).value = dogData[i][mood];
        };

    };
});

