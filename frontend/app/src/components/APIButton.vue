<template>
  <button class="APIButton" @click="passedFunctionHandler">
    <span>{{ name }}</span>
  </button>
</template>

<script>
export default {
  props: {
    name: String,
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
.APIButton {
  width: 20%;
  padding: 10px;
  border: none;
  border-radius: 30px;
  background-color: rgb(0, 100, 255);
  font-weight: bold;
  color: white;
  margin: 20px;
}
.APIButton:hover {
  filter: brightness(1.25);
  transition: 0.25s;
}
.APIButton:active {
  filter: brightness(0.75);
  transform: scale(0.95);
  transition: 0.25s;
}
</style>
