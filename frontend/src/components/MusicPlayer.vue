<template>
  <div class="music-player">
    <h2>Music List</h2>
    <ul>
      <li v-for="(song, index) in songs" :key="index">
        <div>{{ song.name }}</div>
        <button @click="togglePlayPause(index)">
          <i
            :class="
              isPlaying && currentSongIndex === index
                ? 'fas fa-pause'
                : 'fas fa-play'
            "
          ></i>
        </button>
      </li>
    </ul>
    <audio ref="audio" @ended="stopSong"></audio>
  </div>
</template>

<script>
export default {
  data() {
    return {
      songs: [
        { name: "CCCA-4hi(JSS)", file: "/music/CCCA-4hi.mp3" },
        {
          name: "Eagles-Hotel California",
          file: "/music/Eagles-Hotel-California.mp3",
        },
        {
          name: "F.O.O.L-Conflict",
          file: "/music/F.O.O.L-Conflict.mp3",
        },
        { name: "Ryllz-Nemesis", file: "/music/Ryllz-Nemesis.mp3" },
        {
          name: "SOZZA-Spartanos(Original Mix)",
          file: "/music/SOZZA-Spartanos.mp3",
        },
        {
          name: "Taylor Swift-The Archer",
          file: "/music/Taylor Swift-The Archer.mp3",
        },
        {
          name: "Taylor Swift-You Need To Calm Down",
          file: "/music/Taylor Swift-You Need To Calm Down.mp3",
        },
      ],
      currentSongIndex: null,
      isPlaying: false,
    };
  },
  computed: {
    currentSongUrl() {
      return this.currentSongIndex !== null
        ? this.songs[this.currentSongIndex].file
        : "";
    },
  },
  methods: {
    togglePlayPause(index) {
      if (this.isPlaying && this.currentSongIndex === index) {
        this.stopSong();
      } else {
        this.playSong(index);
      }
    },
    playSong(index) {
      this.currentSongIndex = index;
      this.isPlaying = true;
      this.$refs.audio.src = this.currentSongUrl;
      this.$refs.audio.load();
      this.$refs.audio.play().catch((error) => {
        console.error("播放失败:", error);
      });
    },
    stopSong() {
      this.isPlaying = false;
      this.$refs.audio.pause();
      this.$refs.audio.currentTime = 0;
    },
  },
};
</script>

<style scoped>
.music-player {
  font-family: Arial, sans-serif;
  padding: 20px;
}

h2 {
  margin-bottom: 10px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 5px 0;
  border: 1px solid transparent;
}
li div {
  width: 170px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 20px;
  color: #333;
}

button:hover {
  color: #4caf50;
}
</style>
