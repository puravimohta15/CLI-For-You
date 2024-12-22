# Sound Playback Demo for RPG CLI Game

## Objective
This README details the implementation of a sound playback system for an RPG CLI game using Node.js. The goal was to identify and demonstrate a Node.js library that meets the following requirements:

- **Cross-platform compatibility** (Windows, macOS, Linux).
- **Ease of use** with simple function calls.
- **No extra software dependencies** required for playback.
- **Sound quality** with normal, undistorted playback.

## Recommended Library
### Library: `sound-play`

`sound-play` was selected for the following reasons:
- **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux.
- **Ease of Use**: Simple API with minimal configuration required.
- **No Dependencies**: Does not require additional software like VLC.
- **Active Support**: Lightweight and actively maintained.

## Alternative Libraries

1. **`play-sound`**
   - **Pros**:
     - Cross-platform compatibility.
     - Offers advanced features when external software is available.
   - **Cons**:
     - Requires external software (e.g., VLC) for advanced functionality.

2. **`node-wav-player`**
   - **Pros**:
     - Simple and reliable for `.wav` files.
   - **Cons**:
     - Limited to `.wav` file formats, does not support `.mp3` files.

3. **`audioplayer`**
   - **Pros**:
     - Lightweight and easy to use.
     - Cross-platform compatibility.
   - **Cons**:
     - Limited support for advanced playback features.

4. **`node-mp3-player`**
   - **Pros**:
     - Specifically designed for MP3 playback.
     - Lightweight and simple.
   - **Cons**:
     - Limited support for other formats like `.wav`.

5. **`howler.js`**
   - **Pros**:
     - Full-featured audio library with advanced controls.
     - Supports multiple file formats and features like looping and volume control.
   - **Cons**:
     - Larger library, may be overkill for simple sound playback.

6. **`speaker`**
   - **Pros**:
     - Streams audio directly to speakers.
     - Works well for low-level audio control.
   - **Cons**:
     - Requires more setup and knowledge of audio streams.

## Installation and Setup

### Prerequisites
- Node.js (version 14 or later)

### Steps to Install `sound-play`
1. Initialize a Node.js project (if not already done):
   ```bash
   npm init -y
   ```

2. Install the `sound-play` library:
   ```bash
   npm install sound-play
   ```

### How to Run the Script
1. Place an MP3 file (e.g., `test.mp3`) in the same directory as the script.
2. Run the script:
   ```bash
   node play-sound.js
   ```
3. Observe the playback and ensure the sound plays without issues.

## Testing and Validation

### Tested Environments
1. **Windows 11**:
   - Sound played successfully.
   - No additional software required.

2. **Ubuntu**:
   - Sound played successfully.
   - No additional software required.

### Proof of Functionality
- **Test File**: The MP3 file used for testing (`test.mp3`) is included in this folder.
- **Recording**: A recording (`demo-recording.mp4`) showing the script playing the sound is provided.

## Summary of Findings

| Library          | Pros                                                 | Cons                                    |
|------------------|-----------------------------------------------------|-----------------------------------------|
| `sound-play`     | Simple API, no dependencies, cross-platform         | Limited advanced features               |
| `play-sound`     | Advanced features with external software support    | Requires external software for some use |
| `node-wav-player`| Reliable for `.wav` files                           | Limited format support                  |
| `audioplayer`    | Lightweight and easy to use                         | Limited advanced playback features      |
| `node-mp3-player`| Designed for MP3 playback, lightweight              | Limited format support                  |
| `howler.js`      | Full-featured, advanced controls and multi-format   | Larger library, potentially overkill    |
| `speaker`        | Streams audio directly to speakers                  | Requires more setup                     |

### Recommendation
`sound-play` is the best choice for this project due to its simplicity, cross-platform compatibility, and lack of external dependencies.

## Folder Structure
```
Sound/
└── rndastech/
    ├── play-sound.js
    ├── test.mp3
    ├── demo-recording.mp4
    ├── README.md
```

## References
- [sound-play Documentation](https://www.npmjs.com/package/sound-play)
- [Node.js Documentation](https://nodejs.org/)
