<template>
  <div class="datasetBox">
    <span>{{ datasetName }}</span>
    <span>File size: {{ size }} o</span>
    <DatasetActionButton
      iconImage="ri-delete-bin-line"
      :passedFunction="deleteDatasetMethod"
    />
    <DatasetActionButton iconImage="ri-line-chart-line" />
  </div>
</template>

<script>
import DatasetActionButton from "./DatasetActionButton.vue";
import { getDataset, deleteDataset } from "../../api/csv";

export default {
  data() {
    return {
      size: 0,
    };
  },
  props: {
    datasetName: String,
  },
  components: {
    DatasetActionButton,
  },
  async mounted() {
    this.size = await this.getSize();
  },
  methods: {
    async getSize() {
      try {
        return (await getDataset(this.datasetName.split(".")[0])).size;
      } catch (error) {
        console.error(error);
      }
    },
    async deleteDatasetMethod() {
      try {
        const response = await deleteDataset(this.datasetName.split(".")[0]);
        this.$emit("refreshDatasets");
        return response;
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
.datasetBox {
  width: 50%;
  height: 15%;
  padding: 10px;
  border: none;
  border-radius: 30px;
  background-color: lightgray;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  margin: 10px;
}
</style>
