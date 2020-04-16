<template>
  <div class="uploadFile">
    <el-row>
      <el-upload
        class="upload-demo"
        action="http://127.0.0.1:8000/api/uploadFile"
        :on-success="uploadSuccess"
        :before-upload="beforeAvatarUpload"
        :show-file-list="false"
        :file-list="fileList">
        <el-button size="small" type="primary">点击上传</el-button>
        <div slot="tip" class="el-upload__tip">只能上传音频文件，且不超过2MB</div>
      </el-upload>
    </el-row>
    <el-row>
<!--      <router-link to="/home">-->
<!--        <el-button size="small" type="primary">跳转</el-button>-->
<!--      </router-link>-->
      <el-button size="small" type="primary" @click="turnToPage()">跳转</el-button>
    </el-row>
    <el-row>
      <el-table :data="uploadFileList" style="width: 100%" border>
        <el-table-column prop="id" label="编号" min-width="100">
          <template scope="scope"> {{ scope.row.pk }} </template>
        </el-table-column>
        <el-table-column prop="book_name" label="文件名" min-width="100">
          <template scope="scope"> {{ scope.row.fields.file_name }} </template>
        </el-table-column>
        <el-table-column prop="user_name" label="上传人" min-width="100">
          <template scope="scope"> {{ scope.row.fields.user_name }} </template>
        </el-table-column>
        <el-table-column prop="upload_time" label="上传时间" min-width="100">
          <template scope="scope"> {{ scope.row.fields.upload_time }} </template>
        </el-table-column>
        <el-table-column prop="file_type" label="文件类型" min-width="100">
          <template scope="scope"> {{ scope.row.fields.file_type }} </template>
        </el-table-column>
        <el-table-column prop="status" label="操作" min-width="100">
          <template scope="scope">
            <el-button type="text" size="mini" @click="deleteUploadFile(scope.row.pk)" v-if="scope.row.fields.status==1">删除</el-button>
            <el-button type="text" size="mini" disabled="true" v-else-if="scope.row.fields.status==0">已经删除</el-button>
            <audio :src="scope.row.fields.url" controls="controls"></audio>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>

</template>

<script>
    export default {
      name: "uploadFile",
      data () {
        return {
          input: '',
          uploadFileList: [],
          fileList:[]
        }
      },
      mounted: function () {
        this.showUploadFileList()
      },
      methods: {
        showUploadFileList () {
          this.$http.get('http://127.0.0.1:8000/api/show_upload_file')
            .then((response) => {
              var res = JSON.parse(response.bodyText)
              console.log(res)
              if (res.error_num === 0) {

                this.uploadFileList = res['list']
              } else {
                this.$message.error('查询书籍失败')
                console.log(res['msg'])
              }
            })

        },
        turnToPage() {

          this.$router.push("home")
        },
        deleteUploadFile(id){
          this.$http.get('http://127.0.0.1:8000/api/delete_upload_file?id='+id)
            .then((response) => {
              console.log(response)
              var res = JSON.parse(response.bodyText)
              if (res.error_num === 0) {
                console.log("fafa1")
                console.log(res.data[0]['pk'])
                console.log("fafa1")
                this.showUploadFileList()
              } else {
                this.$message.error('删除数据失败')
                console.log(res['msg'])
              }
            })
        },
        uploadSuccess(response){
          this.showUploadFileList()
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

<style scoped>

</style>
