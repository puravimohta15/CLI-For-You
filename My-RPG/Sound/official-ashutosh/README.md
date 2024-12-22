
# Sound Player for CLI RPG Game

## Overview

A simple and efficient sound player implementation for CLI RPG games using the `sound-play` library. This system provides cross-platform audio playback with automatic directory management and error handling.

## Installation

### Install required package:

```bash
npm install sound-play
```

### Create the basic directory structure:

```plaintext
your-project/
  ├── sound-player.js
  └── sounds/           (created automatically if missing)
      ├── effect1.mp3
      └── effect2.mp3
```

## Features

- Automatic sound directory creation
- Support for multiple audio formats
- Error handling and logging
- Sequential sound playback testing
- Cross-platform compatibility

## Usage

### Basic Usage

```javascript
const SoundPlayer = require('./sound-player');

// Create player instance
const player = new SoundPlayer();

// Play a sound file
await player.play('test.mp3');
```

### Running Sound Tests

```javascript
// Test all sounds in the directory
node sound-player.js
```

## Class Documentation

### SoundPlayer Class

#### Constructor

```javascript
new SoundPlayer(soundsPath = './sounds')
```

- `soundsPath`: Optional path to the sounds directory (defaults to `./sounds`)
- Creates the sounds directory if it doesn't exist

#### Methods

##### play(soundFile)

```javascript
await player.play('test.mp3')
```

- `soundFile`: Name of the sound file to play
- Returns a `Promise` that resolves when playback completes
- Throws an error if the file is not found or playback fails

### Test Function

The included `testSound()` function:

- Logs current directory and sounds path
- Lists all available sound files
- Attempts to play each sound sequentially
- Provides detailed logging of playback status

Example output:

```plaintext
Starting sound test...
Current directory: /path/to/project
Sounds directory: /path/to/project/sounds
Available sound files: ["test.mp3", "test2.mp3"]
Found 2 sound file(s), playing all...
Playing sound: test.mp3
effect1.mp3 completed!
Playing sound: test2.mp3
effect2.mp3 completed!
```

## Error Handling

The system handles several types of errors:

- Missing sound directory (creates automatically)
- Missing sound files
- Playback errors

Example error output:

```plaintext
Sound file not found: C:\project\sounds\missing.mp3
Error playing sound: Error: File not found
```

## Dependencies

- `sound-play`: Audio playback functionality
- `path`: Path manipulation and resolution
- `fs`: File system operations

## File Structure

```plaintext
sound-player.js        // Main implementation file
sounds/                // Directory for sound files
  ├── effect1.mp3     // Sound files
  └── effect2.mp3
```

## Testing

Run the included test function:

```bash
node sound-player.js
```

This will attempt to play all sound files in the sounds directory sequentially.

## Best Practices

- Keep sound files in the designated sounds directory
- Use supported audio formats (MP3, WAV)
- Handle errors appropriately in your implementation
- Test sound playback before deployment

## Troubleshooting

### If sounds aren't playing:

- Check if the file exists in the sounds directory
- Verify the file format is supported
- Check if the system audio is working
- Look for error messages in the console

### If getting path errors:

- Ensure the sounds directory exists
- Check file permissions
- Verify file names match exactly
