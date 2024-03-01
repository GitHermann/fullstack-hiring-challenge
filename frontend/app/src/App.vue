<template>
  <div class="main">
    <div class="leftBox">
      <div class="APIBox">
        <APIButton
          name="List the datasets"
          :passedFunction="callGetAllDatasetAPI"
        />
        <div>
          <APIButton
            name="Upload a dataset"
            :passedFunction="callPostDatasetAPI"
          />
          <input
            type="file"
            ref="fileUpload"
            @change="handleFileChange"
            accept=".csv"
          />
        </div>
      </div>
      <div class="datasetListBox">
        <Dataset
          v-for="datasetName in datasetsNames"
          :datasetName="datasetName"
          @refreshDatasets="callGetAllDatasetAPI"
          @fetchedFormattedDataset="setFormattedDataset"
        />
      </div>
    </div>
    <div class="rightBox">
      <Chart
        v-for="element in formattedDataset"
        :email="element.email"
        :payments="element.payments"
      />
    </div>
  </div>
</template>

<script>
import APIButton from "./components/APIButton.vue";
import Dataset from "./components/Dataset.vue";
import Chart from "./components/Chart.vue";
import { getAllDatasets, postCsv } from "../api/csv";

export default {
  data() {
    return {
      datasetsNames: [],
      formattedDataset: {},
      uploadedFile: null,
    };
  },
  components: {
    APIButton,
    Dataset,
    Chart,
  },
  methods: {
    async test() {
      console.log("HELLO");
    },
    async callGetAllDatasetAPI() {
      try {
        this.datasetsNames = await getAllDatasets();
      } catch (error) {
        console.error(error);
      }
    },
    setFormattedDataset(formattedDataset) {
      this.formattedDataset = formattedDataset;
    },
    resetUploadedFile() {
      this.uploadedFile = this.$refs.fileUpload.files[0];
    },
    async callPostDatasetAPI() {
      console.log(this.$refs.fileUpload.files);
      this.uploadedFile = this.$refs.fileUpload.files[0];
      try {
        await postCsv(this.uploadedFile);
        this.callGetAllDatasetAPI();
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
  width: 35%;
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

.rightBox {
  width: 65%;
  height: 85vh;
  margin: 10px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  background-color: white;
  border-radius: 30px;
  box-shadow: 3px 3px 3px rgb(230, 230, 230);
  overflow: auto;
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
