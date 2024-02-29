<template>
  <div class="main">
    <div class="leftBox">
      <div class="test">
        <APIButton name="List the datasets" />
      </div>
      <div class="test"></div>
    </div>
  </div>
</template>

<script>
import APIButton from "./components/APIButton.vue";

export default {
  components: {
    APIButton,
  },
  methods: {
    async test() {
      console.log("HELLO");
    },
  },
};
</script>

<style scoped>
.main {
  height: 100vh;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: rgb(245, 245, 245);
}

.leftBox {
  width: 40%;
  height: 85vh;
  margin: 10px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.test {
  width: 100%;
  height: 45%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: white;
  border-radius: 30px;
  box-shadow: 3px 3px 3px rgb(230, 230, 230);
  text-align: center;
}
</style>

<style>
* {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  margin: 0;
  padding: 0;
}
</style>
