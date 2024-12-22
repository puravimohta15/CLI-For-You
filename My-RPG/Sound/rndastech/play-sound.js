const sound = require('sound-play');
const path = require('path');
const filePath = path.join(__dirname, 'test.mp3');
sound.play(filePath).then(() => {
    console.log('Sound playback completed!');
}).catch((err) => {
    console.error('Error during playback:', err);
});
