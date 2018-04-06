<template>
  <div id="app">
    <h1 class="title"> demo app </h1>
    <div class="backcolor">
      <div class="select-block">
        <div class="block">
          <el-date-picker
            v-model="value1"
            type="date"
            placeholder="Pick a day"
            :picker-options="picupOption">
          </el-date-picker>
        </div>

        <div class="select">
          <el-select v-model="value2" clearable placeholder="Select">
            <el-option
              v-for="item in options1"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </div>

        <div class="select">
          <el-select v-model="value3" clearable placeholder="Select">
            <el-option
              v-for="item in options1"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </div>

        <div class="select">
          <el-select v-model="value4" clearable placeholder="Select">
            <el-option
              v-for="item in options1"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </div>

        <div class="select">
          <el-select v-model="value5" clearable placeholder="Select">
            <el-option
              v-for="item in options1"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </div>

      </div>
      <div class="button">
        <el-button type="primary" icon="el-icon-search" @click="Search">Search</el-button>
      </div>
    </div>
    <h2 class="val"> {{ value1 }} </h2>
    <h2 class="val"> {{ value2 }} </h2>
    <h2 class="val"> {{ value3 }} </h2>
    <h2 class="val"> {{ value4 }} </h2>
    <h2 class="val"> {{ value5 }} </h2>
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
      value2: '',
      value3: '',
      value4: '',
      value5: ''
    }
  },
  methods: {
    Search () {

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

h1.title {
  text-align: center;
  color: #8492A6;
}

.backcolor {
  background: #F5F5F5;
}

.select-block {
  height: 100%;
  padding: 5%;
}

.block {
  margin-top: auto;
  margin-left: 6%;
  float:left;
}

.select {
  margin-top: auto;
  margin-left: 5%;
  float:left;
}

h2.val {
  margin-top: 5px;
  padding-top: 5px;
  color: #8492A6;
  text-align: center;
}

.button {
  margin-top: auto;
  text-align: center;
}
</style>

