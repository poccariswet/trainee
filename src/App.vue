<template>
  <div id="app">
    <h1> gaw-gaw {{ value }}</h1>
    <div class="block">
      <div class="demo">日付</div>
      <el-date-picker
      v-model="value1"
      type="date"
      placeholder="Pick a day"
      :picker-options="picupOption">
    </el-date-picker>
    </div>

    <div class="select1">
      <el-select v-model="value2" clearable placeholder="Select">
        <el-option
          v-for="item in options1"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
    </div>
    <h2> {{ value1 }} </h2>
    <h2> {{ value2 }} </h2>
  </div>
</template>

<script>
export default {
  data () {
    return {
      picupOption: {
        disabledDate (time) {
          return time.getTime() > Date.now()
        }
      },
      options1: [{
        value: '1',
        label: 'Option1'
      }, {
        value: '2',
        label: 'Option2'
      }, {
        value: '3',
        label: 'Option3'
      }, {
        value: '4',
        label: 'Option4'
      }, {
        value: '5',
        label: 'Option5'
      }],
      value1: '',
      value2: ''
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100%;
}

</style>

