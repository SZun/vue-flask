<template>
  <v-app>
    <v-main>
      <div id="app">
        <h1>{{ response }}</h1>
      </div>
    </v-main>
  </v-app>
</template>

<script >
import axios from "axios"

export default {
  data(){
    return {
      response: ""
    }
  },
  mounted() {
    this.getRequest()
  },
  methods: {
    getRequest: async function () {
      const response = await axios.get("http://127.0.0.1:5000/")
      console.log("Response")
      console.log(response)
      this.response = response.data.test
    }
  }
}
</script>
