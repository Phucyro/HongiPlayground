<template>
  <div class="introduction">
    <img src="../assets/mrRobot.jpg" alt="mrRobot" class="mrRobot">
    <div class="introduction-text">
      Welcome to my personal DevOps and AI playground.
    </div>
  </div>
</template>

<style scoped>
/* Make .introduction a flex container */
.introduction {
  display: flex;
  flex-direction: column; /* Stack items vertically */
  justify-content: center; /* Center items horizontally */
  align-items: center; /* Center items vertically */
}

/* Style for the image */
.mrRobot {
  max-width: 40%;
  max-height: 40%;
}

/* Style for the text */
.introduction-text {
  margin-top: 20px; /* Add some space between the image and text */
  text-align: center; /* Center the text */
}
</style>
