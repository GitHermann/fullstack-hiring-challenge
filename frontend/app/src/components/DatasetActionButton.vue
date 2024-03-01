<template>
  <button class="datasetActionButton" @click="passedFunctionHandler">
    <i :class="iconImage"></i>
  </button>
</template>

<script>
export default {
  props: {
    iconImage: String,
    passedFunction: Function,
  },
  methods: {
    passedFunctionHandler() {
      this.passedFunction();
    },
  },
};
</script>

<style scoped>
.datasetActionButton {
  width: 25px;
  height: 25px;
  padding: 5px;
  border: none;
  border-radius: 3px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: lightgrey;
}

.datasetActionButton:hover {
  filter: brightness(1.25);
  background-color: rgb(200, 200, 200);
  transition: 0.25s;
}

.datasetActionButton:active {
  filter: brightness(0.75);
  transform: scale(0.95);
  transition: 0.25s;
}
</style>
