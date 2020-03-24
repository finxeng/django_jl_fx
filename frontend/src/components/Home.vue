<template>
  <div class="home">
    <el-row display="margin-top:10px">
      <el-input v-model="input" placeholder="请输入书名" style="display:inline-table; width: 30%; float:left"></el-input>
      <el-button type="primary" @click="addBook()" style="float:left; margin: 2px;">新增</el-button>
    </el-row>
    <el-row>
      <el-table :data="bookList" style="width: 100%" border>
        <el-table-column prop="id" label="编号" min-width="100">
          <template scope="scope"> {{ scope.row.pk }} </template>
        </el-table-column>
        <el-table-column prop="book_name" label="书名" min-width="100">
          <template scope="scope"> {{ scope.row.fields.book_name }} </template>
        </el-table-column>
        <el-table-column prop="add_time" label="添加时间" min-width="100">
          <template scope="scope"> {{ scope.row.fields.add_time }} </template>
        </el-table-column>
      </el-table>
    </el-row>
    <el-row>
      <audio :src="src" controls="controls"></audio>
    </el-row>
    <el-row>
      <el-upload
        class="upload-demo"
        action="http://127.0.0.1:8000/api/upload"
        :on-success="uploadSuccess"
        :before-upload="beforeAvatarUpload"
        :show-file-list="false"
        :name="file"
        :file-list="fileList">
        <el-button size="small" type="primary">点击上传</el-button>
        <div slot="tip" class="el-upload__tip">只能上传音频文件，且不超过2MB</div>
      </el-upload>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: 'home',
    data () {
      return {
        input: '',
        bookList: [],
        src: '/static/video/ZOaFuTmGs30A.mp3',
        fileList: []
      }
    },
    mounted: function () {
      this.showBooks()
    },
    methods: {
      addBook () {
        this.$http.get('http://127.0.0.1:8000/api/add_book?book_name=' + this.input)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res.error_num === 0) {
              this.showBooks()
            } else {
              this.$message.error('新增书籍失败，请重试')
              console.log(res['msg'])
            }
          })
      },
      showBooks () {
        this.$http.get('http://127.0.0.1:8000/api/show_books')
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            console.log(res)
            if (res.error_num === 0) {
              this.bookList = res['list']
            } else {
              this.$message.error('查询书籍失败')
              console.log(res['msg'])
            }
          })
      },
      uploadSuccess(response){
        console.log(response.file_url)
        this.src = response.file_url
        this.$message('文件上传成功');
      },
      beforeAvatarUpload(file) {
        console.log(file.type)
        const isJPG = file.type === 'audio/wav'|| file.type=='audio/mp3';
        const isLt2M = file.size / 1024 / 1024 < 2;

        if (!isJPG) {
          this.$message.error('只能上传音频文件');
        }
        if (!isLt2M) {
          this.$message.error('文件大小不能超过2MB');
        }
        return isJPG && isLt2M;
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
</style>
