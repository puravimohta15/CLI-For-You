const { play } = require('sound-play');
const path = require('path');
const fs = require('fs');

class SoundPlayer {
    constructor(soundsPath = './sounds') {
        this.soundsPath = path.resolve(soundsPath);
        
        if (!fs.existsSync(this.soundsPath)) {
            fs.mkdirSync(this.soundsPath, { recursive: true });
            console.log(`Created sounds directory at: ${this.soundsPath}`);
        }
    }

    async play(soundFile) {
        const fullPath = path.join(this.soundsPath, soundFile);
        
        if (!fs.existsSync(fullPath)) {
            console.error(`Sound file not found: ${fullPath}`);
            throw new Error(`Sound file not found: ${fullPath}`);
        }

        try {
            console.log(`Playing sound: ${fullPath}`);
            await play(fullPath);
            console.log('Finished playing sound');
        } catch (err) {
            console.error('Error playing sound:', err);
            throw err;
        }
    }
}

async function testSound() {
    const player = new SoundPlayer();
    
    try {
        console.log('Starting sound test...');
        console.log('Current directory:', process.cwd());
        console.log('Sounds directory:', player.soundsPath);
        
        const files = fs.readdirSync(player.soundsPath);
        console.log('Available sound files:', files);
        
        if (files.length > 0) {
            console.log(`Found ${files.length} sound file(s), playing all...`);
        
            for (const file of files) {
                console.log(`Playing sound: ${file}`);
                try {
                    await player.play(file);
                    console.log(`${file} completed!`);
                } catch (err) {
                    console.error(`Error playing ${file}:`, err);
                }
            }
        } else {
            console.log('No sound files found in sounds directory');
        }
    } catch (err) {
        console.error('Error in sound test:', err);
    }
}

module.exports = SoundPlayer;

if (require.main === module) {
    testSound();
}
