<template>
  <div class="main">
    <div class="leftBox">
      <div class="APIBox">
        <APIButton
          name="List the datasets"
          :passedFunction="callGetAllDatasetAPI"
        />
        <APIButton name="Upload a dataset" />
      </div>
      <div class="datasetListBox">
        <Dataset
          v-for="dataset in datasets"
          :datasetName="dataset"
          @refreshDatasets="callGetAllDatasetAPI"
        />
      </div>
    </div>
    <div class="rightBox"></div>
  </div>
</template>

<script>
import APIButton from "./components/APIButton.vue";
import Dataset from "./components/Dataset.vue";
import { getAllDatasets } from "../api/csv";

export default {
  data() {
    return {
      datasets: [],
    };
  },
  components: {
    APIButton,
    Dataset,
  },
  methods: {
    async test() {
      console.log("HELLO");
    },
    async callGetAllDatasetAPI() {
      try {
        this.datasets = await getAllDatasets();
      } catch (error) {
        console.error(error);
      }
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
  width: 45%;
  height: 85vh;
  margin: 10px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.APIBox {
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

.datasetListBox {
  width: 100%;
  height: 45%;
  display: flex;
  flex-direction: column;
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
