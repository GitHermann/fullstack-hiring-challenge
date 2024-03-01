<template>
  <div>
    {{ email }}
    <Bar :data="data" :options="options" />
  </div>
</template>

<script>
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";
import { Bar } from "vue-chartjs";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

export default {
  props: {
    email: String,
    payments: Object,
  },
  components: {
    Bar,
  },
  data() {
    return {
      dates: [],
      amounts: [],
      data: {
        labels: JSON.parse(JSON.stringify(this.payments.invoicing_dates)),
        datasets: [
          {
            label: "Amount Paid Each Month",
            data: JSON.parse(JSON.stringify(this.payments.amounts)),
            backgroundColor: "rgba(75, 192, 192, 0.2)",
            borderColor: "rgba(75, 192, 192, 1)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
      },
    };
  },
};
</script>
