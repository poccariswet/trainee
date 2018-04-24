<template>
  <div id="app">
    <h1 class="title"> demo app </h1>
    <div class="backcolor">
      <div class="select-block">
        <div class="block">
          <el-date-picker
            v-model="value1"
            v-on:change="changevalue"
            type="date"
            placeholder="Pick a day"
            :picker-options="picupOption">
          </el-date-picker>
        </div>

        <div class="select">
          <el-select v-model="value2" v-on:change="getDPTData" clearable placeholder="Select">
            <el-option
              v-for="item in Bumonlist"
              :key="item.lCatId"
              :label="item.lCatName"
              :value="item.lCatId">
            </el-option>
          </el-select>
        </div>

        <div class="select">
          <el-select v-model="value3" v-on:change="getLINEData" clearable placeholder="Select">
            <el-option
              v-for="item in DPTlist"
              :key="item.l2CatId"
              :label="item.l2CatName"
              :value="item.l2CatId">
            </el-option>
          </el-select>
        </div>

        <div class="select">
          <el-select v-model="value4" v-on:change="getCLASSData" clearable placeholder="Select">
            <el-option
              v-for="item in LINElist"
              :key="item.mCatId"
              :label="item.mCatName"
              :value="item.mCatId">
            </el-option>
          </el-select>
        </div>

        <div class="select">
          <el-select v-model="value5" clearable placeholder="Select">
            <el-option
              v-for="item in CLASSlist"
              :key="item.sCatId"
              :label="item.sCatName"
              :value="item.sCatId">
            </el-option>
          </el-select>
        </div>

      </div>
      <div class="button">
        <el-button type="primary" icon="el-icon-search" @click="message">Search</el-button>
      </div>
    </div>
    {{ value2 }}
    {{ value3 }}
    {{ value4 }}
    {{ value5 }}

  </div>
</template>

<script>
const axios = require('axios');
export default {
  data () {
    return {
      picupOption: {
        disabledDate (time) {
          return time.getTime() > Date.now()
        }
      },
      value1: '',
      value2: '',
      value3: '',
      value4: '',
      value5: '',
      endpoint: 'https://faia9q1b3l.execute-api.ap-northeast-1.amazonaws.com/dev/getCategoryList',
      token: process.env.TOKEN_AOI,
      Bumonlist: [],
      DPTlist: [],
      LINElist: [],
      CLASSlist: []
    }
  },
  mounted () {
    this.getBumonData()
  },
  methods: {
    changevalue () { // ここで日付が選択されたら、イベントの発火
      var dateformat = require('dateformat');
      var now = new Date();
      if (dateformat(now, 'isoDate') > dateformat(this.value1, 'isoDate')){
        console.log(dateformat(this.value1, 'isoDate'));
      }
    },
    message () {
      if (this.value1 == '' || this.value1 == null) {
        this.$message({
          message: '日付が選択されていません',
          type: 'error',
          duration: 2500
        })
        return
      }
      this.getData()
    },
    getBumonData() {
      const url = this.endpoint
      axios.get(url).then((res) => {
        this.Bumonlist = res.data.plu_code
      }).catch( error => { console.log(error) } )
    },
    getDPTData() {
      const url = this.endpoint + '?token=' + this.token + '&lCatId=' + this.value2
      axios.get(url).then((res) => {
        this.DPTlist = res.data.plu_code
      }).catch( error => { console.log(error) } )
    },
    getLINEData() {
      const url = this.endpoint + '?token=' + this.token + '&l2CatId=' + this.value3
      axios.get(url).then((res) => {
        this.LINElist = res.data.plu_code
      }).catch( error => { console.log(error) } )
    },
    getCLASSData() {
      const url = this.endpoint + '?token=' + this.token + '&mCatId=' + this.value4
      axios.get(url).then((res) => {
        this.CLASSlist = res.data.plu_code
      }).catch( error => { console.log(error) } )
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

.el-table {
}

</style>
