<template>
  <div id="app">
    <h1 class="title"> 即時集計アプリ </h1>
    <div class="backcolor">
      <div class="select-block">
        <div class="block">
          <el-date-picker
            v-model="value1"
            v-on:change="changevalue"
            type="date"
            placeholder="日付"
            :picker-options="picupOption">
          </el-date-picker>
        </div>

        <div class="select">
          <el-select v-model="value2" v-on:change="getDPTData" clearable placeholder="Bumon Code">
            <el-option
              v-for="item in Bumonlist"
              :key="item.lCatId"
              :label="item.lCatName"
              :value="item.lCatId">
            </el-option>
          </el-select>
        </div>

        <div class="select">
          <el-select v-model="value3" v-on:change="getLINEData" clearable placeholder="DPT Code">
            <el-option
              v-for="item in DPTlist"
              :key="item.l2CatId"
              :label="item.l2CatName"
              :value="item.l2CatId">
            </el-option>
          </el-select>
        </div>

        <div class="select">
          <el-select v-model="value4" v-on:change="getCLASSData" clearable placeholder="Line Code">
            <el-option
              v-for="item in LINElist"
              :key="item.mCatId"
              :label="item.mCatName"
              :value="item.mCatId">
            </el-option>
          </el-select>
        </div>

        <div class="select">
          <el-select v-model="value5" clearable placeholder="Class Code">
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
    <el-table
      :data="PostList"
      style="width: 100%"
      height="600">
      <el-table-column
        fixed
        prop="Item.skucode"
        label="SKUコード"
        width="150">
      </el-table-column>
      <el-table-column
        fixed
        prop="Item.p_name"
        label="商品名"
        width="150">
      </el-table-column>
      <el-table-column label="売上数">
        <el-table-column
          prop="Item.9"
          label="~9"
          width="120">
        </el-table-column>
        <el-table-column
          prop="Item.10"
          label="~10"
          width="120">
        </el-table-column>
        <el-table-column
          prop="Item.11"
          label="~11"
          width="120">
        </el-table-column>
        <el-table-column
          prop="Item.12"
          label="~12"
          width="120">
        </el-table-column>
        <el-table-column
          prop="Item.13"
          label="~13"
          width="120">
        </el-table-column>
        <el-table-column
          prop="Item.14"
          label="~14"
          width="120">
        </el-table-column>
        <el-table-column
          prop="Item.15"
          label="~15"
          width="120">
        </el-table-column>
        <el-table-column
          prop="Item.16"
          label="~16"
          width="120">
        </el-table-column>
        <el-table-column
          prop="Item.17"
          label="~17"
          width="120">
        </el-table-column>
        <el-table-column
          prop="Item.18"
          label="~18"
          width="120">
        </el-table-column>
        <el-table-column
          prop="Item.19"
          label="~19"
          width="120">
        </el-table-column>
        <el-table-column
          prop="Item.20"
          label="~20"
          width="120">
        </el-table-column>
        <el-table-column
          prop="uriage"
          label="~21"
          width="120">
        </el-table-column>
        <el-table-column
          prop="uriage"
          label="~22"
          width="120">
        </el-table-column>
        <el-table-column
          prop="uriage"
          label="~23"
          width="120">
        </el-table-column>
        <el-table-column
          prop="uriage"
          label="~24"
          width="120">
        </el-table-column>
        <el-table-column
          prop="uriage"
          label="~25"
          width="120">
        </el-table-column>
      </el-table-column>
    </el-table>
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
      date_val: '',
      value2: '',
      value3: '',
      value4: '',
      value5: '',
      endpoint: '',
      token: '',
      Bumonlist: [],
      DPTlist: [],
      LINElist: [],
      CLASSlist: [],
      SampleList: []
    }
  },
  mounted () {
    this.getBumonData()
  },
  methods: {
    changevalue () { // ここで日付が選択されたら、イベントの発火
      const dateformat = require('dateformat');
      const now = new Date();
      if (dateformat(now, 'isoDate') > dateformat(this.value1, 'isoDate')){
        this.value1 = dateformat(this.value1, 'isoDate')
        const res = this.value1.split( '-' );
        this.date_val = res[0] + res[1] + res[2]
        console.log(this.date_val);
      }
    },
    message () {
      if (this.value1 == '' || this.value1 == null || this.value2 == '' || this.value2 == null) {
        this.$message({
          message: '日付が選択されていません',
          type: 'error',
          duration: 2500
        })
        return
      } else {
        this.SelectPost()
      }
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
    },
    SelectPost() {
      const url = ''
      let body = JSON.stringify({
        date: this.date_val,
        BUMONCode: this.value2,
        DPTCode: this.value3,
        LINECode: this.value4,
        CLASSCode: this.value5
    })

      axios.post(url, body, {
        headers:{
          'Content-type': 'application/json'
          }
      }).then((res) => {
        this.PostList = res.data
        console.log(res.data)
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
