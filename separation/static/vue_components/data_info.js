/**
 * Vue component
 * data-info
 * request element-ui
 * @authors
 * @date    2019-1-01
 */
// document.write('<script src="/static/vue_components/common/search_dialog.js"></script>');
Vue.component('data-info', {
    template:
        `
        <div v-show="currentMenu === 'dataInfo'">
            <div v-show="showDetail === 'n'">
                <el-breadcrumb separator-class="el-icon-arrow-right">
                  <el-breadcrumb-item><a :href="'/manage/data-remit-team/'">数据汇交</a></el-breadcrumb-item>
                  <el-breadcrumb-item><a :href="'/manage/data-remit-project/?teamId=' + allId.teamId">汇交项目</a></el-breadcrumb-item>
                  <el-breadcrumb-item><a :href="'/manage/data-remit-list/?projId=' + allId.projId">汇交计划</a></el-breadcrumb-item>
                  <el-breadcrumb-item v-if="dataSetPathData">{{ dataSetPathData.dataSetName }}</el-breadcrumb-item>
                </el-breadcrumb>
                <el-row>
                    <el-button type="warning" style="margin: 10px" @click="handleSpecificDDataSetPath">遍历</el-button>
                    <!--<el-button type="default" style="margin: 10px" @click="uploadFile">上传</el-button>-->
                    <el-button style="float: right;margin: 10px;" icon="el-icon-menu" @click="handleShow('y')"></el-button>
                    <el-button style="float: right;margin: 10px;" icon="el-icon-tickets" @click="handleShow('n')"></el-button>
                </el-row>
                <el-row><el-upload
                        ref="uploadEnclosure"
                        class="upload-demo"
                        :action="importFileUrl"
                        :on-change="getEnclosureFiles"
                        :on-remove="handleRemoveEnclosure"
                        multiple
                        :limit="3"
                        :on-exceed="handleExceedEnclosure"
                        :file-list="fileList">
                        <el-button style="margin: 10px" size="small" type="primary">点击上传</el-button>
                    </el-upload></el-row>
                <el-row>
                    <span style="margin: 10px;font-size: 12px;">上一次遍历时间：{{ rowPlanInfo.createTime | formatDate }}</span>
                    <span style="margin: 10px;font-size: 12px;">用时：{{ rowPlanInfo.runTime | floatNumberFilter }} 秒</span>
                    <span style="margin: 10px;font-size: 12px;">遍历文件：{{ rowPlanInfo.count }} 个</span>
                </el-row>
                <loader :loading-num="loadingNum"></loader>
                <div v-show="currentMenu === 'dataInfo'">
                    <el-table :data="server.raw" v-if="server.raw" v-show="showDetail === 'n'">
                        <el-table-column
                          label="文件名" prop="path">
                        </el-table-column>
                        <el-table-column
                          label="文件大小" prop="size" >
                          <template slot-scope="scope">{{ scope.row.size | formatSize}}</template>
                        </el-table-column>
                        <el-table-column
                          label="创建时间">
                          <template slot-scope="scope">{{ scope.row.createFileTime }}</template>
                        </el-table-column>
                    </el-table>
                    <el-table :data="server.raw" v-if="server.raw" v-show="showDetail === 'y'">
                        <el-table-column>
                          <template slot-scope="scope">
                            <img v-if="scope.row.children" :src="folderFileUrl" alt="" style="width: 3%;height: 3%;" />
                            <img v-else :src="folder1Url" alt="" style="width: 3%;height: 3%;" />
                            <span>{{ scope.row.path }}</span>
                          </template>
                        </el-table-column>
                    </el-table>
                    <!--<div :data="server.raw"  v-show="showFolder === 'y'">-->
                        <!--<el-col v-for="r in server.raw" :span="6">-->
                            <!--<img v-if="r.children" :src="folderFileUrl" alt="" style="width: 10%;height: 10%;" />-->
                            <!--<img v-else :src="folder1Url" alt="" style="width: 10%;height: 10%;" />-->
                            <!--<span>{{ r.filename }}</span>-->
                        <!--</el-col>-->
                    <!--</div>-->
                </div>
            </div>
            <div v-show="showDetail === 'y'">
                <el-row>
                    <el-button style="float: right;margin: 10px;" icon="el-icon-menu" @click="handleShow('y')"></el-button>
                    <el-button style="float: right;margin: 10px;" icon="el-icon-tickets" @click="handleShow('n')"></el-button>
                </el-row>
                <el-tabs v-model="activeName" :tab-position="tabPosition" @tab-click="handleClick">
                    <el-tab-pane label="基本信息" name="first">用户管理</el-tab-pane>
                    <el-tab-pane label="关键词" name="second">配置管理</el-tab-pane>
                    <el-tab-pane label="汇交信息" name="third">汇交信息</el-tab-pane>
                    <el-tab-pane label="信息1" name="fourth">信息</el-tab-pane>
                    <el-tab-pane label="信息2" name="five">信息</el-tab-pane>
                    <el-tab-pane label="信息3" name="six">信息</el-tab-pane>
                    <el-tab-pane label="信息4" name="seven">信息</el-tab-pane>
                 </el-tabs>
                <el-table :data="server.raw" v-if="server.raw">
                    <el-table-column
                      label="文件名" prop="path">
                    </el-table-column>
                    <el-table-column
                      label="文件大小" prop="size" >
                      <template slot-scope="scope">{{ scope.row.size | formatSize}}</template>
                    </el-table-column>
                    <el-table-column
                      label="创建时间">
                      <template slot-scope="scope">{{ scope.row.createFileTime }}</template>
                    </el-table-column>
                </el-table>
            </div>
        </div>
    `,
    props: {
        id: {
            default: ''
        },
        refresh: {
            default: false
        },
        currentMenu: {
            default: 'baseInfo'
        },
    },
    data() {
        return {
            url_datasubmit_plan: '/api/expedition/exp_datasubmitplan/',
            url_submit:'/api/expdata/ds_datasubmittedinfo/',
            url_submit_file:'/api/expdata/ds_datasubmittedfileInfo/',
            // form rules
            loadingNum: 0,
            server:{},
            dataSetServer:{},
            labelFile:false,
            folder1Url: '/static/image/folder1.png',
            folderFileUrl: '/static/image/folder-file.png',
            showDetail:'n',
            allId:{},
            rowPlanInfo:{createTime:'',},
            dataSetPathData:[],
            labelDataSetFile:false,
            fileList:[],
            importFileUrl:'',
            activeName:'second',
            tabPosition:'left',
        }
    },
    mounted() {
        this.getPlanServerFile();
        this.getSpecificDataSetPath();
    },
    filters: {
        formatSize(size) {
            if (size > 1024 * 1024 * 1024) {
                return Math.floor(size * 100 / (1024 * 1024 * 1024)) / 100 + ' G';
            } else if (size > 1024 * 1024) {
                return Math.floor(size * 100 / (1024 * 1024)) / 100 + ' M';
            } else if (size > 1024) {
                return Math.floor(size * 100 / 1024) / 100 + ' KB';
            } else {
                return Math.floor(size * 100) / 100 + ' B';
            }
        },
        formatDate(time) {
            if (time) {
                return time.split("T")[0];
            }
        },
        floatNumberFilter(num){
            if (num) {
                let realVal = parseFloat(num).toFixed(2);
                return parseFloat(realVal);
            }
        },
    },
    methods: {
        handleBack() {
            location.href = document.referrer;
        },
        handleShow(val){
            if (this.showDetail !== val) {
                this.showDetail = val;
            }
        },
        //uploadFiles数据上传
        uploadFile(){
            console.log("数据上传");

        },
        //文件上传
        //上传新闻附件
        getEnclosureFiles(file, fileList){
            this.fileList = fileList;
        },
        handlePreviewEnclosure(file) {
            console.log(file);
        },
        handleExceedEnclosure(files, fileList) {
            this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
        },
        beforeRemoveEnclosure(file, fileList) {
            return this.$confirm(`确定移除 ${ file.name }？`);
        },
        handleRemoveEnclosure(file, fileList) {
            this.fileList = fileList;
        },
        UploadUrl(){
            let fd = new FormData();
            let url = '/manage/upload-file/?path=';
            fd.append('file',this.fileList);//传文件
            fd.append('srid',this.aqForm.srid);//传其他参数
            this.axios.post(url + this.rowPlanInfo.currentPath,fd).then(function(res){
                    alert('成功');
            })
        },
        handleClick(tab, event) {
            console.log(tab, event);
        }
    },
    computed: {
    },
});